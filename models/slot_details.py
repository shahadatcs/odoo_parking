
from odoo import fields, models


class SlotDetails(models.Model):
    """Details for Slot"""
    _name = 'slot.details'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Details about slot'

    code = fields.Char(string='Code', tracking=True, required=True,
                       help='Unique identifier for slot')
    name = fields.Char(string='Name', required=True,
                       help='Name of the slot')
    slot_type_id = fields.Many2one('slot.type', string='Slot Type',
                                   tracking=True, required=True,
                                   help='Type of the slot')
