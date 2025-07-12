from odoo import models, fields # type: ignore

class Notification(models.Model):
    _name = 'stackit.notification'
    _description = 'Notification'

    user_id = fields.Many2one('res.users', string='User ')
    message = fields.Text(string='Message')
    is_read = fields.Boolean(string='Read', default=False)