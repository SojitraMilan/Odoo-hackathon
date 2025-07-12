from odoo import models, fields

class Tag(models.Model):
    _name = 'stackit.tag'
    _description = 'Tag'

    name = fields.Char(string='Tag Name', required=True)