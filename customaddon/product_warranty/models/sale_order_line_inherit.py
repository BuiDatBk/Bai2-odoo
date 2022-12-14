from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = "sale.order.line"

    discount_warranty = fields.Monetary(string="Discount", compute="discount_estimated")

    def discount_estimated(self):
        for record in self:
            # FIXME: Phan quyen
            if record.product_id.is_warranty():
                record.discount_warranty = 0
            else:
                record.discount_warranty = record.price_subtotal * 0.1

