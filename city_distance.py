from ubicacion_api import ubicacion_api
from ubicacion_csv import ubicacion_csv
from ubicacion_mock import ubicacion_mock
from ubicacion_interface import ubicacion_interface
from distance import distance

def calc_distance(city_1, country_1, city_2, country_2, service):
    if service == "csv":
        ubicacion = ubicacion_csv()
    elif service == "mock":
        ubicacion = ubicacion_mock()
    elif service == "api":
        ubicacion = ubicacion_api()

    ubicacion.get_location(city_1, country_1)
    latitud_1 = float(ubicacion.get_latitud())
    longitud_1 = float(ubicacion.get_longitud()) 

    ubicacion.get_location(city_2, country_2)
    latitud_2 = float(ubicacion.get_latitud())
    longitud_2 = float(ubicacion.get_longitud())

    # Convertir las coordenadas de grados a radianes
    dist = distance(latitud_1, longitud_1, latitud_2, longitud_2)

    return f"{dist:.2f} km"