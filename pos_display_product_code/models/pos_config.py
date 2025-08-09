from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    display_default_code = fields.Boolean(default=False)
