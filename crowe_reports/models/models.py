from odoo import models, fields, api


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def get_header_month(self, date):
        return date.strftime('%B, %Y')

    def get_basic(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'BASIC':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_house_rent(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'HR':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_utilities_allowance(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'UY':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_recognition_bonus(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'RB':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_leave_encashment(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'LE':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_phone_allowance(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'PA':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_internet_allowance(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'IA':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_car_allowance(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'CA':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_driver_allowance(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'DA':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_lfa(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'Lfa':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_other_allowance(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'OA':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_performance_bonus(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'PB':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_relocate_allowance(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'REA':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_arrears(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'AR':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_pf(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'PF':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_income_tax(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'Tax':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_professional_tax(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'Pt':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_eobi(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'EOB':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_pa_arrears(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'Pa':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_pf_loan(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'PL':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_membership_rec(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'MR':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'

    def get_salary_deduction(self):
        result = '-'
        for line in self.line_ids:
            if line.salary_rule_id.code == 'Sd':
                if line.total != 0:
                    result = round(line.total)
        return result or '-'
