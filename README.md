# new-flask-app
> Create a new flask application using this simple command

![demo.gif](demo.gif)

## Features

* One blueprint for the index
* One template for the index
* One basic jinja layout with refs to all assets
* Javascript minifier (jsmin)
* Password encryption module using bcrypt
* Configuration file (json)

## Install
> To install it on your system:

    $ python setup.py install

## Usage
> To create a new flask application run:

    $ new-flask-app

> This will create a directory called `app` with the basic
> flask structure:

    └── app
        ├── APP_NAME
        │   ├── __init__.py
        │   ├── app.py
        │   ├── config.py
        │   ├── password.py
        │   ├── static
        │   │   ├── css
        │   │   ├── image
        │   │   └── js
        │   │       ├── app.js
        │   │       └── utils.js
        │   ├── templates
        │   │   ├── index.html
        │   │   └── layout.html
        │   └── views
        │       ├── __init__.py
        │       ├── index.py
        ├── __main__.py
        ├── config.example.json
        ├── config.json
        └── setup.py

## Running your created app
> To run the app you created, go into its directory and execute:

    $ python setup.py install
    $ python __main__.py
