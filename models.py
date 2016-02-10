from __future__ import unicode_literals

from django.db import models


class TechnicalSkill(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    stars = models.DecimalField(max_digits=2, decimal_places=1)


class Experience(models.Model):
    company = models.CharField(max_length=100, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100) 
    achievements = ''
