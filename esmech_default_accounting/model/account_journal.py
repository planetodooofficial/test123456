from odoo import api, fields, models, _

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    code = fields.Char(string='Short Code', size=50, required=True,
                       help="Shorter name used for display. The journal entries of this journal will also be named using this prefix by default.")