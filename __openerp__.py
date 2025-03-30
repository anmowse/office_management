#!/usr/bin/env python
# -*- coding: utf-8 -*-
{
    'name': 'Quản lý Văn Phòng',
    'version': '1.0',
    'category': 'Văn Phòng',
    'sequence': 1,
    'summary': 'Hệ thống Quản lý Văn Phòng Toàn Diện',
    'description': """
Hệ Thống Quản Lý Văn Phòng
==========================
    """,
    'author': 'Đặng Hoài An',
    'website': 'http://www.yourcompany.com',
    'depends': [
        'base',
        'mail',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/office_department_view.xml',
        'views/office_equipment_view.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
