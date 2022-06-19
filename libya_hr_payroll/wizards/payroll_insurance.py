# -*- coding: utf-8 -*-

from odoo import fields, models
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
# import datetime


class CreateWizard(models.TransientModel):
    _name = 'payroll.insurance'
    _description = 'Payroll Insurance'


    date_from = fields.Date("Date From",default=lambda self: fields.Date.to_string(date.today().replace(day=1)),required=True)
    date_to = fields.Date("Date To",default=lambda self: fields.Date.to_string((datetime.now() + relativedelta(months=+1, day=1, days=-1)).date()),required=True)

    def _get_report_pdf(self):
        exist_payslip = self.env['hr.payslip'].search([('date_from','<=',self.date_from),('date_to','>=',self.date_to)])
        date_month = datetime.strptime(
            self.date_from.strftime('%Y-%m-%d'), '%Y-%m-%d')
        payslip_ids = []
        for payslip in exist_payslip:
            payslip_ids.append({
                'employee_name': payslip.employee_id.name,
                'basic':payslip.line_ids.filtered(lambda line: line.code == 'TOBASIC').total,
                'employee_insurance':payslip.line_ids.filtered(lambda line: line.code == 'TOBASIC').total * 0.0375,
                'company_insurance':payslip.line_ids.filtered(lambda line: line.code == 'TOBASIC').total * 0.105,

            })


        return {
            'payslip_ids': payslip_ids,
            'date_month':date_month.month,
            'date_year' : date_month.year
        }

    def generate_payroll_insurance(self):
        data = self._get_report_pdf()
        return self.env.ref('libya_hr_payroll.report_payroll_libya_insurance_pdf').report_action([],data=data)







