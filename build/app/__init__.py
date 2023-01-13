#!/usr/bin/python3

#!/usr/bin/env python3

from flask import Flask

def create_app():
    app = Flask(__name__)

    from auth import auth
    app.register_blueprint(auth)

    from main import main
    app.register_blueprint(main)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port='5000')
