# Copyright 2025 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import api, models


class WizardModel(models.TransientModel):
    _name = "module.wizard_model"
    _description = "Wizard Name"

    @api.multi
    def action_accept(self):
        """Do something useful."""
        self.ensure_one()
        self.do_something_useful()
