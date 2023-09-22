
from odoo import fields, models


class VehicleDetails(models.Model):
    """Details of a Vehicle"""
    _name = 'vehicle.details'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'vehicle_id'
    _description = 'Vehicle Details'

    vehicle_id = fields.Many2one('fleet.vehicle', string='vehicle',
                                 tracking=True, required=True,
                                 help='Name of vehicle')
    partner_id = fields.Many2one('res.partner', string='Owner',
                                 tracking=True, help=' Name of Partner')
    number_plate = fields.Char(string='Number Plate', tracking=True,
                               required=True, help='Number for the vehicle')
    ownership_type = fields.Selection([('outsider', 'Outsider'), ('member',
                                                                  'Member')],
                                      string='Ownership type', tracking=True,
                                      required=True, help='Type of the owner '
                                                          'of vehicle')
