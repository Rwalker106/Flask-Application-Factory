from flask import Flask
from flask_bootstrap import Bootstrap5
from app.extension import db  # ← single source of truth
from os import getenv
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

bootstrap = Bootstrap5()

# __init__.py
def create_app():
    flask_app = Flask(__name__)
    
    default_db = 'sqlite:///' + os.path.join(flask_app.instance_path, 'cafes.db')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI', default_db)
    
    # Make sure the instance folder exists
    os.makedirs(flask_app.instance_path, exist_ok=True)
    
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SECRET_KEY'] = getenv('SECRET_KEY', 'default_secret_key')

    db.init_app(flask_app) # <- initialize SQLAlchemy with the Flask app
    bootstrap.init_app(flask_app)

    from app.routes import bp  # load routes AFTER app is created
    flask_app.register_blueprint(bp)
    
    @flask_app.context_processor
    def inject_current_year():
        from datetime import datetime
        return {'current_year': datetime.now().year}
    
    with flask_app.app_context():
        from app import models # Import models to register them with SQLAlchemy
        db.create_all()  # Create database tables if they don't exist   

    return flask_app
