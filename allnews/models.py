from sqlalchemy import (
    Column,
    String,
    Index,
    Integer,
    Text,
    DateTime,
    or_,
    and_
    )
import datetime
from sqlalchemy.ext.declarative import declarative_base
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.sql.expression import func
from allnews.utility_script import pager
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class News(Base):
    """Sqlalchemy deals model"""
    __tablename__ = "news"

    id =            Column(Integer, primary_key=True)
    title =         Column(String, nullable=False, unique=True)
    description =   Column(String, nullable=False, unique=True)
    detail_url =    Column( String, nullable=False, unique=True)
    image_url =     Column( String, nullable=True, unique=True)
    category =      Column( String, nullable=False)
    source =        Column( String, nullable=False)
    created =       Column( DateTime, default=datetime.date.today())
    count =         Column(Integer, default=0)
    language =      Column(Text, nullable=True)
    paper_name =    Column(Text, nullable=False)


    @classmethod
    def all(cls, category):
        date_today = datetime.date.today()
        queryset = DBSession.query(News).filter(and_(News.category == category), (News.created == date_today)).order_by(News.title).limit(20)
        if queryset.count() == 0:
            previous_day = date_today - datetime.timedelta(days=1)
            queryset = DBSession.query(News).filter(and_(News.category == category), (News.created == previous_day)).order_by(News.title).limit(20)
        return queryset

    @classmethod
    def get_paginator(cls, category):
        date_today = datetime.date.today()
        previous_day = date_today - datetime.timedelta(days=1)
        total_row = DBSession.query(News).filter(and_(News.category == category), (News.created == date_today)).count()
        if total_row == 0:
            total_row = DBSession.query(News).filter(and_(News.category == category), (News.created == previous_day)).count()
        item_per_page = 20
        return pager(total_row, item_per_page)

    @classmethod
    def newspaper_sort(cls, category, paper_name):
        date_today = datetime.date.today()
        queryset = DBSession.query(News).filter(and_(News.category == category), (News.paper_name == paper_name), (News.created == date_today))
        if queryset.count() == 0:
            previous_day = date_today - datetime.timedelta(days=1)
            queryset = DBSession.query(News).filter(and_(News.category == category), (News.paper_name == paper_name), (News.created == previous_day))
        return queryset

    @classmethod
    def by_id(cls, id):
        detail_data = DBSession.query(News).filter(News.id == id).first()
        increment = detail_data.count + 1
        DBSession.query(News).filter_by(id=id).update({"count": increment})
        return detail_data

    @classmethod
    def search(cls, text):
        return DBSession.query(News).filter(or_(News.title.ilike("%"+text+"%"), News.description.ilike("%"+text +"%"))).order_by(News.title).limit(20)

    @classmethod
    def popular(cls):
        date_today = datetime.date.today()
        queryset = DBSession.query(News).filter(News.created == date_today).order_by(News.count).limit(20)
        if queryset.count() == 0:
            previous_day = date_today - datetime.timedelta(days=1)
            queryset = DBSession.query(News).filter(News.created == previous_day).order_by(News.count).limit(20)
        return queryset

    @classmethod
    def popularity_paginator(cls):
        date_today = datetime.date.today()
        previous_day = date_today - datetime.timedelta(days=1)
        total_row = DBSession.query(News).filter(News.created == date_today).count()
        if total_row == 0:
            total_row = DBSession.query(News).filter(News.created == previous_day).count()
        item_per_page = 20
        return pager(total_row, item_per_page)








# import datetime
#
# date_today = datetime.date.today()
#
# previos_day= date_today - datetime.timedelta(days=1)


# query.filter(Model.column.ilike("%ganye%"))

