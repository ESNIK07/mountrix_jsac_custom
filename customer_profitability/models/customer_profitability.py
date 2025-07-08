# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class CustomerProfitabilityReport(models.Model):
    _name = 'customer.profitability.report'
    _description = 'Customer Profitability Report'
    _auto = False

    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    total_sales = fields.Monetary(string='Total Sales', currency_field='currency_id', readonly=True)
    total_cost = fields.Monetary(string='Total Cost', currency_field='currency_id', readonly=True)
    profit = fields.Monetary(string='Profit', currency_field='currency_id', readonly=True)
    margin = fields.Float(string='Margin (%)', readonly=True)
    currency_id = fields.Many2one('res.currency', string='Currency')

    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW customer_profitability_report AS (
                SELECT
                    MIN(so.id) AS id,
                    so.partner_id,
                    so.currency_id,
                    SUM(sol.price_subtotal) AS total_sales,
                    SUM(sol.product_uom_qty * pt.standard_price) AS total_cost,
                    SUM(sol.price_subtotal - (sol.product_uom_qty * pt.standard_price)) AS profit,
                    CASE
                        WHEN SUM(sol.price_subtotal) = 0 THEN 0
                        ELSE ROUND(((SUM(sol.price_subtotal - (sol.product_uom_qty * pt.standard_price)) / SUM(sol.price_subtotal)) * 100), 2)
                    END AS margin
                FROM
                    sale_order_line sol
                JOIN
                    sale_order so ON sol.order_id = so.id
                JOIN
                    product_product pp ON sol.product_id = pp.id
                JOIN
                    product_template pt ON pp.product_tmpl_id = pt.id
                WHERE
                    so.state IN ('sale', 'done')
                GROUP BY
                    so.partner_id, so.currency_id
            )
        """)


    def action_open_customer_sales(self):
        self.ensure_one()
        # Recuperar IDs de órdenes de venta válidas (las que aportan al total calculado)
        self.env.cr.execute("""
            SELECT DISTINCT so.id
            FROM sale_order_line sol
            JOIN sale_order so ON sol.order_id = so.id
            WHERE so.state IN ('sale', 'done') AND so.partner_id = %s
        """, [self.partner_id.id])
        sale_order_ids = [row[0] for row in self.env.cr.fetchall()]

        return {
            'type': 'ir.actions.act_window',
            'name': f'Órdenes válidas de {self.partner_id.name}',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', sale_order_ids)],
            'target': 'current',
            'context': {'default_partner_id': self.partner_id.id},
        }
    
# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'

#     estimated_cost = fields.Float(string='Estimated Cost', compute='_compute_estimated_cost', store=True)
#     date_order = fields.Datetime(related='order_id.date_order', store=True)

#     @api.depends('qty_delivered', 'product_id.standard_price')
#     def _compute_estimated_cost(self):
#         for line in self:
#             line.estimated_cost = line.product_uom_qty * line.product_template_id.standard_price