#Actividad_6
#Emilio_Garcia_Giaquinta

class Cuenta:
    def _init_(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def ingresar(self):
        print("Ingrese una cantidad")
    def retiro(self):
        print("retiro la cantidad ingresada")
Cuenta1 = Cuenta
Cuenta1.ingresar(1800)
Cuenta1.retiro(1000)