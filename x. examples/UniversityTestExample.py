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
    run = 0
    while run < 5000000 or run > 999999999:
        run = int(input("Ingrese su run: \n"))
    nombre = None
    print('Inserte su nombre: ')
    nombre = data_maker(nombre)
    nombre.capitalize()
    direccion = None
    print('Inserte su direccion: ')
    direccion = data_maker(direccion)
    comuna = None
    print('Inserte su comuna: ')
    comuna = data_maker(comuna)
    suscripcion = ''
    suscripcion = sus_maker(suscripcion)
    user = {
        'run': run,
        'nombre': nombre,
        'direccion': direccion,
        'comuna': comuna,
        'suscripcion': suscripcion
    }
    registros.append(user)
    return registros


def client_con():
    if len(registros) == 0:
        print('No existen registros para consultar. Haga un registro e intente nuevamente.')
    elif len(registros) >= 1:
        runcliente = int(input('\ninserte su run: '))
        for _, value in enumerate(registros):
            # la alternativa a este codigo: usershow = list(filter(lambda user: user['run'] == runcliente, registros))
            if runcliente == value['run']:
                print('\nSus datos se imprimiran a continuacion: ')
                print(value)


def client_sus_change():
    if len(registros) == 0:
        print('No existen registros para consultar. Haga un registro e intente nuevamente.\n')
    elif len(registros) >= 1:
        runcliente = int(input('inserte su run\n'))
        suscripcion = ''
        for _, value in enumerate(registros):
            if runcliente == value['run']:
                print('Su tipo de suscripcion es: ', value['suscripcion'])
                suscripcion = sus_maker(suscripcion)
                value['suscripcion'] = suscripcion
                print('Su tipo de cliente ahora es: ', value['suscripcion'])
            else:
                print('No existe el rut que inserto')



def sus_maker(suscripcion=''):
    while (suscripcion != 'feliz') and (suscripcion != 'sufriente') and (suscripcion != 'premium'):
        try:
            suscripcion = input(
                'inserte su tipo de suscripcion: \n')
            suscripcion.lower()
        except ValueError:
            print(
                'Error: Entrada invalida. Retornando al menu.')
            menu_op()
    return suscripcion


def data_maker(data):
    while data is None:
        try:
            data = input()
        except ValueError:
            print('Error: Entrada invalida. Retornando al menu.')
            menu_op()
    return data


registros = []
menu_client()
