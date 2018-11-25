from T01 import Currencies, Users, Orders, Mercado
import io

def crear_lista_currencies():
    # Lista objetos de Currencies
    lista_currencies = [Currencies("DCCapital", "DCC")]
    data = io.open("Currencies.csv", encoding="latin-1")
    linea = data.readline()
    primera_linea = linea.strip()
    primera_linea = primera_linea.split(";")

    pos_name = primera_linea.index("name: string")
    pos_symbol = primera_linea.index("symbol: string")

    linea = data.readline()
    while linea != "":
        linea1 = linea.strip()
        linea2 = linea1.split(";")
        lista_currencies.append(Currencies(linea2[pos_name],
                                           linea2[pos_symbol]))
        linea = data.readline()
    data.close()

    return lista_currencies

# Lista de usuarios como objetos
def crear_lista_usuarios():
    lista_users = []
    data = io.open("users.csv", encoding="latin-1")
    linea = data.readline()
    primera_linea = linea.strip()
    primera_linea = primera_linea.split(";")

    pos_orders = primera_linea.index("orders: list")
    pos_birth = primera_linea.index("birthday: string")
    pos_username = primera_linea.index("username: string")
    pos_name = primera_linea.index("name: string")
    pos_lastname = primera_linea.index("lastname: string")

    linea = data.readline()
    while linea != "":
        linea1 = linea.strip()
        linea2 = linea1.split(";")
        lista_users.append(Users(linea2[pos_username],
                                 linea2[pos_name],
                                 linea2[pos_lastname],
                                 linea2[pos_birth],
                                 linea2[pos_orders]))
        linea = data.readline()
    #Convertimos el usuarios.orders en lista
    for i in range(len(lista_users)):
        lista_users[i].orders = lista_users[i].orders.split(":")

    for i in range(len(lista_users)):
        for j in range(len(lista_orders)):
            for k in range(len(lista_users[i].orders)):
                if lista_users[i].orders[k] == str(
                        lista_orders[j].order_id):
                    lista_users[i].orders[k] = lista_orders[j]
                    if lista_users[i].orders[k].date_match == "":
                        lista_users[i].orders[k].categoria = "Pending"
                    else:
                        lista_users[i].orders[k].categoria = "Match"

    for i in range(len(lista_users)):
        if lista_users[i].orders[0] == "":
            lista_users[i].orders = []



    data.close()

    # Les pone categoria a cada usuario
    for i in range(len(lista_users)):
        cosa = lista_users[i]
        cosa.categorizar()

    return lista_users

def crear_lista_orders():
    # Lista de Orders
    lista_orders = []
    data = io.open("orders.csv", encoding="latin-1")
    linea = data.readline()
    primera_linea = linea.strip()
    primera_linea = primera_linea.split(";")

    pos_id = primera_linea.index("order_id: int")
    pos_price = primera_linea.index("price: float")
    pos_datec = primera_linea.index("date_created: string")
    pos_type = primera_linea.index("type: string")
    pos_datem = primera_linea.index("date_match: string")
    pos_amount = primera_linea.index("amount: float")
    pos_ticker = primera_linea.index("ticker: string")

    linea = data.readline()
    while linea != "":
        linea1 = linea.strip()
        linea2 = linea1.split(";")
        lista_orders.append(Orders(linea2[pos_id],
                                   linea2[pos_datec],
                                   linea2[pos_datem],
                                   linea2[pos_amount],
                                   linea2[pos_price],
                                   linea2[pos_type],
                                   linea2[pos_ticker]))
        linea = data.readline()

    data.close()
    return lista_orders

def crear_lista_mercados():
    lista_mercados = []
    for i in range (len(lista_currencies)):
        for j in range (len(lista_currencies)):
            if i != j:
                ticker = str(lista_currencies[i].symbol) + \
                         str(lista_currencies[j].symbol)
                asks = []
                bids = []
                mer = Mercado(ticker, asks, bids)
                mer.mon1 = lista_currencies[i]
                mer.mon2 = lista_currencies[j]
                lista_mercados.append(mer)

    return lista_mercados

lista_orders = crear_lista_orders()
lista_users = crear_lista_usuarios()
lista_currencies = crear_lista_currencies()
lista_mercados_casi_final = crear_lista_mercados()
lista_mercados = Mercado.poblar_mercado(lista_users, lista_orders,
                                        lista_mercados_casi_final)
