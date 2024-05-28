# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
import logging

_logger = logging.getLogger(__name__)

class Tour(models.Model):

    _name = 'infomusicplus.tour'

    _sql_constraints = [('check_name','UNIQUE(name)','A tour name name must be unique')]

    name = fields.Char(required=True)

    singer_id = fields.Many2one('infomusic.singer')
    tour_city_ids = fields.One2many('infomusicplus.tour.city','tour_id')

    state = fields.Selection([('new','New'),('confirmed','Confirmed'),('done','Done'),('cancelled','Cancelled')], default='new')

    @api.constrains('tour_city_ids')
    def _check_nbr_of_cities(self):
        for record in self:
            if len(self.tour_city_ids) > 4:
                raise ValidationError('Maximum number of ciies in a tour is 4')

    def tour_done(self):
        for record in self:
            if record.state != 'confirmed':
                raise UserError('Only it is allowed to pass to state Done from state Confirmed')
            else:
                record.state = 'done'
        return True

    def tour_cancel(self):
        for record in self:
            if record.state == 'done':
                raise UserError('It is not allowed to pass from state Done to state Cancelled')
            else:
                record.state = 'cancelled'
        return True

    @api.onchange('tour_city_ids')
    def _onchange_tour_city_confirmed(self):

        if len(self.tour_city_ids) > 0  and (self.state == 'new' or self.state == 'confirmed'):

            # confirmed is True when all the cities are confirmed
            confirmed = True
            for city in self.tour_city_ids:
                if not city.confirmed:
                    confirmed = False

            if self.state == 'new' and confirmed:
                self.state = 'confirmed'

            if self.state == 'confirmed' and not confirmed:
                self.state = 'new'

    def unlink(self):
        for record in self:
            _logger.info('tour unlink state = '+record.state)
            if record.state != 'cancelled' and record.state != 'done':
                raise UserError('Only tours in states Cancelled or Done can be removed')
        return super().unlink()