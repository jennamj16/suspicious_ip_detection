from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='app/templates')

    # Import blueprints here (AFTER creating the app to avoid circular import)
    from app.main import main_bp  
    app.register_blueprint(main_bp)

    return app
