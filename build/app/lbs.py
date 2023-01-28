#!/usr/bin/python3

from common.base import Base, engine
from common.configs import SECRET_KEY

Base.metadata.create_all(engine)

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    from blueprints.main import main
    app.register_blueprint(main)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port='5000')
