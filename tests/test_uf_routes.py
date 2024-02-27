from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_uf_value_good_case():
    """
    Test for the case where the UF value is successfully retrieved.
    """
    date_str = "2022-01-01"
    response = client.get(f"/uf-value/{date_str}")

    assert response.status_code == 200
    assert "uf_value" in response.json()


def test_uf_value_no_date():
    """
    Test for the case where no date is provided.
    """
    response = client.get("/uf-value/")

    assert response.status_code == 404


def test_uf_value_invalid_format():
    """
    Test for the case where the date format is invalid.
    """
    date_str = "01-01-2022"
    response = client.get(f"/uf-value/{date_str}")

    assert response.status_code == 400
    assert response.json() == {"detail": "Formato de fecha inválido. Por favor use YYYY-MM-DD."}


def test_uf_value_below_minimum_date():
    """
    Test for the case where the provided date is below the minimum allowed date (01-01-2013).
    """
    date_str = "2012-12-31"
    response = client.get(f"/uf-value/{date_str}")

    assert response.status_code == 400
    assert response.json() == {"detail": "La fecha no puede ser menor a 01-01-2013."}