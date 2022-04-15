from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    hsn_code = fields.Char(string="HSN Code")
