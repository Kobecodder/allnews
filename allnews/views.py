from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    News,
    )


class BasicViews:
    def __init__(self, request):
        self.request = request
        self.title = 'Welcome'
        self.category = 'home'

    @view_config(route_name='home', renderer='templates/newslist.jinja2')
    def home_view(self):
        newsset = News.all('home')
        pager = News.get_paginator('home')
        if self.request.params.get('next_page', ''):
            next = self.request.params['next_page']
            newsset = News.all('home').offset(pager[int(next)])
        return {'newsset': newsset, 'pager': pager}

    @view_config(route_name='news_category', renderer='templates/newslist.jinja2')
    def category_view(self):
        category = self.request.matchdict['category']
        self.category = category
        newsset = News.all(category)
        pager = News.get_paginator(category)
        if self.request.params.get('next_page', ''):
            next = self.request.params['next_page']
            newsset = News.all(category).offset(pager[int(next)])
        if self.request.params.get('search', ''):
            search_param = self.request.params['search']
            newsset=News.search(search_param)
            pager={}
        return {'newsset': newsset, 'pager': pager}

    @view_config(route_name='popular', renderer='templates/newslist.jinja2')
    def popular_view(self):
        newsset = News.popular()
        pager ={}
        if self.request.params.get('next_page', ''):
            next = self.request.params['next_page']
            newsset = News.popular().offset(pager[int(next)])
        return {'newsset': newsset, 'pager': pager}

    @view_config(route_name='newspaper_sort', renderer='templates/newslist.jinja2')
    def newspaper_sort_view(self):
        category = self.request.matchdict['category']
        newspaper = self.request.matchdict['newspaper']
        self.category = category
        newsset = News.newspaper_sort(category,newspaper)
        pager = {}
        return {'newsset': newsset, 'pager': pager}


