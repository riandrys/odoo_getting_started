from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tags'
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique."),
    ]

    name = fields.Char("Name", required=True)
