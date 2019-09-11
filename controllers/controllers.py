# -*- coding: utf-8 -*-
from openerp import http

# class Tacna(http.Controller):
#     @http.route('/tacna/tacna/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tacna/tacna/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tacna.listing', {
#             'root': '/tacna/tacna',
#             'objects': http.request.env['tacna.tacna'].search([]),
#         })

#     @http.route('/tacna/tacna/objects/<model("tacna.tacna"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tacna.object', {
#             'object': obj
#         })