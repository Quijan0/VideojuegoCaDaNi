import mysql.connector

# Conectar a la base de datos
db = mysql.connector.connect(user='rootq', password='12345', host='localhost', database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

class Ranking:
    def __init__(self):
        self.ranking = {}

    def agregar_jugador(self, jugador, puntuacion):
        self.ranking[jugador] = puntuacion

    def actualizar_puntuacion(self, jugador, puntuacion):
        self.ranking[jugador] = puntuacion

    def consultar_puntuacion(self, jugador):
        return self.ranking[jugador]

    def consultar_ranking(self):
        return sorted(self.ranking.items(), key=lambda x: x[1], reverse=True)

# Crear un ranking
ranking = Ranking()

# Agregar jugadores al ranking
ranking.agregar_jugador("Jugador 1", 100)
ranking.agregar_jugador("Jugador 2", 50)

# Actualizar puntuación de un jugador
ranking.actualizar_puntuacion("Jugador 1", 150)

# Consultar puntuación de un jugador
print(ranking.consultar_puntuacion("Jugador 1"))

# Consultar ranking
print(ranking.consultar_ranking())