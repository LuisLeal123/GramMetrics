from flask import Flask

# main app
def create_app():
    # starts app
    app = Flask(__name__)

    # Import and register routes to the application 
    from app.routes import main
    app.register_blueprint(main)

    return app
