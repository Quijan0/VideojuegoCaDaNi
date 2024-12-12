import mysql.connector

# Conectar a la base de datos
db = mysql.connector.connect(user='rootq', password='12345', host='localhost', database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

class Equipo:
    def __init__(self, nombre, estadisticas):
        self.nombre = nombre
        self.estadisticas = estadisticas

    def agregar_jugador(self, jugador):
        self.estadisticas[jugador] = {"puntuacion": 0, "partidas_jugadas": 0}

    def actualizar_estadisticas(self, jugador, puntuacion, partidas_jugadas):
        self.estadisticas[jugador]["puntuacion"] = puntuacion
        self.estadisticas[jugador]["partidas_jugadas"] = partidas_jugadas

    def consultar_estadisticas(self, jugador):
        return self.estadisticas[jugador]

# Crear un equipo
equipo = Equipo("Equipo A", {})

# Agregar jugadores al equipo
equipo.agregar_jugador("Jugador 1")
equipo.agregar_jugador("Jugador 2")

# Actualizar estadísticas de un jugador
equipo.actualizar_estadisticas("Jugador 1", 100, 5)

# Consultar estadísticas de un jugador
print(equipo.consultar_estadisticas("Jugador 1"))