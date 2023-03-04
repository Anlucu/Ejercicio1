import pickle


class vehiculo():

    def __init__(self):
        self.auto = "Camaro"
        self.ruedas = 4
        self.puertas = 4


auto = vehiculo()

f = open("clase", "wb")
pickle.dump(auto, f)
f.close()
del(f)

f = open("clase", "rb")
lista = pickle.load(f)
f.close()
