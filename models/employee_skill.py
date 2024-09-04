# -*- coding: utf-8 -*-
from odoo import models, fields, api

  
  #ToDo:Allow managers to assess and assign skills to employees.
  #ToDo:linked Skills to training courses


class EmployeeSkill(models.Model):
    _name = 'employee.skill'
    _inherit = 'hr.employee.skill'
    _description = 'Employee Skill'

    # name = fields.Char(string='Skill', required=True)
    description = fields.Text(string='Skill Description')

    course_ids = fields.Many2many('training.course', string='Related Courses')
