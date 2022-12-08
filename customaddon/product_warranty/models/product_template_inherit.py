# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    product_warranty = fields.Text(string="Product Warranty", compute="warranty_code")
    date_from = fields.Datetime(string="From Date")
    date_to = fields.Datetime(string="To Date")

    # @api.depends('value')
    def _is_warranty(self):
        for record in self:
            if record.date_from and record.date_to and record.date_to > record.date_from:
                return True
            else:
                return False

    @api.depends("date_from", "date_to")
    def warranty_code(self):
        for record in self:
            if record._is_warranty():
                format_date_from = record.date_from.strftime("%d%m%y")
                format_date_to = record.date_to.strftime("%d%m%y")
                warranty_code = "PWR" + "/" + format_date_from + "/" + format_date_to
                record.product_warranty = warranty_code
            else:
                record.product_warranty = False
