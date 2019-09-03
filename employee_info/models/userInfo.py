from odoo import models, fields


class UserInfo(models.Model):
    _inherit = 'hr.employee'

    id_card = fields.Char()
    driving_license = fields.Selection([
        ('none', 'None'),
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], default='none'
    )
