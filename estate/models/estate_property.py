from datetime import datetime, timedelta
from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.estate_property'

    active = fields.Boolean(string='Active', default=True),
    name = fields.Char(string='Property Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(
        string='Date Availability', copy=False, default=lambda self: self.get_default_availability_date())
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(
        string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default='2')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ],
        string='Garden Orientation'
    )
    status = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled')
        ],
        string='Status',
        default='new',
        required=True,
        copy=False,
    )

    def get_default_availability_date(self):
        """Get the default availability date as 3 months from today."""
        now = datetime.now()
        then = now + timedelta(days=90)
        return then
