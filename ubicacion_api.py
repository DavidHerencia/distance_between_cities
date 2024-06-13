from ubicacion_interface import ubicacion_interface

import urllib, json
import urllib.request


class ubicacion_api(ubicacion_interface):
    def __init__(self):
        super().__init__()

    def get_location(self, city, country):
        city = city.replace(" ", "_")
        country = country.replace(" ", "_")
        # to lower case
        city = city.lower()
        country = country.lower()
        url = (
            "https://nominatim.openstreetmap.org/search?q="
            + city
            + ","
            + country
            + "&format=json"
        )
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        self.latitud = data[0]["lat"]
        self.longitud = data[0]["lon"]

    def get_latitud(self):
        return self.latitud

    def get_longitud(self):
        return self.longitud

    def set_latitud(self, latitud):
        self.latitud = latitud

    def set_longitud(self, longitud):
        self.longitud = longitud
