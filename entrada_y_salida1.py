import pickle


nombres = ["Angel", "Nashe"]

f = open("juguete", "wb")
pickle.dump(nombres, f)
f.close()
del(f)


f = open("juguete", "rb")
lista = pickle.load(f)
print(lista)
