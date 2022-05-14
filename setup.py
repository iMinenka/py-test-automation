from setuptools import setup

setup(
    name='pta',
    version='1.0',
    author='igmin',
    packages=['lesson_3'],
    package_data={'Lesson_3': ['Q&A questions']},
    description='Installing package pta with setup.py',
    install_requires=['prettytable']
)
