from odoo import models, fields

class IntegratedCalendarEvent(models.Model):
    _inherit = 'calendar.event'

    source_document_number = fields.Char(string='Source Document Number')
    partner_id = fields.Many2one('res.partner', string='Partner')
    execution_time = fields.Float(string='Execution Time')
