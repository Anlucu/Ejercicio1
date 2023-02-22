class Vehiculo():

    def __init__(self, color, rueda, puerta):
        self.color = color
        self.rueda = rueda
        self.puerta = puerta


class Coche(Vehiculo):

    def __init__(self, color, rueda, puerta, velocidad, cilindrada):
        Vehiculo.__init__(self, color, rueda, puerta)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def Mostrar(self):
        return f"Color: {self.color}\nRuedas: {self.rueda}\nPuertas: {self.puerta}\nVelocidad: {self.velocidad}\nCilindrada: {self.cilindrada}"


a = Coche("Azul", 4, 5, 1111, 3)

print(a.Mostrar())
