#entrada
tabla = input("Ingrese la tabla de multiplicar: ")
#salida
for contador in range(1,13):
    print(tabla + " x " + str(contador) + " = " + str(contador * int(tabla)))