# Copyright 2025 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    expected_income = fields.Monetary(
        compute="_compute_expected_income",
        store=True,
        help="Time spent multiplied by the sale unit price.",
    )

    def _compute_expected_income(self):
        """Compute the expected income for each analytic line."""
