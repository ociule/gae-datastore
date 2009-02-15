#!/usr/bin/env python

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

# Set the debug level
_DEBUG = True

class BaseRequestHandler(webapp.RequestHandler):
  """Base request handler extends webapp.Request handler

     It defines the generate method, which renders a Django template
     in response to a web request
  """

  def generate(self, template_name, template_values={}):
    """Generate takes renders and HTML template along with values
       passed to that template

       Args:
         template_name: A string that represents the name of the HTML template
         template_values: A dictionary that associates objects with a string
           assigned to that object to call in the HTML template.  The defualt
           is an empty dictionary.
    """

    # Construct the path to the template
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, 'templates', template_name)

    # Respond to the request by rendering the template
    self.response.out.write(template.render(path, template_values, debug=_DEBUG))
