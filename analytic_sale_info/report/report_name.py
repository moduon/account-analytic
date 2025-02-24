# Copyright 2025 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import api, models


class Name(models.AbstractModel):
    _name = "report.module.name_report"
    _description = "Report Name"

    @api.multi
    def render_html(self, data=None):
        """Render the report."""
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name("module.name_report")
        docargs = {
            "doc_ids": self._ids,
            "doc_model": report.model,
            "docs": self,
        }
        return report_obj.render("module.name_report", docargs)
