

# * clases Persona
#     Atributo: nombre y apellido

# * clases Cliente(Persona):
#     Atributo: numero_cuenta y balance
#     Metodo: Uno Para imprimir
#             - Deposito()
#             - Retirar()

# * Codigo para elegir Deposito, Retirar o salir
#     * Funcion Crear-cliente()
#                 inicio()

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'cliente: {self.nombre} {self.apellido} \n Balance de cuenta {self.numero_cuenta}: ${self.balance}'

    def depositar (self, monto_depositar):
        self.balance += monto_depositar
        print ('Deposito aceptado')

    def retirar (self, retirar_monto):
        if self.balance >= retirar_monto:
            self.balance -= retirar_monto
            print('Retiro realizado')
        else: 
            print('Fondos insuficientes')  

def crear_cliente():
    nombre_cl = input('Ingrese su nombre: ')
    apellido_cl = input('Ingrese su apellido: ')
    numero_cuenta_cl = input('Ingrese su numero de cuenta: ')
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta_cl)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print ('Elige: Depositar (D), Retirar (R), o salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input('Monto depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print('Gracias por operar en Banco Python')

inicio()        