from __future__ import unicode_literals

from django.db import models


class TechnicalSkill(models.Model):
    name = ''
    years = 0
    stars = 5


class Experience(models.Model):
    title = ''
    company = ''
    description = ''
    achievements = ''
