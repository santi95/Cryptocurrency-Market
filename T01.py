import numpy
from datetime import date, timedelta, datetime
import random
import operator

class Users:
    def __init__(self, username, name, lastname, birthdate, orders):
        self.username = username
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate
        self.orders = orders
        self.categoria = "no tiene"
        self.cuota_investor = False
        self.mercados_registrados = []
        self.cantidad_moneda = []
        self.lista_monedas = []


    def agregar_mercado(self, mercado, lista_mercados):
        if lista_mercados[mercado] in self.mercados_registrados:
            print("Usted ya está registrado en este mercado")
            print("-------------------")
        else:
            self.mercados_registrados.append(lista_mercados[mercado])
            if self.categoria != ("Underage"):
                curr1 = lista_mercados[mercado].mon1
                curr2 = lista_mercados[mercado].mon2
                if curr1.name == ("DCCapital"):
                    if curr1.name not in self.lista_monedas:
                        self.cantidad_moneda.append(
                            (lista_mercados[mercado].mon1, 100000))
                    if curr2.name not in self.lista_monedas:
                        self.cantidad_moneda.append(
                            (lista_mercados[mercado].mon2, 50000))
                elif curr2.name == ("DCCapital"):
                    if curr2.name not in self.lista_monedas:
                        self.cantidad_moneda.append((curr2, 100000))
                    if curr1.name not in self.lista_monedas:
                        self.cantidad_moneda.append((curr1, 50000))
                else:
                    if curr1.name not in self.lista_monedas:
                        self.cantidad_moneda.append((curr1, 50000))
                    if curr2.name not in self.lista_monedas:
                        self.cantidad_moneda.append((curr2, 50000))

                self.lista_monedas = []
                for i in range(len(self.cantidad_moneda)):
                    self.lista_monedas.append(
                        self.cantidad_moneda[i][0].name)



            elif self.categoria == ("Underage"):
                print("Ha agregado el mercado satisfactoriamente,"
                      " pero el magnate no le ha regalado nada")
                print("-------------------")
        print(self.lista_monedas)


    def revisar_si_en_sistema(usuario, lista_users):
        for i in range(len(lista_users)):
            if lista_users[i].username == usuario:
                signed_in = lista_users[i]
                return True

    def categorizar(self):
        today = datetime.today()
        cumple = self.birthdate.split("-")
        cumple2 = datetime(int(cumple[0]),
                           int(cumple[1]), int(cumple[2]))

        age = (today - cumple2) // timedelta(days=365.2425)  # Esta linea sacada de StackOverflow
        age = int(age)

        if age < 18:
            self.categoria = "Underage"

        if age >= 18:
            self.categoria = "Trader"

        if age >= 18 and self.cuota_investor == True:
            self.categoria = "Investor"

    def crear_ask(self, lista_orders, lista_users):

        if len(self.mercados_registrados) != 0:
            lista_orders_id = []
            for i in range(len(lista_orders)):
                lista_orders_id.append(lista_orders[i].order_id)
            print("Elija el mercado en el que quiere vender: ")
            for i in range(len(self.mercados_registrados)):
                print(str(i) + "- " + str(
                    self.mercados_registrados[i].ticker))
            mercado_elegido = input("Elija su opción: ")
            n_mercado_elegido = int(mercado_elegido)
            mercado_elegido = self.mercados_registrados[
                n_mercado_elegido]
            #Creando el ASK
            #Restamos la cantidad de plata que quiere vender de su saldo

            date_created = datetime.today()
            date_match = ""
            cantidad = input("Cuanto " + str(mercado_elegido.mon1)
                             + " quiere vender?: ")
            precio = input("A cuanto " + str(mercado_elegido.mon2)
                           + " quiere vender cada unidad?: ")
            precio = (precio , mercado_elegido.mon2)
            tipo = "ask"
            ticker = self.mercados_registrados[n_mercado_elegido]

            saldo = True
            while saldo == True:
                for i in range(len(self.lista_monedas)):
                    if self.cantidad_moneda[i][0].name == \
                            mercado_elegido.mon1.name:
                        if self.cantidad_moneda[i][1] >= int(cantidad):
                            #self.cantidad_moneda[i][0] es nombre
                            moneda = self.cantidad_moneda[i][0]
                            saldo = self.cantidad_moneda[i][1]
                            saldo= saldo - int(cantidad)
                            self.cantidad_moneda[i] = (moneda, saldo)
                            saldo = False
                        else:
                            print("Usted no tiene " + str(moneda.name)
                                  + " suficiente")
                            cantidad = input("Cuanto " + str(
                                mercado_elegido.mon1) +
                                             " quiere vender?: ")
                            precio = input("A cuanto " + str(
                                mercado_elegido.mon2) + " "
                                        "quiere vender cada unidad?: ")

            b = True
            while b == True:
                #numero de orders es random y revisa si esque ya existe.
                order_id = random.randint(0, 9999)
                order_id = str(order_id)
                if order_id not in lista_orders_id:
                    final = Orders(order_id, date_created,
                                   date_match, cantidad, precio,
                                   tipo, ticker)
                    final.categoria = "Pending"
                    final.mercado = mercado_elegido
                    lista_orders.append(final)
                    self.orders.append(final)
                    print("-------------------")

                    b = False
                else:
                    b = True
            mercado_elegido.revisar_si_match(lista_users)

        else:
            print("Usted no está registrado en ningun mercado")


    def crear_bid(self, lista_orders, lista_users):
        if len(self.mercados_registrados) != 0:
            lista_orders_id = []
            for i in range(len(lista_orders)):
                lista_orders_id.append(lista_orders[i].order_id)
            print("Elija el mercado en el que quiere comprar: ")
            for i in range(len(self.mercados_registrados)):
                print(str(i) + "- " + str(
                    self.mercados_registrados[i].ticker))
            mercado_elegido = input("Elija su opción: ")
            n_mercado_elegido = int(mercado_elegido)
            mercado_elegido = self.mercados_registrados[n_mercado_elegido]
            #Creando el ASK
            date_created = datetime.today()
            date_match = ""
            cantidad = input("Cuanto " + str(
                mercado_elegido.mon1) + " quiere comprar?: ")
            tipo = "bid"
            ticker = self.mercados_registrados[n_mercado_elegido]
            precio = input("A cuanto " + str(
                mercado_elegido.mon2) + " quiere comprar "
                                        "cada unidad?: ")
            precio = int(precio)

            #revisando que puede comprar la cantidad que quiere

            saldo = True
            while saldo == True:
                for i in range(len(self.lista_monedas)):
                    if self.cantidad_moneda[i][0].name == \
                            mercado_elegido.mon2.name:
                        #[0] es la moneda
                        if self.cantidad_moneda[i][1] >= \
                                        float(cantidad)*(precio):
                            saldo = self.cantidad_moneda[i][1]
                            moneda = self.cantidad_moneda[i][0]
                            saldo = saldo - float(cantidad)*(precio)
                            self.cantidad_moneda[i] = (moneda, saldo)
                            saldo = False

                        else:
                            print("Usted no tiene saldo suficiente")
                            cantidad = input("Cuanto " + str(
                                mercado_elegido.mon1) +
                                             " quiere comprar?: ")
                            precio = input("A cuanto " + str(
                                mercado_elegido.mon2) + " quiere"
                                            " comprar cada unidad?: ")



            b = True
            while b == True:
                order_id = random.randint(0, 5000)
                order_id = str(order_id)
                if order_id not in lista_orders_id:
                    final = Orders(order_id, date_created,
                                   date_match, cantidad,
                                   precio, tipo, ticker)
                    final.categoria = "Pending"
                    lista_orders.append(final)
                    final.mercado = mercado_elegido
                    self.orders.append(final)
                    print("-------------------")

                    b = False
                else:
                    b = True
            mercado_elegido.revisar_si_match(lista_users)
        else:
            print("Usted no está registrado en ningun mercado")


    def mostrar_orders(self):
        today = datetime.today()
        if self.categoria == "Underage":
            print("Tiene que tener 18 para poder tener orders")
        if self.categoria == "Trader":
            try:
                print("Recuerde que usted es un Trader y puede ver "
                      "máximo 7 días para atras")
                print("Recuerde que el formato de fecha es "
                      "YYYY-MM-DD")
                fecha = input("Escriba la fecha desde la"
                              " que quiere ver sus orders: ")
                cumple = fecha.split("-")
                fecha_listada = datetime(int(cumple[0]),
                                         int(cumple[1]),
                                         int(cumple[2]))
            except:
                print("Escriba una fecha valida")
                self.mostrar_orders()

            for i in range(len(self.orders)):
                if today - fecha_listada > timedelta(days=7):
                    print("No puede ver sus orders desde tan atrás")

                if today - fecha_listada < timedelta(days=7):
                    for i in range(len(self.orders)):
                        fecha_order = self.orders[i].date_created
                        fecha_order = fecha_order.split("-")
                        fecha_order = datetime(int(fecha_order[0]),
                                               int(fecha_order[1]),
                                               int(fecha_order[2]))

                        if fecha_order > fecha_listada:
                            print(self.orders[i].order_id)

        if self.categoria == "Investor":
            try:
                print("Recuerde que usted es un Investor"
                      " y puede ver días ilimitados para atras")
                fecha = input("Escriba la fecha desde la"
                              " que quiere ver sus orders: ")
                cumple = fecha.split("-")
                fecha_listada = datetime(int(cumple[0]),
                                         int(cumple[1]),
                                         int(cumple[2]))
            except:
                print("Escriba una fecha valida")
                self.mostrar_orders()

            for i in range(len(self.orders)):
                fecha_order = self.orders[i].date_created
                fecha_order = fecha_order.split("-")
                fecha_order = datetime(int(fecha_order[0]),
                                       int(fecha_order[1]),
                                       int(fecha_order[2]))
                if fecha_order > fecha_listada:
                    print(self.orders[i].order_id)

    def mostrar_activas(self):
        for i in range(len(self.orders)):
            if len(self.orders) == 0:
                print("Usted no tiene orders activas")
            if self.orders[i].categoria == "Pending":
                print(self.orders[i])

        print("-------------------")


    def mostrar_info_mercados(self, lista_users, lista_orders):
        choice2 = "2"
        while choice2 == "2":
            print("-------------------")
            largo = len(self.mercados_registrados)
            if largo > 0:
                print("Usted está registrado en los "
                  "siguientes mercados: ")
                for i in range (largo):
                    print(self.mercados_registrados[i].ticker)
                    choice2 = 0
                mercado_elegido = input("Elija el mercado"
                                        " del cual quiere "
                                        "ver información")
                mercado_elegido = int(mercado_elegido)
                mercado_elegido = self.mercados_registrados[
                    mercado_elegido]
            if largo == 0:
                print("Usted no está regitrado en ningun mercado")
        print("-------------------")

        contador = 0
        #Sumando todos los orders dentro de los usuarios
        for i in range(len(lista_users)):
            if mercado_elegido in lista_users[i].lista_users_id:
                contador += 1
        #Sumando orders sin usuarios dados en el .csv
        for i in range(len(lista_orders)):
            if lista_orders[i].ticker == mercado_elegido.name:
                contador +=1
        numero_orders = contador
        print("El numero de orders en el mercado" + str(
            mercado_elegido.name) +  "es de: " + numero_orders)

        #spread
        max = 999999999999999999999999
        min = 0
        contador_asks = 0
        contador_bids = 0

        #revisando los del csv
        for i in range(len(lista_orders)):
            if lista_orders[i].ticker == mercado_elegido.ticker:
                if lista_orders[i].tipo == "ask" and \
                            lista_orders[i].date_match == "Pending":
                    contador_asks +=1
                    if min >= lista_orders[i].price:
                        min = lista_orders[i].price
                if lista_orders[i].tipo == "bid" and \
                            lista_orders[i].date_match == "Pending":
                    contador_bids +=1
                    if  max <= lista_orders[i].price:
                        max = lista_orders[i].price
        spread = max - min
        print("El spread actual es de: " + str(spread))
        print("Hay " + str(contador_bids) + " bids en este mercado")
        print("Hay " + str(contador_asks) + " asks en este mercado")
        print("El ask best es de: " + str(min))
        print("El bid best es de: " + str(max))
        print("El match más alto fue de: ")
        print("El match más bajo fue de: ")


    def transferencia(self, lista_users):
        usuario2 = input("Escriba el nombre de usuario"
                         " a quien desea trasnferirle"
                         " criptomonedas: ")
        if Users.revisar_si_en_sistema(usuario2, lista_users) == True:
            for i in range(len(lista_users)):
                if lista_users[i].username == usuario2:
                    usuario2 = lista_users[i]
            for i in range(len(self.cantidad_moneda)):
                print(str(i) + " "+ str(self.cantidad_moneda[i]))
            moneda_transferencia = input("Elija la moneda que"
                                         " quiere transferir: ")
            moneda_transferencia = int(moneda_transferencia)
            monto_transferencia = float(input("Cuanto de esta moneda"
                                              " quiere transferir: "))
            #Sacandole al dueño
            cantidad = float(self.cantidad_moneda[i][1])
            cantidad = cantidad - monto_transferencia
            if cantidad < 0:
                print("No tiene suficiente saldo")
                self.transferencia(lista_users)
            self.cantidad_moneda[moneda_transferencia] = \
                (self.cantidad_moneda[moneda_transferencia][0],
                                                    cantidad)

            #entregando al destinatario
            for i in range(len(usuario2.cantidad_moneda)):
                if self.cantidad_moneda[moneda_transferencia] ==\
                        usuario2.cantidad_moneda[i]:
                    cantidad2 = usuario2.cantidad_moneda[i][1]
                    cantidad2 = cantidad2 + monto_transferencia
                    usuario2.cantidad_moneda[i] = \
                        (usuario2.cantidad_moneda[0], cantidad2)
                else:
                    #se crea la moneda en el usuario
                    usuario2.cantidad_moneda.append(
                        (self.cantidad_moneda[moneda_transferencia],
                         cantidad))
            print("Su transferencia se ha hecho con exito")

        else:
            print("Usuario no existe")
            print("Probemos nuevamente")
            self.transferencia(lista_users)


class Orders:
    def __init__(self, order_id, date_created,
                 date_match, amount, price, tipo, ticker):
        self.order_id = order_id
        self.date_created = date_created
        self.date_match = date_match
        self.amount = amount
        self.price = price
        self.tipo = tipo
        self.ticker = ticker
        self.mercado = object

    def __repr__(self):
        return "Id: " + str(self.order_id) + \
               " - Cantidad: " + str(self.amount) + \
               " - Precio: " + str(self.price)


class Currencies:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.cantidad = int

    def __repr__(self):
        cosa = str(self.name) + " (" + str(self.symbol) + ")"
        return cosa

    def Salir():
        pass


class Mercado:
    def __init__(self, ticker, asks, bids):
        self.ticker = ticker
        self.asks = asks
        self.bids = bids
        self.mon1 = object
        self.mon2 = object
        self.match = []

    def mostrar_mercado(self):
        print("-------------------")
        print("El mercado " + str(self.ticker) + ": ")
        print("Asks")
        self.asks.sort(key = operator.attrgetter('price'))
        self.bids.sort(key = operator.attrgetter('price'))

        for i in range(len(self.asks)):
            print(self.asks[i])
        print("-------------------")
        print("Bids")
        for i in range(len(self.bids)):
            print(self.bids[i])

    def poblar_mercado(lista_users, lista_orders, lista_mercados):
        for i in range(len(lista_mercados)):
            #lista_mercados[i] nos da el ticker de cada mercado
            #revisamos todos los mercados
            mer = lista_mercados[i]
            for j in range(len(lista_users)):
                persona = lista_users[j]
                if len(persona.orders) > 0:
                    for k in range(len(persona.orders)):
                        if persona.orders[k].tipo == "ask":
                            mer.asks.append(persona.orders[k])
                        if persona.orders[k].tipo == "bid":
                            mer.bids.append(persona.orders[k])


            #Cada mercado poblado con todos sus asks y bids
        return lista_mercados

    def revisar_si_match(self, lista_users):
        for i in range(len(self.asks)):
            for j in range(len(self.bids)):
                if self.asks[i].price <= self.bids[j].pric and \
                                self.asks[i].categoria == "Pending" and \
                                self.bids[j].categoria == "Pending":
                    print("Se produjo un nuevo match!")
                    order_a = self.asks[i].order_id
                    order_b = self.bids[j].order_id
                    user_a = self.retorna_usuario(order_a, lista_users)
                    user_b = self.retorna_usuario(order_b, lista_users)
                    mon1 = self.mon1
                    mon2 = self.mon2

                    if self.asks[i].amount < self.bids[j].amount:
                        cantidad_transada = self.asks[i].amount
                        self.bids[j].amount = int(
                            self.asks[i].amount) - int(
                            self.bids[j].amount)
                        self.asks[i].categoria = "Match"

                    if self.asks[i].amount > self.bids[j].amount:
                        cantidad_transada = self.bids[j].amount
                        self.asks[i].amount = int(
                            self.bids[j].amount) - int(
                            self.asks[i].amount)
                        self.bids[j].categoria = "Match"

                    self.ajustar_saldo_ask(user_a, mon2,
                                           cantidad_transada)
                    self.ajustar_saldo_bid(user_b, mon1,
                                           cantidad_transada)


    def retorna_usuario(self, order_number, lista_users):
        for i in range(len(lista_users)):
            if order_number in lista_users[i].orders:
                return lista_users[i]

    def ajustar_saldo_ask(self,user,moneda,order_a):
        for i in range(len(user.cantidad_moneda)):
            if user.cantidad_moneda[i][0] == moneda:
                cantidad_i = user.cantidad_moneda[i][1]
                cantidad_i = cantidad_i + (float(order_a.price)
                                           * float(order_a.amount))
                user.cantidad_moneda[i] = (moneda, cantidad_i)

    def ajustar_saldo_bid(self,user,moneda,order_b):
        for i in range(len(user.cantidad_moneda)):
            if user.cantidad_moneda[i][0] == moneda:
                cantidad_i = user.cantidad_moneda[i][1]
                cantidad_i = cantidad_i + (float(order_b.price)
                                           * float(order_b.amount))
                user.cantidad_moneda[i] = (moneda, cantidad_i)

    def consultas_generales(self, lista_users, lista_mercados):
        pass





