from T01 import *
from Importador import *
from datetime import date, timedelta, datetime
import io

def variable_espera():
    input("Aprete enter para continuar: ")

#Copiado de stack overflow y cambiado
def main_menu():
    choice ='0'
    while choice =='0':
        print("Opcion Principal: Elija 1 de 2 opciones")
        print("Presione 1 para registrarse")
        print("Presione 2 para iniciar sesión")

        choice = input ("Please make a choice: ")

        if choice == "1":
            register_menu(choice)
            signed_in = sign_in_menu(choice, "")
            return signed_in

        elif choice == "2":
            signed_in = sign_in_menu(choice, "")
            return signed_in

        else:
            print("-------------------")
            print("Probemos nuevamente")
            print("-------------------")
            main_menu()


def register_menu(choice1):
    while choice1 == "1":
        a = True
        user = input ("Ingrese su nombre de usuario: ")
        while a == True:
            if Users.revisar_si_en_sistema(user, lista_users) == True:
                print("Usuario ya existe, escriba otro:")
                user = input ("Ingrese su nombre de usuario: ")
            else:
                a = False


        name = input ("Ingrese su nombre: ")
        lastname = input ("Ingrese su apellido: ")
        birthdate = input ("Ingrese su cumpleaños "
                           "en el formato YYYY-MM-DD: ")
        #Convertimos el string en un date
        cumple = birthdate.split("-")
        cumple2 = datetime(int(cumple[0]),
                           int(cumple[1]), int(cumple[2]))
        orders = []
        new_register = Users(user, name, lastname, birthdate, orders)
        lista_users.append(new_register)
        new_register.categorizar()
        choice1 = 0
        sign_in_menu(1, "")


def sign_in_menu(choice2, signed_in):

    while choice2 == "1" or choice2 == "2":
        print("-------------------")
        print("Inicio Sesión")
        probando_usuario = input("Escriba su nombre de usuario: ")
               #Busca la persona2
        if Users.revisar_si_en_sistema(probando_usuario,
                                    lista_users) == True:
            print("Ha iniciado sesión correctamente")
            print("-------------------")
            for i in range(len(lista_users)):
                if lista_users[i].username == probando_usuario:
                    signed_in = lista_users[i]
                    choice2 = 0

        else:
            print("Ingrese un usuario valido")
        #name: string;orders: list;birthday: string;lastname: string;username: string


    while choice2 == 0:

        print("Usted tiene: ")
        for i in range(len(signed_in.cantidad_moneda)):
            print(signed_in.cantidad_moneda[i])
        print("-------------------")
        print("Elija la opción que desee")                              #Listo
        print("Presione 1 para: Lista de Mercados Disponibles")         #Listo
        print("Presione 2 para: Lista de Mercados en los "              #Listo
              "que se encuentra registrado")
        print("Presione 3 para: Registrarse en un mercado nuevo")       #Listo
        print("Presione 4 para: Lista de orders segun tiempo")          #Listo
        print("Presione 5 para: Lista de orders activas")               #Listo
        print("Presione 6 para: Generar una oferta de venta (ask)")     #Listo
        print("Presione 7 para: Generar una oferta de compra (bid)")    #Listo
        print("Presione 8 para: Información "                           #Listo Casi
              "de los mercados en los que se encuentra registrado")
        print("Presione 9 para: Banco, Transferir dinero a terceros")   #Listo
        print("Presione 10 para: Consultas generales")                  #Pendiente
        print("Presione 11 para: Cerrar sesión")                        #Listo
        print("Presione 12 para: Cerrar todo el sistema")
        #Falta hacer los matches

        choice2 = input ("Elija una opción: ")
        if choice2 == "1":
            choice_1(choice2, signed_in)
        if choice2 == "2":
            choice_2(choice2, signed_in)
        if choice2 == "3":
            choice_3(choice2, signed_in)
        if choice2 == "4":
            choice_4(choice2, signed_in)
        if choice2 == "5":
            choice_5(choice2, signed_in)
        if choice2 == "6":
            choice_6(choice2, signed_in)
        if choice2 == "7":
            choice_7(choice2, signed_in)
        if choice2 == "8":
            choice_8(choice2, signed_in)
        if choice2 == "9":
            choice_9(choice2, signed_in)
        if choice2 == "10":
            choice_10(choice2, signed_in)
        if choice2 == "11":
            main_menu()
        if choice2 == "12":
            choice_12(lista_users, lista_orders)
        else:
            sign_in_menu(0, signed_in)

            #Escribir función que me escriba archivos con los nuevos datos
        return signed_in

def choice_1(choice2, signed_in):
    while choice2 == "1":
        print("-------------------")
        print("Lista de Mercados Disponibles:")
        for i in range (len(lista_mercados)):
            print(str(i) + ". -" + lista_mercados[i].ticker)
        print("-------------------")
        variable_espera()
        sign_in_menu(0, signed_in)


def choice_2(choice2, signed_in):
    while choice2 == "2":
        print("-------------------")
        largo = len(signed_in.mercados_registrados)
        if largo > 0:
            print("Usted está registrado en los "
                  "siguientes mercados:")
            for i in range (largo):
                print(signed_in.mercados_registrados[i].ticker)
        if largo == 0:
            print("Usted no está regitrado en ningun mercado")
        print("-------------------")

        variable_espera()
        sign_in_menu(0, signed_in)

def choice_3(choice2, signed_in):
    while choice2 == "3":
        print("-------------------")
        print("Presione el numero asociado a el mercado que desea"
              " registrarse: ")
        for i in range (len(lista_mercados)):
            print(str(i) + ". -" + lista_mercados[i].ticker)

        try:
            mercado_nuevo = input("Ingrese el numero del"
                              " mercado a entrar: ")
            mercado_nuevo = int(mercado_nuevo)
            if mercado_nuevo >= len(lista_mercados):
                print("Presione un número valido")
                choice_3("3", signed_in)
            else:
                signed_in.agregar_mercado(mercado_nuevo,
                                          lista_mercados)
                choice2 = 0

        except:
            choice_3("3", signed_in)

    variable_espera()
    print("-------------------")
    sign_in_menu(0, signed_in)

def choice_4(choice2, signed_in):
    signed_in.mostrar_orders()
    sign_in_menu(0, signed_in)
def choice_5(choice2, signed_in):
    signed_in.mostrar_activas()
    variable_espera()
    sign_in_menu(0, signed_in)
def choice_6(choice2, signed_in):
    signed_in.crear_ask(lista_orders, lista_users)
    sign_in_menu(0, signed_in)
def choice_7(choice2, signed_in):
    signed_in.crear_bid(lista_orders, lista_users)
    sign_in_menu(0, signed_in)
def choice_8(choice2, signed_in):
    signed_in.mostrar_info_mercados(lista_users, lista_orders)
    sign_in_menu(0, signed_in)
def choice_9(choice2, signed_in):
    signed_in.transferencia(lista_users)
def choice_10(choice2, signed_in):
    for i in range(len(lista_mercados)):
        lista_mercados[i].mostrar_mercado()
def choice_12(lista_users, lista_orders):
    print("Escibiendo todos sus cambios en el sistema")
    #Escribiendo los Users junto a sus nuevos orders
    data = io.open("users.csv", 'w', encoding="latin-1")
    print("name: string;orders: list;birthday: string;lastname: "
          "string;username: string", file = data)
    for i in range(len(lista_users)):
        string_orders = ""
        for k in range(len(lista_users[i].orders)):
            string_orders = string_orders + \
                            lista_users[i].orders[k].order_id + ":"

        string_orders = string_orders[:-1]

        print(lista_users[i].name + ";" + string_orders + ";" +
              lista_users[i].birthdate + ";" +
              lista_users[i].lastname + ";" +
              lista_users[i].username, file = data)

    data.close()
    #Escribiendo el csv de orders

    data = io.open("orders.csv", 'w', encoding="latin-1")
    print("ticker: string;type: string;amount: float;price: "
          "float;date_match: string;date_created: string;order_id:"
          " int", file = data)
    for i in range(len(lista_orders)):
        ticker = lista_orders[i].ticker
        tipo = lista_orders[i].tipo
        cantidad = lista_orders[i].amount
        precio = lista_orders[i].price
        date_match = lista_orders[i].date_match
        date_created = lista_orders[i].date_created
        order_id = lista_orders[i].order_id
        print(ticker + ";" + tipo + ";" + cantidad + ";" + precio + ";" + date_match + ";" + date_created + ";" + order_id, file = data)

    data.close()


signed_in = main_menu()
