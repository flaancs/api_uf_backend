def test_uf_value(client, mock_redis_client, mocker):
    """
    Test for the case where the UF value is successfully retrieved.
    """
    date_str = "2022-01-01"
    expected_uf_value = "30.000,00"

    mock_redis_client.get_value.return_value = expected_uf_value
    response = client.get(f"/uf-value/{date_str}")

    assert response.status_code == 200
    assert response.json() == {"uf_value": expected_uf_value}


def test_uf_value_no_date(client):
    """
    Test for the case where no date is provided.
    """
    response = client.get("/uf-value/")

    assert response.status_code == 404


def test_uf_value_invalid_format(client):
    """
    Test for the case where the date format is invalid.
    """
    date_str = "01-01-2022"
    response = client.get(f"/uf-value/{date_str}")

    assert response.status_code == 400
    assert response.json() == {"detail": "Formato de fecha inválido. Por favor use YYYY-MM-DD."}


def test_uf_value_below_minimum_date(client):
    """
    Test for the case where the provided date is below the minimum allowed date (01-01-2013).
    """
    date_str = "2012-12-31"
    response = client.get(f"/uf-value/{date_str}")

    assert response.status_code == 400
    assert response.json() == {"detail": "La fecha no puede ser menor a 01-01-2013."}
