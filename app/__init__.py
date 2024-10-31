from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuraciones de la aplicación
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'sdfjkl')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar la base de datos y migraciones
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Importar modelos para que Flask-Migrate los detecte
    from .models import Paciente, Atencion
    
    # Importar y registrar las rutas
    from .routes import main
    app.register_blueprint(main)
    
    return app

# Crear la instancia de la aplicación
app = create_app()