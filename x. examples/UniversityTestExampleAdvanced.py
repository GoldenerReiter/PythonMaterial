class User:
    def __init__(self, run=0, nombre=None, direccion=None, comuna=None, subscripcion=None):
        self.run = run
        self.nombre = nombre
        self.direccion = direccion
        self.comuna = comuna
        self.subscripcion = subscripcion

    @classmethod
    def user_creation(cls):
        return cls(int(input('Inserte su run')), input('Inserte su nombre'), input('Inserte su direccion'),
                   input('inserte su comuna'), input('Inserte su tipo de subscripcion (feliz, sufriente o premium)'))

    def auto_describe(self):
        print('run: ', self.run, '\n nombre: ', self.nombre, '\n direccion: ', self.direccion, '\n comuna: ',
              self.comuna, '\n subscripcion: ', self.subscripcion, '\n')

    def sus_auto_change(self):
        self.subscripcion = sus_maker()
        print('Su nuevo tipo de subscripcion es: ', self.subscripcion)


def menu_client():
    print("\t John Bonachon app")
    print("1 Registrar Cliente")
    print("2 Suscripcion cliente")
    print("3 Consultar datos cliente")
    print("4 Salir\n")
    menu_op()


def menu_op():
    option = int(input('Inserte su opcion\n'))
    try:
        if option == 1:
            print("Registro de clientes\n")
            client_reg()
            menu_client()
        elif option == 2:
            print("suscripcion de cliente\n")
            client_sus_change()
            menu_client()
        elif option == 3:
            print("consultar datos de cliente\n")
            client_con()
            menu_client()
        elif option == 4:
            print("usted ha salido del sistema")
            print("Gracias por utilizar a la App de John Bonachon")
            return
        else:
            menu_op()
    except ValueError:
        print('Error: Entrada invalida. Retornando al menu.')
        menu_op()


def client_reg():
    user = User.user_creation()
    if user.run < 1000000 or ((user.subscripcion != 'feliz') and (user.subscripcion != 'sufriente') and (user.subscripcion != 'premium')):
        print('Tu run es falso o tu subscripcion es incorrecta :(')
        del user
    else:
        registros.append(user)
        print('¡Creacion de usuario completada con exito!')


def client_con():
    if len(registros) == 0:
        print('No existen registros para consultar. Haga un registro e intente nuevamente.')
    elif len(registros) >= 1:
        runcliente = int(input('\ninserte su run: '))
        if list(filter(lambda i: i['run'] != runcliente, registros)):
            print('El run que consulto no existe, intente nuevamente')
        else:
            print(list(filter(lambda i: i['run'] == runcliente, registros)))


def client_sus_change():
    if len(registros) == 0:
        print('No existen registros para consultar. Haga un registro e intente nuevamente.\n')
    elif len(registros) >= 1:
        runcliente = int(input('inserte su run: '))
        for _, value in enumerate(registros):
            if runcliente == value.run:
                value.sus_auto_change()
            else:
                print('No existe el rut que inserto en nuestros registros\n')


def sus_maker(subscripcion=''):
    while (subscripcion != 'feliz') and (subscripcion != 'sufriente') and (subscripcion != 'premium'):
        try:
            subscripcion = input('Inserte su tipo de subscripcion (feliz, sufriente o premium): ')
            subscripcion.lower()
        except ValueError:
            print('Error: Entrada invalida. Retornando al menu.\n')
            menu_op()
    return subscripcion


registros = []
menu_client()
