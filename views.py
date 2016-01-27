from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wwwidmer.models import TechnicalSkill, Experience

import random


class Link:
    def __init__(self, name, url, glyph):
        self.name = name
        self.url = url
        self.glyph = glyph


def index(request):
    intro = 'Software developer in New York, NY USA.'
    link_list = links()
    experience = TechnicalSkill.objects.all()
    technicals = Experience.objects.all()
    context = {'intro': intro, 'links': link_list, 'experience': experience, 'technicals':technicals}
    return render_to_response('index.html', context)


def links():
    github = Link('github', 'https://www.github.com/wwwidmer', '/static/GitHub-Mark-32px.png')
    linkedin = Link('linkedin', 'https://linkedin url', '/static/In-2C-34px-TM.png')
    return [github, linkedin]
