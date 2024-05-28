# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Song(models.Model):

    _name = 'infomusic.song'

    name = fields.Char(string='Title', required=True)
    disk_id = fields.Many2one('infomusic.disk')
    order = fields.Integer()
    duration = fields.Float()
