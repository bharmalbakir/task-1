# -- coding: utf-8 --
{
    'name': 'Custom BOM',
    'sequence': -500,
    'author': 'Cloud infosoft',
    'version': '17.0',
    'license': 'LGPL-3',
    'depends': ['base','mrp'],
    'data': ['view/custom_purchase.xml',
             'security/ir.model.access.csv'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
