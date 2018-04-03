from setuptools import setup
from setuptools.command.install import install
import subprocess
from os.path import expanduser


HOME = expanduser('~')


class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        subprocess.Popen(
            'mkdir {}/.new-flask-app'.format(HOME),
            shell=True
        )

        subprocess.Popen(
            'cp -r boilerplate {}/.new-flask-app/.'.format(HOME),
            shell=True
        )
        install.run(self)


setup(
    name='new-flask-app',
    version='1.0',
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomInstallCommand
    },
    install_requires=[
    ],
    packages=[
        'new_flask_app'
    ],
    entry_points={
        'console_scripts': [
            'new-flask-app = new_flask_app.bin:run'
        ]
    }
)
