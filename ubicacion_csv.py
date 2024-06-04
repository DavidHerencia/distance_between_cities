from ubicacion_interface import ubicacion_interface
import pandas as pd

class ubicacion_csv(ubicacion_interface): # Las Vegas / United States
    def __init__(self):
        super().__init__()

    def get_location(self, city, country):
        df = pd.read_csv('worldcities.csv')
        # to lower case 
        city = city.lower()
        country = country.lower()

        if country != "":
            temp = df[(df['city_ascii'].str.lower() == city) & (df['country'].str.lower() == country)]
        else :
            temp = df[(df['city_ascii'].str.lower() == city)]
            
        self.latitud = temp['lat'].values[0]
        self.longitud = temp['lng'].values[0]

    def get_latitud(self):
        return self.latitud

    def get_longitud(self):
        return self.longitud

    def set_latitud(self, latitud):
        self.latitud = latitud

    def set_longitud(self, longitud):
        self.longitud = longitud

