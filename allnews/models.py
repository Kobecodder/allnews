from sqlalchemy import (
    Column,
    String,
    Index,
    Integer,
    Text,
    DateTime,
    )
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from allnews.utility_script import pager
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


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
    created =       Column( DateTime, default=datetime.datetime.now())
    count =         Column(Integer, nullable=True)
    # language =      Column(Text, nullable=True)


    @classmethod
    def all(cls, category):
        return DBSession.query(News).order_by(News.title).limit(20)

    @classmethod
    def by_id(cls, id):
        return DBSession.query(News).filter(News.id == id).first()

    @classmethod
    def get_paginator(cls, category):
        total_row = DBSession.query(News).filter(News.category == category).count()
        item_per_page = 20
        return pager(total_row, item_per_page)



# query.filter(Model.column.ilike("%ganye%"))

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(Unicode(255), unique=True, nullable=False)
#     password = Column(Unicode(255), nullable=False)
#     last_logged = Column(DateTime, default=datetime.datetime.utcnow)
#
#     @classmethod
#     def by_name(cls, name):
#         return DBSession.query(User).filter(User.name == name).first()
#
#     def verify_password(self, password):
#         return self.password == password

# class Entry(Base):
#     __tablename__ = 'entries'
#     id = Column(Integer, primary_key=True)
#     title = Column(Unicode(255), unique=True, nullable=False)
#     body = Column(UnicodeText, default=u'')
#     created = Column(DateTime, default=datetime.datetime.utcnow)
#     edited = Column(DateTime, default=datetime.datetime.utcnow)
#
    # @classmethod
    # def all(cls):
    #     return DBSession.query(Entry).order_by(sa.desc(Entry.created))
    #
    # @classmethod
    # def by_id(cls, id):
    #     return DBSession.query(Entry).filter(Entry.id == id).first()

#     @property
#     def slug(self):
#         return urlify(self.title)
#
#     @property
#     def created_in_words(self):
#         return time_ago_in_words(self.created)
#
    # @classmethod
    # def get_paginator(cls, request, page=1):
    #     page_url = PageURL_WebOb(request)
    #     return Page(Entry.all(), page, url=page_url, items_per_page=5)
