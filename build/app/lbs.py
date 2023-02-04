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

    from blueprints.user import user_blueprint
    app.register_blueprint(user_blueprint)

    from blueprints.librarian_bp import librarian_blueprint
    app.register_blueprint(librarian_blueprint)

    from blueprints.issued_blueprint import issued_blueprint
    app.register_blueprint(issued_blueprint)

    return app

if __name__ == "__main__":
    # issued1 = Issued('9780002005883', 1, 12)
    # issued1.create_issued()
    # issued2 = Issued('9780006178736', 1, 28)
    # issued2.create_issued()
    # issued3 = Issued('9780006280897', 1, 30)
    # issued3.create_issued()
    # issued4 = Issued('9780006280934', 1, 62)
    # issued4.create_issued()
    # issued5 = Issued('9780006482079', 1, 12)
    # issued5.create_issued()
    # issued6 = Issued('9780006479673', 1, 30)
    # issued6.create_issued()
    app = create_app()
    app.run(host='0.0.0.0', port='5000')
