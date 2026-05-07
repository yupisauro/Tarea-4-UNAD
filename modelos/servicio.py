from abc import ABC, abstractmethod

# Clase para los servicios del sistema

class Servicio(ABC):
    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, *args):
        pass

    @abstractmethod
    def descripcion(self):
        pass

# Clase para reservar las salas
 
class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self.tarifa * horas

    def descripcion(self):
        return f"Sala: {self.nombre}"

# Clase para alquiler de equipos 

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        return self.tarifa * dias

    def descripcion(self):
        return f"Equipo: {self.nombre}"

# Clase para asesorias del servicio

class Asesoria(Servicio):
    
    # Calcula el costo segun el tiempo del servicio 
    
    def calcular_costo(self, horas):
        return self.tarifa * horas

# Devuelve la descripcion del servicio 

    def descripcion(self):
        return f"Asesoría: {self.nombre}"