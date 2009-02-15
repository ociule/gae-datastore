#!/usr/bin/env python

import logging
import wsgiref.handlers

from google.appengine.ext import webapp

from record import Record 
from baseHandler import BaseRequestHandler, _DEBUG
from getHandler import GetHandler
from putHandler import PutHandler


class MainHandler(BaseRequestHandler):

  def get(self):
    logging.error("get")
    self.generate('index.html', template_values={
        'page_title' : "GAE Datastore"
                                                })

_URLS = [('/',              MainHandler),
         ('/get/([^/]+)',   GetHandler),
         ('/put/',          PutHandler),
         ('/put/([^/]+)',   PutHandler)]

def main():
  application = webapp.WSGIApplication(_URLS,
                                       debug=_DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
