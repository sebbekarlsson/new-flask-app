from setuptools import setup


setup(
    name='APP_NAME',
    version='1.0',
    install_requires=[
        'flask_assets',
        'jsmin',
        'flask'
    ],
    packages=[
        'APP_NAME'
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
