# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from datetime import datetime

class office_department(osv.Model):
    _name = 'office.department'
    _description = 'Department'
    
    _columns = {
        'name': fields.char('Tên phòng ban', size=128, required=True),
        'description': fields.text('Mô tả'),
        'manager': fields.many2one('hr.employee', 'Trưởng phòng'),
        'employee_count': fields.integer('Số nhân viên'),
        'active': fields.boolean('Đang hoạt động'),
        'created_date': fields.date('Ngày tạo'),
        'state': fields.selection([
            ('active', 'Hoạt động'),
            ('inactive', 'Không hoạt động'),
            ('recruiting', 'Đang tuyển dụng'),
        ], 'Trạng thái', required=True),
    }

    _defaults = {
        'active': True,
        'created_date': fields.date.context_today,
        'state': 'active',
    }

    def name_get(self, cr, uid, ids, context=None):
        """ Hiển thị tên phòng ban """
        if not ids:
            return []
        result = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.name or 'Unknown'
            result.append((record.id, name))
        return result

    def create(self, cr, uid, vals, context=None):
        """ Kiểm tra trùng tên phòng ban khi tạo mới """
        if 'name' in vals:
            existing_ids = self.search(cr, uid, [('name', '=', vals['name'])], context=context)
            if existing_ids:
                raise osv.except_osv('loi', 'tao phong khac di!')
        return super(office_department, self).create(cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        """ Kiểm tra trùng tên khi cập nhật """
        if 'name' in vals:
            for dept_id in ids:
                existing_ids = self.search(cr, uid, [('name', '=', vals['name']), ('id', '!=', dept_id)], context=context)
                if existing_ids:
                    raise osv.except_osv('loi', 'tao phong khac di!')
        return super(office_department, self).write(cr, uid, ids, vals, context=context)

    def name_search(self, cr, uid, name='', args=None, operator='ilike', context=None, limit=100):
        """ Tìm kiếm phòng ban theo tên """
        if not args:
            args = []
        if name:
            ids = self.search(cr, uid, [('name', operator, name)] + args, limit=limit, context=context)
            return self.name_get(cr, uid, ids, context=context)
        return super(office_department, self).name_search(cr, uid, name=name, args=args, operator=operator, context=context, limit=limit)

    def _compute_employee_count(self, cr, uid, ids, field_name, arg, context=None):
        """ Tính số lượng nhân viên trong phòng ban """
        result = {}
        for department in self.browse(cr, uid, ids, context=context):
            employee_ids = self.pool.get('hr.employee').search(cr, uid, [('department_id', '=', department.id)], context=context)
            result[department.id] = len(employee_ids)
        return result
    def set_active(self, cr, uid, ids, context=None):
    
        return self.write(cr, uid, ids, {'state': 'active'}, context=context)
    def set_inactive(self, cr, uid, ids, context=None):
   
        return self.write(cr, uid, ids, {'state': 'inactive'}, context=context)
    _sql_constraints = [
        ('name_uniq', 'unique(name)',  'tao phong khac di!'),
    ]

    _order = 'name'  # Sắp xếp mặc định theo tên
