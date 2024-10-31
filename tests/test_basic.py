# tests/test_basic.py

import pytest
from app import create_app, db
from app.models import Paciente, Atencion, User

@pytest.fixture
def app():
    app = create_app('config.TestingConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_lista_atenciones(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Lista de Atenciones' in response.data

def test_crear_atencion(client, app):
    response = client.post('/crear_atencion', data={'run': '12345678-9'}, follow_redirects=True)
    assert response.status_code == 200
    assert 'Atención creada exitosamente.' in response.data
    with app.app_context():
        paciente = Paciente.query.filter_by(run='12345678-9').first()
        assert paciente is not None
        atencion = Atencion.query.filter_by(paciente_id=paciente.id).first()
        assert atencion is not None

def test_registro_usuario(client, app):
    response = client.post('/auth/register', data={
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert 'Registro exitoso. Puedes iniciar sesión ahora.' in response.data
    with app.app_context():
        user = User.query.filter_by(email='test@example.com').first()
        assert user is not None

def test_login_usuario(client, app):
    with app.app_context():
        user = User(email='login@example.com')
        user.set_password('securepassword')
        db.session.add(user)
        db.session.commit()
    response = client.post('/auth/login', data={
        'email': 'login@example.com',
        'password': 'securepassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert 'Inicio de sesión exitoso.' in response.data
