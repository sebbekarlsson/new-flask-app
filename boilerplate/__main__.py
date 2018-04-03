import os
from APP_NAME.app import app
import flask_assets


STATIC_DIR = 'APP_NAME/static'


def run():
    env = flask_assets.Environment(app)

    env.load_path = [
        os.path.join(os.path.dirname(__file__), '{STATIC_DIR}/js'.format(
            STATIC_DIR=STATIC_DIR
        ))
    ]

    env.register(
        'js_all',
        flask_assets.Bundle(
            'utils.js',
            'app.js',
            filters=['jsmin'],
            output='js/packed.js'
        )
    )

    app.run(debug=True, threaded=True)


run()
