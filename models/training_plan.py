# -*- coding: utf-8 -*-
from odoo import models, fields, api

  #===========================================================================================================
  #==== PIPELINE ============ EMPLOYEE INFO ==> TRAINING COURSE ==> TRAINING PLAN ============================
  #===========================================================================================================

  #ToDo:


class TrainingPlan(models.Model):
    _name = 'training.plan'
    _description = 'Training Plan'
    _rec_name = 'name'

    name = fields.Char(string='Plan Name', required=True, default=lambda self: self.env['ir.sequence'].next_by_code('training.plan'))
    employee_id = fields.Many2one('hr.employee', string='Employee')
    role_id = fields.Many2one('hr.job', string='Role')
    course_ids = fields.Many2many('training.course', string='Courses')
    due_date = fields.Date(string='Due Date')
    progress = fields.Float(string='Progress', compute='_compute_progress')

    @api.depends('course_ids')
    def _compute_progress(self):
        for plan in self:
            completed_courses = len(plan.course_ids.filtered(lambda c: c in plan.employee_id.training_record_ids.mapped('course_id')))
            total_courses = len(plan.course_ids)
            plan.progress = (completed_courses / total_courses) * 100 if total_courses > 0 else 0
