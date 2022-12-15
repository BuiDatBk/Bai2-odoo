from odoo import fields, models, api


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    discount_total = fields.Monetary(string="Discount Total", compute="all_discount")

    api.depends('order_line.discount_warranty')
    def all_discount(self):
        for record in self:
            order_line_list = record.env['sale.order.line'].search([('order_id', 'in', self.ids)])
            for line in order_line_list:
                record.discount_total += line.discount_warranty

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = discount_no_warranty = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax

            discount_no_warranty = order.discount_total

            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax - discount_no_warranty,
            })

