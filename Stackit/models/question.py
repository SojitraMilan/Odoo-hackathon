from odoo import models, fields, api # type: ignore

class Question(models.Model):
    _name = 'stackit.question'
    _description = 'Question'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title = fields.Char(string='Title', required=True, translate=True)
    description = fields.Html(string='Description')
    tags = fields.Many2many('stackit.tag', string='Tags')
    user_id = fields.Many2one('res.users', string='Asked By', default=lambda self: self.env.user)
    answer_ids = fields.One2many('stackit.answer', 'question_id', string='Answers')
    views = fields.Integer(string='Views', default=0)
    vote_score = fields.Integer(string='Vote Score', default=0)
    closed = fields.Boolean(string='Closed', default=False)
    date_published = fields.Datetime(string='Published Date', default=fields.Datetime.now)