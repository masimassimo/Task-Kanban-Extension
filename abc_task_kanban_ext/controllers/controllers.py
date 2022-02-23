# -*- coding: utf-8 -*-
# from odoo import http


# class TaskKanbanExt(http.Controller):
#     @http.route('/task_kanban_ext/task_kanban_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_kanban_ext/task_kanban_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_kanban_ext.listing', {
#             'root': '/task_kanban_ext/task_kanban_ext',
#             'objects': http.request.env['task_kanban_ext.task_kanban_ext'].search([]),
#         })

#     @http.route('/task_kanban_ext/task_kanban_ext/objects/<model("task_kanban_ext.task_kanban_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_kanban_ext.object', {
#             'object': obj
#         })
