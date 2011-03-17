from django.shortcuts import *
from django.template import RequestContext
from django.core.paginator import Paginator
from exo.util import paginate

from models import *

def index(request, template=None):
    '''Show latest five articles'''

    articles = Article.online.all()[:5]

    c = RequestContext(request, {
        'article_list':articles
    })
    return render_to_response(template or 'blog/index.html',c)


def articles(request, year=None, month=None, day=None, template=None):
    '''List articles. Filter by year, month, day.'''

    articles = Article.online.all()
    years = Article.online.dates('date_published','year')
    months, days = None, None
    if year:
        articles = articles.filter(date_published__year=year)
        months = articles.dates('date_published','month')
        if month:
            articles = articles.filter(date_published__month=month)
            days = articles.dates('date_published','day')
            if day:
                articles = articles.filter(date_published__day=day)

    c = RequestContext(request, {
        'article_list':paginate(request, articles, 20),
        'year':year,
        'month':month,
        'day':day,
        'years':years,
        'months':months,
        'days':days,
    })
    return render_to_response(template or 'exo/blog/article_list.html',c)




def article(request, year=None, month=None, day=None, slug=None, template=None):
    '''Article detail'''
    article = get_object_or_404(Article.online, date_published__year=year, date_published__month=month, date_published__day=day, slug=slug)
    c = RequestContext(request, {
        'object':article,
        'year':year,
        'month':month,
        'day':day,
    })
    return render_to_response(template or 'exo/blog/article_detail.html', c)

