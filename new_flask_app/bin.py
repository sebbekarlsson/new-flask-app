from os.path import expanduser
import os
import shutil


HOME = expanduser('~')
CWD = os.getcwd()


def run():
    shutil.copytree(
        '{}/.new-flask-app/boilerplate'.format(HOME), CWD + '/' + 'app'
    )
