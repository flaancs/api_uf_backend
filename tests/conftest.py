import pytest
import requests_mock
from tests.html_fixtures import mock_html_content

@pytest.fixture
def mock_response():
    """Fixture to create response for requests.get."""
    with requests_mock.Mocker() as m:
        yield m

@pytest.fixture
def uf_html_response():
    """Fixture to return a fake HTML response from SII page."""
    return mock_html_content
