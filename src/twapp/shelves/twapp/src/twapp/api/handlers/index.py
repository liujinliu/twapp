# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from twapp.controllers.api import TWAppPing


class Ping(RequestHandler):
    def get(self):
        self.write(TWAppPing.hi())
