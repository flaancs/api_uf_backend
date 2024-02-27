import requests
from bs4 import BeautifulSoup
import os

def get_uf_value(year: int, month: int, day: int) -> str:
    """
    Get the value of UF for a specific date.
    :param year: Year of the date.
    :param month: Month of the date.
    :param day: Day of the date.
    :return: The value of UF for the specified date.
    """ 
    base_url = os.getenv('BASE_URL', None)
    final_url = f"{base_url}{year}.htm"
    response = requests.get(final_url)
    
    if response.status_code != 200:
        raise Exception("Error al acceder al SII.")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    div_container = soup.find('div', id='mes_all')
    if not div_container:
        raise Exception("No se ha encontrado el contenedor de la tabla de todos los meses.")
    
    table = div_container.find('table')
    if not table:
        raise Exception("No se ha encontrado la tabla con los valores de UF.")
    
    months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    searched_month = months[month-1]
    
    try:
        headers = table.find('thead').find_all('th')
        month_index = None
        for i, th in enumerate(headers):
            if th.text.strip() == searched_month:
                month_index = i
                break
        
        if month_index is None:
            raise ValueError("La tabla no posee información para el mes proporcionado.")
        
        rows = table.find('tbody').find_all('tr')
        for row in rows:
            day_cell = row.find('th', style="text-align:center;")
            if day_cell and int(day_cell.text.strip()) == day:
                uf_value = row.find_all('td')[month_index-1].text.strip()
                if uf_value == "":
                    raise ValueError("No se ha encontrado el valor de UF para la fecha especificada.")
                return uf_value
        
        raise ValueError("No se ha encontrado el valor de UF para la fecha especificada.")
    except Exception as e:
        raise Exception(e)