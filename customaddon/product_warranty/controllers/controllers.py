# -*- coding: utf-8 -*-
# from odoo import http


# class Customaddon/productWarranty(http.Controller):
#     @http.route('/customaddon/product_warranty/customaddon/product_warranty', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customaddon/product_warranty/customaddon/product_warranty/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customaddon/product_warranty.listing', {
#             'root': '/customaddon/product_warranty/customaddon/product_warranty',
#             'objects': http.request.env['customaddon/product_warranty.customaddon/product_warranty'].search([]),
#         })

#     @http.route('/customaddon/product_warranty/customaddon/product_warranty/objects/<model("customaddon/product_warranty.customaddon/product_warranty"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customaddon/product_warranty.object', {
#             'object': obj
#         })
