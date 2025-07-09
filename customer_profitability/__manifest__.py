# -*- coding: utf-8 -*-
{
    'name': 'Customer Profitability Analysis',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Analyze sales profitability per customer',
    'description': 'Calculates total sales, costs, and margins per customer using confirmed sales orders.',
    'author': 'Juan Sebastián Agudelo',
    'license': 'LGPL-3',
    'depends': ['sale', 'account', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_profitability_views.xml',
        'reports/customer_profitability_report.xml',
    ],
    'installable': True,
    'application': True,
}
