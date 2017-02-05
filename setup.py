# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(HERE, 'README.rst')) as f:
        return f.read()


def _setup():
    setup(
        name='twapp',
        version='0.0.4',
        description='tornado web app generator',
        long_description=readme(),
        url='https://github.com/liujinliu/twapp',
        author='liujinliu',
        author_email='liujinliu@lbesec.com',
        install_requires=['tornado'],
        packages=find_packages('src'),
        include_package_data=True,
        package_dir={'': 'src'},
        package_data={
            'twapp': [
                'shelves/twapp/Makefile',
                'shelves/twapp/README.md',
                'shelves/twapp/setup.py',
                'shelves/twapp/config/logging.conf',
                'shelves/twapp/src/twapp/__init__.py',
                'shelves/twapp/src/twapp/main.py',
                'shelves/twapp/src/twapp/api/__init__.py',
                'shelves/twapp/src/twapp/api/urls.py',
                'shelves/twapp/src/twapp/api/handlers/__init__.py',
                'shelves/twapp/src/twapp/api/handlers/index.py',
                'shelves/twapp/src/twapp/controllers/__init__.py',
                'shelves/twapp/src/twapp/controllers/api.py',
                'shelves/twapp/src/twapp/controllers/modle/__init__.py',
            ]
        },
        entry_points={
            'console_scripts': [
                'twapp-make=twapp.main:main',
                ]
            },
        classifiers=[
            'Environment :: Console',
            'Topic :: Utilities',
        ],
    )


def main():
    _setup()


if __name__ == '__main__':
    main()
