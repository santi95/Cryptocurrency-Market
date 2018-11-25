# Explicación Tarea

## Santiago Muñoz Venezian; santi95

28 de agosto, 2017

Mi tarea tiene 3 modulos.

    1.Importador

    2.T01

    3.Menu

Partiremos explicando el 1. "importador.py"
-------------------------------------------

En estas funciones se importan los datos de todos los archivos (.csv),
cree listas con todos los usuarios, orders y currencies.

En el caso de los usuarios tuve que transformar el string de las orders por usuario
por una lista de python en la parte baja de a función. Desde la linea 50 hasta la 57.
Se hizo lo pedido de que sin importar el orden con el cual nos den los datos,
el programa pueda leerlo correctamente y crear los objetos de forma eficiente.

En la función "crear_lista_users" no solamente meti a todos los usuarios del users.csv
en una lista, sino que también le di la categría "Pending" o "Match" a cada uno de los
orders dentro de la lista de orders pertenecientes a cada usuario.

Más abajo en la funcion crear_lista_mercados (linea 112) hice una lista de todos
los posibles tickers, los meti en una lista y luego cree los mercados como objetos
que tienen como atributos las monedas que pertenecen a él y sus asks y bids que son
insertados más adelante en el codigo.

Converti todas las variables en globales y las importe desde los otros 2 archivos.

Seguimos con el 2. "Menu.py"
----------------------------

Para que el programa no corra demasiado rápido hice una función variable_espera()
que detiene el programa para que puedas leer la informacón pedida con calma,
en vez de subir en la consola a leer lo pedido.

"main_menu()" es la función que te permite registrar un nuevo usuario o iniciar sesión.
Luego hay un register_menu que verifica que no se repitan los nombres de usuarios
y que cada user este bien creado, osino no te deja crearlo.
Después está el "sign_in_menu" que es la que redirige todo lo pedido por el programa
a diversas funciones dentro de los modulos.
Desplega opciones del 1 al 12

Intenté minimizar las veces que un usuario tenia que poner un input de una forma
muy especifica, por lo tanto, las primeras 3 funciones son muy de presionar tu
opción con un número. Es muy intuitivo registrarse en un mercado, que te muestre tus
mercados registrados y que te muestre la lista de mercados disponibles.

No tuve tiempo para registrar cada user en mercados en los cuales tenia orders pasadas

"choice_12" guarda en los mismos .csv creados por ustedes toda la nueva información
pero con un orden especifico, que despúes mi programa sabe interpretarlo para
volver a abrirlo.

Desde la choice 4 hasta la 10, era poco práctico hacerlos en el mismo módulo,
por lo tanto cree el modulo T01

Seguimos con el 3. "T01.py"
---------------------------
Este archivo es el más largo de todos.
algunas lineas quedaron desordenadas, debido a tener que respetar el largo del
pep8.

Aquí está definidas todas las clases.

### Partimos con la de Users

Cuenta con:

1. una lista de mercados registrados
2. una lista que tiene tuplas (el objeto moneda, cantidad de la moneda)
3. una lista de monedas para simplificar una parte del codigo
4. un atributo que nos dice si es o no un investor

Son todos Traders por default a menos que se categorice diferente.

La clase tiene una serie de funciones:

1. agregar_mercado:

Revisa si el usuario ya está registrado en el mercado y si no lo está lo agrega,
tomando en cuenta la categría del usuario

2. revisar_si_en_sistema:

Es para el login, si el usuario está dentro del csv puede hacer login, sino
intenta nuevamente o puede crear un nuevo usuario.

3. categorizar:

Le da una categoría a cada user, underage, trader o investor

4. crear_ask:

Crea el objeto order con los atributos pedidos al usuario en la consola,
revisa si tiene saldo suficiente, agrega el order a la lista de asks en el mercado
correspondiente y luego revisa si se hizo un nuevo match con la función
al final de esta función llamada revisar_si_match que está definida en la clase
Mercados.

Al crear el ask, el sistema le quita el saldo que intenta vender.

5. crear_bid

Es muy similar a la anterior

6. mostrar_orders

Primero sabe tu categoría para ver cuantos días para atras te puede mostrar,
te recuerda el formato de fecha y lo intenta convertir a una fecha que el sistema
entiende, sino te dice que lo intentes nuevamente. Luego la función toma
la fecha desde la cual quieres ver tus orders y te las muestra todas, independiente
de su estado

7. mostrar_activas

Te muestra tus orders que todavía no hacen match, aprovecha el order.categoria del
archivo importador para definir cuales están activas.

8. mostrar_info_mercados

Estan casi todas, pero los ultimos 2 que eran muy faciles de hacer por la forma en
la que está construido mi programa

9. transferencia

encuentra los usuarios, los saldos de cada moneda y revisa si tiene lo suficiente
para transferir. No pude sacarles la comisión, me sentía mal estafandolos, ya que
las criptomonedas son para evitar las comisiones (Mentira, no alcancé). Al final
de la función actualiza saldos.

### Seguimos con la clase Orders

No tiene funciones mas que las como representar un order cuando es impreso

### Seguimos con la clase Currencies

Lo mismo que la clase Orders, solo una

### Clase Mercado

tiene varias funciones también.

1. mostrar_mercado:

Donde debi haber puesto que las personas que tenian orders en cada mercado
quedaran automaticamente inscritas, pero no sabía si el magnate les regalaba plata
en esas condiciones

2. poblar_mercado:

Ingresa los asks y los bids de los usuarios al mercado para armar el sistema

3. revisar_si_match:

El nombre lo dice, revisa si es posible hacer un match y la llama cada vez que
se hace un nuevo order en el mercado.
Revisa que si una transacción es parcial, no la saque de las orders pendientes, sino
que solo altera la cantidad, mietras que la que si se completa la marca como match

4. retorna_usuario

Para hacer más linda la función del match, en vez de ponerme a buscar los
usuarios que hacen match con un "for"

5. ajustar_sueldo_ask

Ajusta saldos luego de realizar el ask

6. ajustar_sueldo_bid

Lo mismo pero para la parte bid del match

7. consultas_generales

No alcancé pero esta todo lindamente armado para poder crearlo.

Espero haberte ayudado con el .md!
Todo en general corre bastante bien, algunos errores de inputs no los corregí
y no pude programar matches simultaneos, pero me gustó la tarea y siento que
la tengo bien avanzada!

Intenté armar esto para que no pierdas tiempo intentando ver cual llama a cual
y que hace cada una.

Saludos
Gracias!!



