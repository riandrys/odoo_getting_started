from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float("Price", required=True)
    status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)