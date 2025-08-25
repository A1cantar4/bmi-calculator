import os
from flask import Flask, request
from flask_babel import Babel, get_locale
from dotenv import load_dotenv

babel = Babel()
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    app.config['BABEL_DEFAULT_LOCALE'] = os.getenv("BABEL_DEFAULT_LOCALE")
    app.config['BABEL_SUPPORTED_LOCALES'] = os.getenv("BABEL_SUPPORTED_LOCALES").split(",")

    babel.init_app(app, locale_selector=get_locale_selector)

    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)

    from .routes import bp
    app.register_blueprint(bp)

    return app

def get_locale_selector():
    return request.args.get("lang") or os.getenv("BABEL_DEFAULT_LOCALE")