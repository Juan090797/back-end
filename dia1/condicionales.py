#entrada
from unittest import result


numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")
operacion = input("Operacion a ejecutar(suma/resta): ")
#proceso
if(operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif(operacion == "resta"):
    resultado = int(numero1) - int(numero2)
else:
    print("Debe ingresar una operacion validar")
#salida
if(resultado != 0):
    print("El resultado es: " + str(resultado))
