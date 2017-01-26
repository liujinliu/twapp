# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def _setup():
    setup(
        name='twapp',
        version='0.0.1',
        description='tornado web app',
        url='',
        install_requires=['tornado'],
        packages=find_packages('src'),
        package_dir={'': 'src'},
        entry_points={
            'console_scripts': [
                'twapp-start=twapp.main:main',
                ]
            },
        classifiers=[
            'Development Status :: 4 - Beta Development Status',
            'Environment :: Console',
            'Topic :: Utilities',
        ],
    )


def main():
    _setup()


if __name__ == '__main__':
    main()
