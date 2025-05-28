import os
import sys
import tempfile
import pytest

# Assurez-vous que le chemin vers l'application est dans sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    # S'assurer que le dossier de test existe
    os.makedirs('/data', exist_ok=True)
    with open('/data/test.txt', 'w') as f:
        f.write("Hello World")

    yield client

def test_api_files(client):
    response = client.get('/api/files')
    assert response.status_code == 200
    assert "test.txt" in response.json

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"test.txt" in response.data

def test_download_file(client):
    response = client.get('/download/test.txt')
    assert response.status_code == 200
    assert b"Hello World" in response.data
