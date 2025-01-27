import pytest
from app import create_app, db
from app.models import User
from flask_jwt_extended import create_access_token

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Create a test user
            test_user = User(username='testuser', password='testpassword')
            db.session.add(test_user)
            db.session.commit()
        yield client

        with app.app_context():
            db.session.remove()
            db.drop_all()

@pytest.fixture
def access_token(client):
    with client.application.app_context():
        user = User.query.filter_by(username='testuser').first()
        token = create_access_token(identity=user.id)
        return token
