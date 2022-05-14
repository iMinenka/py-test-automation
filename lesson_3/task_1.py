"""
setup.py
Для своего проекта с домашними заданиями необходимо написать setup.py файл, который позволит устанавливать ваш проект через pip install.
"""

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


"""
Steps:
py.exe .\setup.py sdist --> dist\pta-1.0.tar.gz and pta.egg-info folder
pip install .           --> install project in build\lib\pta directory
pip uninstall pta       --> uninstall package from python site-packages
"""