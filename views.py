from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wwidmer.models import page, blog, portfolio, project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
	menu_list = page.objects.filter(onMenu = True)
	context = {'menu_list':menu_list}
	return render_to_response('index.html',context)

def portfolios(request):
	menu_list = page.objects.filter(onMenu = True)
	port_view = portfolio.objects.all()
	context = {'menu_list':menu_list, 'port_view':port_view}
	return render_to_response('page.html',context)

def portfolio_article(request, p_id):
	menu_list = page.objects.filter(onMenu = True)
	port_view = portfolio.objects.filter(id = p_id)
	context = {'menu_list':menu_list, 'port':port_view}
	return render_to_response('page.html',context)

def pages(request, page_slug):
	menu_list = page.objects.filter(onMenu = True)
	pages = page.objects.filter(title__icontains=page_slug)
	context = {'menu_list':menu_list, 'pages':pages}
	return render_to_response('page.html',context)
