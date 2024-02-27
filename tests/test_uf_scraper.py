import pytest
from scraping.uf_scraper import get_uf_value

def test_get_uf_value(mock_response, uf_html_response):
    """
    Test the get_uf_value function for a correct case where the UF value is successfully retrieved.
    """
    year, month, day = 2023, 1, 1
    expected_uf_value = "30.000,00"
    base_url = "https://www.sii.cl/valores_y_fechas/uf/uf"
    mock_url = f"{base_url}{year}.htm"
    
    mock_response.get(mock_url, text=uf_html_response)
    actual_uf_value = get_uf_value(year, month, day)

    assert actual_uf_value == expected_uf_value


def test_get_uf_value_empty_value(mock_response, uf_html_response):
    """
    Test the get_uf_value function for a case where the UF value is empty.
    """
    year, month, day = 2023, 2, 1
    base_url = "https://www.sii.cl/valores_y_fechas/uf/uf"
    mock_url = f"{base_url}{year}.htm"
    
    mock_response.get(mock_url, text=uf_html_response)
    
    with pytest.raises(Exception) as exc_info:
        get_uf_value(year, month, day)
    
    assert "No se ha encontrado el valor de UF para la fecha especificada." in str(exc_info.value)


def test_get_uf_value_incorrect_date(mock_response, uf_html_response):
    """
    Test the get_uf_value function for an incorrect case where the UF value cannot be found for the given date.
    """
    year, month, day = 2023, 2, 30
    base_url = "https://www.sii.cl/valores_y_fechas/uf/uf"
    mock_url = f"{base_url}{year}.htm"
    
    mock_response.get(mock_url, text=uf_html_response)
    
    with pytest.raises(Exception) as exc_info:
        get_uf_value(year, month, day)
    
    assert "No se ha encontrado el valor de UF para la fecha especificada." in str(exc_info.value)
