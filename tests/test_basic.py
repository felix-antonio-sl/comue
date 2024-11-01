# tests/test_basic.py

import pytest
from app import create_app, db
from app.models import Paciente, Atencion, User
from config import TestingConfig


@pytest.fixture
def app_fixture():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app_fixture):
    return app_fixture.test_client()


@pytest.fixture
def runner(app_fixture):
    return app_fixture.test_cli_runner()


@pytest.fixture
def test_user_email(app_fixture):
    with app_fixture.app_context():
        user = User(email="testuser@example.com")
        user.set_password("testpassword")
        db.session.add(user)
        db.session.commit()
        return user.email


@pytest.fixture
def login_client(client, app_fixture, test_user_email):
    with app_fixture.app_context():
        response = client.post(
            "/auth/login",
            data={"email": test_user_email, "password": "testpassword"},
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert "Inicio de sesión exitoso." in response.get_data(as_text=True)
    return client


def test_lista_atenciones(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Lista de Atenciones" in response.get_data(as_text=True)


def test_crear_atencion(login_client, app_fixture):
    response = login_client.post(
        "/crear_atencion", data={"run": "12345678-9"}, follow_redirects=True
    )
    assert response.status_code == 200
    assert "Atención creada exitosamente." in response.get_data(as_text=True)
    with app_fixture.app_context():
        paciente = db.session.query(Paciente).filter_by(run="12345678-9").first()
        assert paciente is not None
        atencion = db.session.query(Atencion).filter_by(paciente_id=paciente.id).first()
        assert atencion is not None


def test_registro_usuario(client, app_fixture):
    response = client.post(
        "/auth/register",
        data={
            "email": "newuser@example.com",
            "password": "newpassword123",
            "confirm_password": "newpassword123",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Registro exitoso. Puedes iniciar sesión ahora." in response.get_data(
        as_text=True
    )
    with app_fixture.app_context():
        user = db.session.query(User).filter_by(email="newuser@example.com").first()
        assert user is not None


def test_login_usuario(client, app_fixture):
    # Crear el usuario para login
    with app_fixture.app_context():
        user = User(email="login@example.com")
        user.set_password("securepassword")
        db.session.add(user)
        db.session.commit()

    # Iniciar sesión
    response = client.post(
        "/auth/login",
        data={"email": "login@example.com", "password": "securepassword"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Inicio de sesión exitoso." in response.get_data(as_text=True)
