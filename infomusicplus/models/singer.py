# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Singer(models.Model):

    _inherit = 'infomusic.singer'

    _sql_constraints = [('check_name','UNIQUE(name)','A singer name must be unique')]

    photo = fields.Image(max_width=150, max_height=150)
    country_of_birth = fields.Many2one('res.country')

    tour_ids = fields.One2many('infomusicplus.tour','singer_id')

    age = fields.Integer(compute='_compute_age')

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            _logger.info('_compute_age birthday = '+str(record.birthday))
            if record.birthday:
                today = fields.Date.today()
                age = today.year - record.birthday.year
                if today.month < record.birthday.month:
                    age -= 1
                elif today.month == record.birthday.month:
                    if today.day < record.birthday.day:
                        age -= 1
                record.age = age
            else:
                record.age = None 
