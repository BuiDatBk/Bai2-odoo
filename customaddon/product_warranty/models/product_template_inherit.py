# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    _inherit = "product.product"

    product_warranty = fields.Text(string="Product Warranty", compute="warranty_code")
    date_from = fields.Datetime(string="From Date", groups="product_warranty.group_product_warranty")
    date_to = fields.Datetime(string="To Date", groups="product_warranty.group_product_warranty")
    currency_id = fields.Many2one('res.currency', string="Currency")
    product_discount_estimated = fields.Monetary('Discount',
                                                 # optional: currency_field='currency_id',
                                                 compute="discount_estimated"
                                                 )
    time_interval = fields.Text(string="Time Interval", compute="cal_day")
    has_valid_code = fields.Boolean(string="Valid Code", compute="compute_valid_code", store=True)

    def compute_valid_code(self):
        for record in self:
            if record.is_warranty():
                record.has_valid_code = True
            else:
                record.has_valid_code = False

    @api.depends("date_from", "date_to")
    def cal_day(self):
        for record in self:
            days = 0
            if record.is_warranty():
                days = (record.date_to - record.date_from).days
                if days % 365 == 0:
                    if days / 365 == 1:
                        record.time_interval = 'One year'
                    else:
                        record.time_interval = str(days / 365) + ' ' + 'years'
                elif days % 30 == 0:
                    if days / 30 == 1:
                        record.time_interval = 'One month'
                    else:
                        record.time_interval = str(days / 30) + ' ' + 'months'
                else:
                    if days == 1:
                        record.time_interval = 'One day'
                    else:
                        record.time_interval = str(days) + ' ' + 'days'
            else:
                record.time_interval = False

    # @api.depends('value')
    def is_warranty(self):
        for record in self:
            if record.date_from and record.date_to and record.date_to > record.date_from:
                return True
            else:
                return False

    @api.depends("date_from", "date_to")
    def warranty_code(self):
        for record in self:
            if record.is_warranty():
                format_date_from = record.date_from.strftime("%d%m%y")
                format_date_to = record.date_to.strftime("%d%m%y")
                warranty_code = "PWR" + "/" + format_date_from + "/" + format_date_to
                record.product_warranty = warranty_code
            else:
                record.product_warranty = False

    @api.depends("date_from", "date_to")
    def discount_estimated(self):
        for record in self:
            if record.is_warranty():
                record.product_discount_estimated = 0
            else:
                record.product_discount_estimated = record.standard_price * 0.1
