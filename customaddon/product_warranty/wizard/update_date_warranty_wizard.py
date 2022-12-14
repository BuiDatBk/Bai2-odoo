from odoo import fields, models, api


class UpdateDateWarrantyWizard(models.TransientModel):
    _name = 'update.date.warranty.wizard'

    mess_date_from = fields.Datetime(string="From")
    mess_date_to = fields.Datetime(string="To")
    product_ids = fields.Many2many('product.product', string="Products")

    def add_date_warranty(self):
        for product in self.product_ids:
            product.date_from = self.mess_date_from
            product.date_to = self.mess_date_to
