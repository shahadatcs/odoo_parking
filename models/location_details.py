from odoo import fields, models


class LocationDetails(models.Model):
    """Details for a location"""
    _name = 'location.details'
    _description = 'Location Details'

    name = fields.Char(string='Locations', required=True,
                       help='Name of the location')
