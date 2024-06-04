from ubicacion_interface import ubicacion_interface


class ubicacion_mock(ubicacion_interface):  # Las Vegas / United States
    def __init__(self):
        super().__init__()

    def get_location(self, city, country):
        if city == "Las Vegas":
            self.latitud = 36.1672559
            self.longitud = -115.148516
        else:
            self.latitud = -12.0621065
            self.longitud = -77.0365256

    def get_latitud(self):
        return self.latitud

    def get_longitud(self):
        return self.longitud

    def set_latitud(self, latitud):
        self.latitud = latitud

    def set_longitud(self, longitud):
        self.longitud = longitud
