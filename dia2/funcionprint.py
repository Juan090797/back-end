numero = int(input("Ingrese el numero: "))

for contador in range(1,numero+1):
    if(contador == 1 or contador == numero):  
        print("* " * numero)
    else: 
        print("*" + str('  ' * (numero-2)) + ' *')