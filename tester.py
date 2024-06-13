from ubicacion_api import ubicacion_api
from ubicacion_csv import ubicacion_csv
from ubicacion_mock import ubicacion_mock
from distance import distance
from min_city_distance import min_distance

class Test:
    def __init__():
        pass

    def test_busqueda_valida(self):
        #testear las 3 apis con una ciudad valida (csv, mock, api)
        ciudad = "Lima"
        pais = "Peru"
        ubicacion = ubicacion_api()
        ubicacion.get_location(ciudad, pais)
        assert ubicacion.get_latitud() == -12.046374
        assert ubicacion.get_longitud() == -77.0427934

        ubicacion = ubicacion_csv()
        ubicacion.get_location(ciudad, pais)
        assert ubicacion.get_latitud() == -12.046374
        assert ubicacion.get_longitud() == -77.0427934

        ubicacion = ubicacion_mock()
        ubicacion.get_location(ciudad, pais)
        assert ubicacion.get_latitud() == -12.046374
        assert ubicacion.get_longitud() == -77.0427934
    
    def test_busqueda_invalida(self):
        #testear las 3 apis con una ciudad invalida (csv, mock, api)
        ciudad = "St. marmero"
        pais = "Antegria"
        ubicacion = ubicacion_api()
        ubicacion.get_location(ciudad, pais)
        assert ubicacion.get_latitud() == None
        assert ubicacion.get_longitud() == None

        ubicacion = ubicacion_csv()
        ubicacion.get_location(ciudad, pais)
        assert ubicacion.get_latitud() == None
        assert ubicacion.get_longitud() == None

        ubicacion = ubicacion_mock()
        ubicacion.get_location(ciudad, pais)
        assert ubicacion.get_latitud() == None
        assert ubicacion.get_longitud() == None

    def test_calculo_distancia_valida(self):
        #testear la distancia entre 2 ciudades validas
        #las vegas        
        c1_latitud = 36.1672559
        c1_longitud = -115.148516
        
        #lima
        c2_latitud = -12.0621065
        c2_longitud = -77.0365256

        distancia = distance(c1_latitud, c1_longitud, c2_latitud, c2_longitud)
        assert distancia == 8396.0
    
    def test_calculo_distancia_invalida(self):
        #testear la distancia entre 2 ciudades invalidas

        c1_latitud = -200
        c1_longitud = -200
        
        #lima
        c2_latitud = -12.0621065
        c2_longitud = -77.0365256

        distancia = distance(c1_latitud, c1_longitud, c2_latitud, c2_longitud)
        assert distancia == None

    def test_obtener_2_ciudades_cercanas_min_de_3(self):
        #testear obtener las ciudades mas cercanas a una ciudad valida
        #lima
        ciudadA = "Lima"
        paisA = "Peru"
        #las vegas
        ciudadB = "Las Vegas"
        paisB = "United States"

        #buenos aires
        ciudadC = "Buenos Aires"
        paisC = "Argentina"
        ciudades_cercanas = min_distance(ciudadA, paisA, ciudadB, paisB, ciudadC, paisC, "csv")