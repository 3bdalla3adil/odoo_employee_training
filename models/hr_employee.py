from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # Link to training records
    training_record_ids = fields.One2many('training.record', 'employee_id', string='Training Records')

    # Link to training plans
    training_plan_ids = fields.One2many('training.plan', 'employee_id', string='Training Plans')

    # Link to skills
    # skill_ids = fields.Many2many('employee.skill','rel_employee_skill','', string='Skills')
