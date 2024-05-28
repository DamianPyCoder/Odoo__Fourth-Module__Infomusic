# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TourCity(models.Model):

    _name = 'infomusicplus.tour.city'

    name = fields.Char(string='City', required=True) # city name
    country_id = fields.Many2one('res.country',required=True)
    date = fields.Date()

    tour_id = fields.Many2one('infomusicplus.tour')

    confirmed = fields.Boolean(compute='_compute_confirmed')

    @api.depends('date')
    def _compute_confirmed(self):
        for record in self:
            if record.date:
                record.confirmed = True
            else:
                record.confirmed = False
