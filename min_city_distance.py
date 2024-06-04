from ubicacion_api import ubicacion_api
from ubicacion_csv import ubicacion_csv
from ubicacion_mock import ubicacion_mock
from ubicacion_interface import ubicacion_interface
from distance import distance

#Retonar las ciudades con distancia la menor distancia entre ellas (3 ciudades)
def min_distance(city_1,country_1,city_2,country_2,city_3,country_3,service):
    #Inicializar las ubicaciones
    ubicacion = ubicacion_interface()
    if service == "csv":
        ubicacion = ubicacion_csv()
    elif service == "mock":
        ubicacion = ubicacion_mock()
    elif service == "api":
        ubicacion = ubicacion_api()
    
    
    
    #Obtener las ubicaciones de las ciudades
    ubicacion.get_location(city_1, country_1)
    latitud_1 = float(ubicacion.get_latitud())
    longitud_1 = float(ubicacion.get_longitud()) 

    ubicacion.get_location(city_2, country_2)
    latitud_2 = float(ubicacion.get_latitud())
    longitud_2 = float(ubicacion.get_longitud())

    ubicacion.get_location(city_3, country_3)
    latitud_3 = float(ubicacion.get_latitud())
    longitud_3 = float(ubicacion.get_longitud())
    
    distancia1_2 = distance(latitud_1, longitud_1, latitud_2, longitud_2)
    distancia1_3 = distance(latitud_1, longitud_1, latitud_3, longitud_3)
    distancia2_3 = distance(latitud_2, longitud_2, latitud_3, longitud_3)
    
    distancia_minima = min(distancia1_2, distancia1_3, distancia2_3)
    if distancia_minima == distancia1_2:
        return city_1 + " y " + city_2
    elif distancia_minima == distancia1_3:
        return city_1 + " y " + city_3
    else:
        return city_2 + " y " + city_3

    