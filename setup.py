# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def _setup():
    setup(
        name='twapp',
        version='0.0.1',
        description='tornado web app generator',
        url='https://github.com/liujinliu/twapp',
        author='liujinliu',
        author_email='liujinliu@lbesec.com',
        install_requires=['tornado'],
        packages=find_packages('src'),
        include_package_data=True,
        package_dir={'': 'src'},
        package_data={
            'twapp': [
                'shelves/twapp/*',
                'shelves/twapp/config/*',
                'shelves/twapp/src/twapp/*',
                'shelves/twapp/src/twapp/api/*',
                'shelves/twapp/src/twapp/api/handlers/*',
                'shelves/twapp/src/twapp/controllers/*',
                'shelves/twapp/src/twapp/controllers/modle/*',
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
