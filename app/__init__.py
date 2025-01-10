from flask import Flask

# main app
def create_app():
    # starts app
    app = Flask(__name__)

    # Import the blueprint and register it to the app
    from app.routes import main
    app.register_blueprint(main)

    return app
