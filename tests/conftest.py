import pytest
import requests_mock
from fastapi.testclient import TestClient
from tests.html_fixtures import mock_html_content
from app.redis_client import RedisClient
from app.main import app

@pytest.fixture
def mock_response():
    """Fixture to create response for requests.get."""
    with requests_mock.Mocker() as m:
        yield m


@pytest.fixture
def uf_html_response():
    """Fixture to return a fake HTML response from SII page."""
    return mock_html_content


@pytest.fixture
def mock_redis(mocker):
    mocker.patch('app.redis_client.redis.Redis', autospec=True)
    return RedisClient()


@pytest.fixture
def mock_redis_client(mocker):
    mock = mocker.patch('app.services.uf_services.RedisClient', autospec=True)
    instance = mock.return_value
    instance.get_value.return_value = None
    instance.set_value.return_value = True
    return instance


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
