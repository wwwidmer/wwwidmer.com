from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import os

from wwwidmer.models import TechnicalSkill, Experience

import random


class Link:
    def __init__(self, name, url, glyph):
        self.name = name
        self.url = url
        self.glyph = glyph


def index(request):
    intro = read_intro()
    link_list = links()
    experience = Experience.objects.all().order_by('start_date')
    technicals = TechnicalSkill.objects.all().order_by('-stars')
    context = {'intro': intro, 'links': link_list, 'experience': experience, 'technicals':technicals}
    return render_to_response('index.html', context)


def links():
    # I don't mind hardcoding this stuff in. Alternatively this would be another table/model.
    github = Link('github', 'https://www.github.com/wwwidmer', '/static/GitHub-Mark-32px.png')
    linkedin = Link('linkedin', 'https://www.linkedin.com/in/williamjohnwidmer', '/static/In-2C-34px-TM.png')
    return [github, linkedin]


def read_intro():
    intro = os.path.join(os.path.dirname(__file__), 'intro.txt')
    with open(intro, 'rw+') as intro_text:
        intro_text.seek(0)
        text = intro_text.readlines()  # This will be a list so we can format it later.
        return text
