from odoo import api, fields, models, _


class TdsRateRule(models.Model):
    _name = 'tds.rates.rule'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name =fields.Char('Section',required=True,)
    nature_of_payment =fields.Text('Nature of Payment')
    limit_dedu_tax =fields.Char('Threshold Limit for deduction tax')
    individual =fields.Char('Individual')
    company =fields.Char('Company')
    other =fields.Char('Other')
    invalid_pan =fields.Char('No Pan or Invalid PAN')
    summary =fields.Text('Summary')
    tax_id = fields.Many2one('account.tax')