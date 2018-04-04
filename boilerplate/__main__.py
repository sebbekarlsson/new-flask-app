import os
from APP_NAME.app import app
from APP_NAME.config import config
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

    app.run(
        debug=config['debug'] if 'debug' in config else False,
        threaded=config['threaded'] if 'threaded' in config else False
    )


if __name__ == '__main__':
    run()
