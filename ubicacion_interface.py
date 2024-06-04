from abc import ABC, abstractmethod

class ubicacion_interface(ABC):
    def __init__(self):
        self.longitud = 0
        self.latitud = 0

    @abstractmethod
    def get_location(self, city, country):
        pass

    @abstractmethod
    def get_longitud(self):
        pass
    
    @abstractmethod
    def get_latitud(self):
        pass

    @abstractmethod
    def set_longitud(self, longitud):
        pass

    @abstractmethod
    def set_latitud(self, latitud):
        pass
