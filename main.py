import os
import re
import random
import hashlib
import hmac
import logging
import json
#from string import letters
import string

import webapp2
import jinja2

from google.appengine.ext import db

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))



class Mainpage(BaseHandler):
    def get(self):
        self.render('index.html')


app = webapp2.WSGIApplication([('/',Mainpage),
                               ],
                              debug=True)



