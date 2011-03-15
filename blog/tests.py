from django.test import TestCase
import datetime

from models import *
from django.contrib.sites.models import Site


ARTICLE_DICT = {
    'title': 'Test Article',
    'slug': 'test-article',
    'content': 'Test Article Content.',
    'user_id': 1,
    'date_published':datetime.datetime(2000,01,01,01,01,01),
}


class BlogTest(TestCase):
    fixtures = ['test']
    urls = 'blog.urls'

    def setUp(self):
        '''Create test Article'''
        article = Article(**ARTICLE_DICT)
        article.save()
        article.sites.add(Site.objects.get_current())


    def test_article(self):
        '''Get an Article'''
        response = self.client.get('/2000/01/01/test-article')
        self.assertEquals(response.status_code,200)
        self.assertEquals(response.context['object'].title, ARTICLE_DICT['title'])

    def test_articles(self):
        '''Get Article list'''
        response = self.client.get('/')
        self.assertEquals(response.status_code,200)
        self.assertEquals(response.context['object_list'][0].title, ARTICLE_DICT['title'])
        response = self.client.get('/2000/')
        self.assertEquals(response.status_code,200)
        self.assertEquals(response.context['object_list'][0].title, ARTICLE_DICT['title'])
        response = self.client.get('/2000/01/')
        self.assertEquals(response.status_code,200)
        self.assertEquals(response.context['object_list'][0].title, ARTICLE_DICT['title'])
        response = self.client.get('/2000/01/01/')
        self.assertEquals(response.status_code,200)
        self.assertEquals(response.context['object_list'][0].title, ARTICLE_DICT['title'])


