from odoo import models, fields # type: ignore

class Answer(models.Model):
    _name = 'stackit.answer'
    _description = 'Answer'

    content = fields.Html(string='Answer')
    question_id = fields.Many2one('stackit.question', string='Question')
    user_id = fields.Many2one('res.users', string='Answered By', default=lambda self: self.env.user)
    vote_count = fields.Integer(string='Votes', default=0)
    is_accepted = fields.Boolean(string='Accepted Answer', default=False)