
from app import create_app


flask_app = create_app()

print("DB URI:", flask_app.config['SQLALCHEMY_DATABASE_URI'])

if __name__ == '__main__':

    
    flask_app.run(debug=True)
    
    