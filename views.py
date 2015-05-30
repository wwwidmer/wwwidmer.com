from django.shortcuts import render_to_response
from wwwidmer.models import page, blog, portfolio, project, index_image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

# General static information at startup
has_portfolio = True if portfolio.objects.all().count() > 0 else False
has_blog = True if blog.objects.all().count() > 0 else False
menu_list = page.objects.filter(onMenu = True)

def index(request):
    mainPage = page.objects.filter(title="main")
    indexed_image = render_image()
    context = {'menu_list':menu_list, 'has_portfolio_list':has_portfolio, 'has_blog_list':has_blog, 'main':mainPage, 'img':indexed_image}
    return render_to_response('index.html',context)

# Clean up template
def render_portfolios(request):
    port_view = portfolio.objects.all()
    context = {'menu_list':menu_list, 'port_view':port_view, 'has_portfolio_list':has_portfolio, 'has_blog_list':has_blog}
    return render_to_response('page.html',context)

# Clean up template
def render_portfolio_article(request, p_id):
    port_view = portfolio.objects.filter(id = p_id)
    context = {'menu_list':menu_list, 'port':port_view, 'has_portfolio_list':has_portfolio, 'has_blog_list':has_blog}
    return render_to_response('page.html',context)

def render_pages(request, page_slug):
    pages = page.objects.filter(title__icontains=page_slug)
    blogs = blog.objects.all().order_by('-pub_date')
    context = {'menu_list':menu_list, 'pages':pages, 'has_portfolio_list':has_portfolio, 'has_blog_list':has_blog,'full_blog_list':blogs}
    return render_to_response('page.html',context)

# images, sidebar styling in template
def render_blog(request, b_id=0):
    blogs = blog.objects.all().order_by('-pub_date')
    blog_view = Paginator(blogs,3)
    page = request.GET.get('page')
    try:
        blog_list = blog_view.page(page)
    except PageNotAnInteger:
        blog_list = blog_view.page(1)
    except EmptyPage:
        blog_list = blog_view.page(blog_view.num_pages)
    context = {'blog_list':blog_list, 'menu_list':menu_list, 'has_portfolio_list':has_portfolio, 'has_blog_list':has_blog, 'full_blog_list':blogs}
    return render_to_response('blog.html',context)

def render_image():
    range = index_image.objects.all().count()
    rand = random.randrange(0,range)
    img = index_image.objects.all()[rand]
    return img

