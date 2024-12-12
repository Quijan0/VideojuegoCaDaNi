import mysql.connector
import datetime

# Conectar a la base de datos
db = mysql.connector.connect(user='rootq', password='12345', host='localhost', database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

class Nodo:
    def __init__(self, fecha, resultado):
        self.fecha = fecha
        self.resultado = resultado
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, fecha, resultado):
        if self.raiz is None:
            self.raiz = Nodo(fecha, resultado)
        else:
            self._agregar_nodo(self.raiz, fecha, resultado)

    def _agregar_nodo(self, nodo, fecha, resultado):
        if fecha < nodo.fecha:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(fecha, resultado)
            else:
                self._agregar_nodo(nodo.izquierda, fecha, resultado)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(fecha, resultado)
            else:
                self._agregar_nodo(nodo.derecha, fecha, resultado)

    def consultar_partidas(self):
        return self._consultar_partidas(self.raiz)

    def _consultar_partidas(self, nodo):
        if nodo is None:
            return []
        else:
            return self._consultar_partidas(nodo.izquierda) + [nodo.resultado] + self._consultar_partidas(nodo.derecha)

    def buscar_partida(self, fecha):
        return self._buscar_partida(self.raiz, fecha)

    def _buscar_partida(self, nodo, fecha):
        if nodo is None:
            return None
        elif fecha == nodo.fecha:
            return nodo.resultado
        elif fecha < nodo.fecha:
            return self._buscar_partida(nodo.izquierda, fecha)
        else:
            return self._buscar_partida(nodo.derecha, fecha)

# Crear un árbol binario
arbol = ArbolBinario()

# Agregar partidas al árbol
arbol.agregar_nodo(datetime.date(2022, 1, 1), "Partida 1")
arbol.agregar_nodo(datetime.date(2022, 1, 15), "Partida 2")
arbol.agregar_nodo(datetime.date(2022, 2, 1), "Partida 3")

# Consultar partidas
partidas = arbol.consultar_partidas()
print(partidas)

# Buscar partida
partida = arbol.buscar_partida(datetime.date(2022, 1, 15))
print(partida)