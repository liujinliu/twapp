# -*- coding: utf-8 -*-

import logging.config
from os import makedirs
from os.path import join as path_join,\
                    exists as path_exists
from tornado.options import define, options

define('port', default=8888, type=int, help='app listen port')
define('debug', default=False, help='debug option')
define('base_dir', default='.', help='put the config path here')


def logging_init():
    config_path = path_join(options.base_dir, 'config')
    log_template = path_join(config_path, 'logging.conf')
    if not path_exists(log_template):
        print('No log config found, use default')
        return
    log_path = path_join(options.base_dir, ('%d' % options.port), 'logs')
    log_config_file = path_join(options.base_dir, ('%d' % options.port),
                                'logging.conf')
    if not path_exists(log_path):
        makedirs(log_path)
    with open(log_template, 'r') as f0:
        values = f0.read()
        with open(log_config_file, 'w') as f1:
            f1.write(values.format(log_path=log_path))
    logging.config.fileConfig(log_config_file)


def app_init():
    from api.urls import urls
    from tornado.web import Application
    app = Application(urls, debug=options.debug)
    app.listen(options.port)


def main():
    options.parse_command_line()
    logging_init()
    app_init()
    import tornado.ioloop
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()

if __name__ == '__main__':
    main()
