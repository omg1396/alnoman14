from odoo import api, fields, models


class ReCompany(models.Model):
    _inherit = 'res.company'
    stamp_pic = fields.Image('Stamp', help='Signature received through the portal.',
                             copy=False, attachment=True, max_width=128, max_height=128)


class ReUsers(models.Model):
    _inherit = 'res.users'
    stamp_pic = fields.Image('Stamp', help='Signature received through the portal.',
                             copy=False, attachment=True, max_width=128, max_height=128)
