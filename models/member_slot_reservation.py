
from odoo import fields, models


class MemberSlotReservation(models.Model):
    """Details for MemberSlotReservation"""
    _name = 'member.slot.reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'slot_id'
    _description = 'Member Slot Reservation'

    slot_id = fields.Many2one('slot.details', string='Slot', tracking=True,
                              required=True,
                              help='Field for the ID of the slot')
    partner_id = fields.Many2one('res.partner', string='Member',
                                 tracking=True, required=True,
                                 help='Field for Reserved Member')
    start_date = fields.Date(string='Start Date', tracking=True,
                             required=True,
                             help='Field for adding the start date')
    end_date = fields.Date(string='End Date', tracking=True, required=True,
                           help='Field for adding end date')
