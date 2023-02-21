def anio(fecha):
    if fecha % 4 == 0:
        print("es bisiesto")
    else:
        print("no es bisiesto")


variable = int(input("Ingrese un anio: "))
anio(variable)
