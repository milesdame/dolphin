import sys
import os
import pytest

sys.path.insert(0, '/Users/milesdame/Documents/dolphin/app')
os.chdir('/Users/milesdame/Documents/dolphin/app')

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client        

def test_some_route(client):
    response = client.get('/anatomy')
    assert response.status_code == 200