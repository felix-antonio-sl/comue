from flask import Flask
from models import db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuraciones de la aplicación
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos y migraciones
    db.init_app(app)
    migrate = Migrate(app, db)

    # Importar rutas
    with app.app_context():
        import routes

    return app

app = create_app()
