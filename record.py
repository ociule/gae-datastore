#!/usr/bin/python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
from google.appengine.ext import db


class Record(db.Model):
  """Record model
  """
  created = db.DateTimeProperty(auto_now_add=True)
  value = db.StringProperty(required=True)
