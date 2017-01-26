# -*- coding: utf-8 -*-
import os
import re
from tornado.options import define, options
import shutil
import sys
import twapp

define('prefix', default='~/workspace',
       help='generate twapp files at [PREFIX]')
define('app', default='', help='app name')
ORI_PROJECT = 'twapp'


def main():
    options.parse_command_line()
    if not options.app:
        options.print_help()
        sys.exit()

    app_name = options.app
    src_path = os.path.realpath(
                os.path.join(twapp.__path__[0], 'shelves',))
    dst_path = os.path.expanduser(options.prefix)
    shutil.copytree(os.path.join(src_path, ORI_PROJECT),
                    os.path.join(dst_path, app_name))

    rename_dirs = []
    for root, dirs, files in os.walk(os.path.join(dst_path, app_name)):
        for ori_name in dirs:
            if ORI_PROJECT in ori_name:
                dst_name = ori_name.replace(ORI_PROJECT, app_name)
                rename_dirs.append((os.path.join(root, ori_name),
                                    os.path.join(root, dst_name)))

        for name in files:
            if '.pyc' in name:
                os.remove(os.path.realpath(os.path.join(root, name)))
                continue

            if re.match(
                (r'.+([py]|[md]|[sh]|[Makefile]|'
                 '[cfg]|[gitignore])$|')+app_name, name):
                with open(os.path.join(root, name), "r+") as f:
                    d = f.read()
                    d = d.replace(ORI_PROJECT, app_name)
                    d = d.replace(ORI_PROJECT.upper(), app_name.upper())
                    f.truncate(0)
                    f.seek(0, 0)
                    f.write(d)

    for dirs in reversed(rename_dirs):
        ori_name, dst_name = dirs
        os.rename(ori_name, dst_name)
