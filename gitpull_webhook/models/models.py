# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gitpull_webhook(models.Model):
#     _name = 'gitpull_webhook.gitpull_webhook'
#     _description = 'gitpull_webhook.gitpull_webhook'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
