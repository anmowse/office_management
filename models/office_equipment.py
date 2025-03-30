# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class office_equipment(osv.osv):
    _name = 'office.equipment'
    _description = 'Thiết bị văn phòng'
    
    _columns = {
        'name': fields.char('Tên thiết bị', required=True),
        'equipment_type': fields.selection([
            ('computer', 'Máy tính'),
            ('printer', 'Máy in'),
            ('chair', 'Ghế'),
            ('desk', 'Bàn làm việc'),
            ('other', 'Khác'),
        ], 'Loại thiết bị', required=True),
        'serial_number': fields.char('Số seri'),
        'location': fields.char('Vị trí'),
        'department': fields.char('Phòng ban sử dụng'),
        'status': fields.selection([
            ('available', 'Đang sử dụng'),
            ('maintenance', 'Bảo trì'),
            ('broken', 'Hỏng'),
            ('retired', 'Ngưng sử dụng'),
        ], 'Tình trạng', required=True),
        'note': fields.text('Ghi chú'),
    }

office_equipment()
