
from odoo import fields, models


class SlotType(models.Model):
    """Details of slot type"""
    _name = 'slot.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'vehicle_type'
    _description = 'Slot Type'

    vehicle_type = fields.Char(string='Name', required=True,
                               tracking=True, help='Name of vehicle')
    code = fields.Char(string='Code', tracking=True,
                       help='Unique identifier for vehicle')
    allowed_park_duration = fields.Float(string='Allowed Parking Time',
                                         help='Time allowed for the vehicle')
