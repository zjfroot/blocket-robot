#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import logging
import urllib2
import sys

from google.appengine.ext import webapp
from google.appengine.api import mail

sys.path.append('.')

from BeautifulSoup import BeautifulSoup

class BlocketHandler(webapp.RequestHandler):
    def get(self):
	logging.info('Blocket Robot: searching blocket with keyword pentax')

        #url = "http://www.blocket.se/stockholm?q=pentax"
    	url = "http://www.blocket.se/stockholm?q=pentax&cg=0&w=3&st=s&st=u&st=b&ca=11&l=0&md=th"

        response = urllib2.urlopen(url)
        result = response.read()
        soup = BeautifulSoup(result)
        simplified_result = soup.find("div", {"class":"list_mode_thumb"})

        self.send_mail(simplified_result)


        #self.response.out.write(result)

    def send_mail(self, result):
        message = mail.EmailMessage(sender="New Blocket Robot <zjfroot@gmail.com>",
                            subject="Result of searching pentax on blocket")

        message.to = "Master Jifeng <zjfroot@gmail.com>"
        message.html = result
        
        logging.info('sending the mail')
        message.send()
        
