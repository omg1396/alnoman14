from odoo import fields, models, api


class CustomerReview(models.Model):
    _name = 'customer.review'
    _description = 'Customer Review'

    name = fields.Char("Name")
    job = fields.Char("Job")
    review = fields.Text("Review")
