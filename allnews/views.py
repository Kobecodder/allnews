from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    News,
    )


# @view_config(route_name='home', renderer='templates/newslist.jinja2')
# def my_view(request):
#     # one = DBSession.query(MyModel).filter(MyModel.name == 'one').limit()
#     newsset = News.all('home')
#     pager=News.get_paginator('home')
#     print (pager)
#
#     return {'newsset': newsset}


class BasicViews:
    def __init__(self, request):
        self.request = request
        self.title = 'Welcome'

    @view_config(route_name='home', renderer='templates/newslist.jinja2')
    def my_view(self):
        newsset = News.all('home')
        pager=News.get_paginator('home')
        print (pager)
        # if self.request.params:
        if self.request.params.get('next_page', ''):
            next = self.request.params['next_page']
            page_number = int(next)
            newsset = News.all('home').offset(pager[int(next)])


        return {'newsset': newsset}





