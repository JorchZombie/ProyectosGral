#============> LIBRERIAS
from persona import persona

class datos(persona):
    def __init__(self, cuenta, balance, nombre, apellido):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance
        
    def __srt__(self):      #SE ESCIBREN LOS DATOS DEL CLIENTE
        #return(
        #    print(f'- Nombre: {self.nombre}\n')
        #    print(f'- \n')         no se puede hacer esto
        #    print(f'- \n')         tiene que ser con f-string
        #    print(f'- \n')
        #)
        return(
            f'===========> DATOS DEL CLIENTE <===========\n'
            f'- Nombre: {self.nombre}\n'
            f'- Apellido: {self.apellido}\n'
            f'- Num de Cuenta: {self.cuenta}\n'
            f'- Balance: {float(self.balance)}\n'
            f'\n'
            f'\n'
        )
        
    def depositar(self, dinero):
        self.balance += dinero
    
    def retirar(self, dinero):
        error = -1
        if dinero > self.balance:
            error = 0
            return error
        else:
            self.balance -= dinero
            return self.balance
        
