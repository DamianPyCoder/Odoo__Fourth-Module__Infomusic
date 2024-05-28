# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Disk(models.Model):

    _inherit = 'infomusic.disk'

    _sql_constraints = [('check_name','UNIQUE(name)','A disk name name must be unique')]

    cover = fields.Image(max_width=150, max_height=150)
    genre = fields.Selection([('rock', 'Rock'),
                              ('pop', 'Pop'),
                              ('pop-rock', 'Pop-Rock'),
                              ('heavy', 'Heavy')
                             ], default='rock')
    nbr_of_songs = fields.Integer(compute='_compute_nbr_of_songs')

    @api.depends('song_ids')
    def _compute_nbr_of_songs(self):
        for record in self:
            self.nbr_of_songs = len(self.song_ids)