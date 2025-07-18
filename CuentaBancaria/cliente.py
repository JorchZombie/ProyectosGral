#===========================> LIBRERIAS
from datos import datos
from persona import persona
import os
#import system
import random


class cliente(datos):
    def __init__(self, cuenta, balance, nombre, apellido):
        super().__init__(cuenta, balance, nombre, apellido)
        
    def __str__(self):
        return super().__srt__()
    
    def CrearCliente():
        print("===========> CREAR CLIENTE <===========")
        print("proporcione los datos necesarios")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cuenta = "ES" + str(random.randint(100000, 999999))