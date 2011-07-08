#!/usr/bin/env python
#
# Copyright 2011 Jifeng Zhang <zjfroot@gmail.com>.
#
#
import os
import sys
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

#sys.path.append('modules')

from blocket import BlocketHandler

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("hello there.")
        
def main():

    blocket_handler = BlocketHandler()
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/blocket', BlocketHandler)
                                          ],
                                          debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
