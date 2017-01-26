# -*- coding: utf-8 -*-

import logging

LOG = logging.getLogger('app')


class TWAppPing(object):

    def hi(self):
        return 'twapp works well.'

TWAppPing = TWAppPing()
