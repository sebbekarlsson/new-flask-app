from os.path import expanduser
import os
import shutil


HOME = expanduser('~')
CWD = os.getcwd()


def run():
    print('Creating your flask application...')
    shutil.copytree(
        '{}/.new-flask-app/boilerplate'.format(HOME), CWD + '/' + 'app'
    )
    print('The application was created!')
