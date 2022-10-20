from email import header
from tabulate import tabulate

tabla = [
    ["Juan Marquina","juanmarquina@gmail.com","989688456"],
    ["Piero Marquina","pieromarquina@gmail.com","989688457"],
    ["Clara Marquina","claramarquina@gmail.com","989688458"]
]

columnas = ["Nombre","Correo","Celular"]

print(tabulate(tabla,headers=columnas,tablefmt="grid"))