from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view(name='static', path='allnews:static')
    config.add_route('home', '/')
    config.add_route('policy', '/disclaimer')
    config.add_route('url_redirect', '/news/{id}/{tittle}')
    config.add_route('popular', '/news/popular')
    config.add_route('news_category', '/category/{category}')
    config.add_route('newspaper_sort', '/category/{category}/{newspaper}')
    config.scan()
    return config.make_wsgi_app()
