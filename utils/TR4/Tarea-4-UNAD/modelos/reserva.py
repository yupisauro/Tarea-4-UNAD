from excepciones.errores import ReservaError
from utils.logger import registrar_log
# Comentario agregado para documentacion

# Clase que representa una reserva del sistema

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaError("Duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
        
# Calcula el costo total del servicio reservado 

    def calcular_total(self):
        try:
            return self.servicio.calcular_costo(self.duracion)
        except Exception as e:
            registrar_log(f"Error cálculo: {e}")
            raise ReservaError("Error al calcular") from e

# Confirma la reserva y cambia el estado 

    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise ReservaError("La reserva ya fue procesada")

            self.estado = "confirmada"
            registrar_log("Reserva confirmada")

        except Exception as e:
            registrar_log(f"Error confirmar: {e}")
            print("❌ Error:", e)

# Cancela la reserva 

    def cancelar(self):
        try:
            self.estado = "cancelada"
            registrar_log("Reserva cancelada")
        except Exception as e:
            registrar_log(f"Error cancelar: {e}")