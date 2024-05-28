# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Singer(models.Model):

    _name = 'infomusic.singer'

    name = fields.Char(required=True)
    birthday = fields.Date('Date of birth')

    disk_ids = fields.Many2many('infomusic.disk')
