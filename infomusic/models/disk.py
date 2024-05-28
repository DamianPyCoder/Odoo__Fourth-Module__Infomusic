# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Disk(models.Model):

    _name = 'infomusic.disk'

    name = fields.Char(string='Title', required=True)
    publish_date = fields.Date('Publishing date')

    song_ids = fields.One2many('infomusic.song', 'disk_id')
    singer_ids = fields.Many2many('infomusic.singer')
