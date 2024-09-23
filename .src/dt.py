class Futbolista:  #Definimos la clase del Futbolista Base
    def __init__(self, numero_de_camiseta, apellido, posicion, minutos_jugados):
        self.numero_de_camiseta = numero_de_camiseta
        self.apellido = apellido
        self.posicion = posicion
        self.minutosJugados = minutos_jugados

    def mostrar_estadisticas(self):
        return f"{self.apellido} (Camiseta {self.numero_de_camiseta}) - Posición: {self.posicion}, Minutos jugados: {self.minutosJugados}"


class Arquero(Futbolista): #Definimos la clase del Arquero (hereda de Futbolista)
    def __init__(self, numero_de_camiseta, apellido, minutos_jugados):
        super().__init__(numero_de_camiseta, apellido, 'Arquero', minutos_jugados)


class Jugador(Futbolista): #Definimos la clase del Jugador (hereda de Futbolista)
    def __init__(self, numero_de_camiseta, apellido, posicion, minutos_jugados, goles):
        super().__init__(numero_de_camiseta, apellido, posicion, minutos_jugados)
        self.goles = goles

    def mostrar_estadisticas(self):
        return f"{super().mostrar_estadisticas()}, Goles: {self.goles}"


class Defensor(Jugador): #Definimos las clases de los Jugadores, heredan de Jugador
    def __init__(self, numero_de_camiseta, apellido, minutos_jugados, goles=0):
        super().__init__(numero_de_camiseta, apellido, 'Defensor', minutos_jugados, goles)


class Mediocampista(Jugador):
    def __init__(self, numero_de_camiseta, apellido, minutos_jugados, goles=0):
        super().__init__(numero_de_camiseta, apellido, 'Central', minutos_jugados, goles)


class Delantero(Jugador):
    def __init__(self, numero_de_camiseta, apellido, minutos_jugados, goles):
        super().__init__(numero_de_camiseta, apellido, 'Delantero', minutos_jugados, goles)


# Función para solicitar input con validación
def mensaje_obligatorio(mensaje):
    valor = input(mensaje)
    while not valor.strip():  # Requiere que no esté vacío
        valor = input("Por favor ingresar el siguiente dato -> " + mensaje)
    return valor


# Carga de datos.
def menu():
    equipo = []
    while True:
        print("_____________")
        print("1. Agregar Arquero")
        print("2. Agregar Defensor")
        print("3. Agregar Mediocampista")
        print("4. Agregar Delantero")
        print("5. Mostrar Equipo")
        print("6. Eliminar Jugador")
        print("7. Salir")
        print("_____________")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero_camiseta = mensaje_obligatorio("Número de camiseta: ")
            apellido = mensaje_obligatorio("Apellido: ")
            minutos_jugados = mensaje_obligatorio("Minutos jugados: ")
            equipo.append(Arquero(numero_camiseta, apellido, minutos_jugados))

        elif opcion == '2':
            numero_camiseta = mensaje_obligatorio("Número de camiseta: ")
            apellido = mensaje_obligatorio("Apellido: ")
            minutos_jugados = mensaje_obligatorio("Minutos jugados: ")
            goles = mensaje_obligatorio("Goles marcados: ")
            equipo.append(Defensor(numero_camiseta, apellido, minutos_jugados, goles))

        elif opcion == '3':
            numero_camiseta = mensaje_obligatorio("Número de camiseta: ")
            apellido = mensaje_obligatorio("Apellido: ")
            minutos_jugados = mensaje_obligatorio("Minutos jugados: ")
            goles = mensaje_obligatorio("Goles marcados: ")
            equipo.append(Mediocampista(numero_camiseta, apellido, minutos_jugados, goles))

        elif opcion == '4':
            numero_camiseta = mensaje_obligatorio("Número de camiseta: ")
            apellido = mensaje_obligatorio("Apellido: ")
            minutos_jugados = mensaje_obligatorio("Minutos jugados: ")
            goles = mensaje_obligatorio("Goles marcados: ")
            equipo.append(Delantero(numero_camiseta, apellido, minutos_jugados, goles))

        elif opcion == '5':
            for jugador in equipo:
                print(jugador.mostrar_estadisticas())

        elif opcion == '6':
            if not equipo:
                print("No hay jugadores para eliminar.")
                continue

            print("Jugadores disponibles:")
            for jugador in equipo:
                print(jugador.mostrar_estadisticas())

            numero_camiseta = mensaje_obligatorio("Ingresar el numero de camiseta del jugador a eliminar: ")
            for jugador in equipo:
                if jugador.numero_de_camiseta == numero_camiseta:
                    equipo.remove(jugador)
                    print(f"Jugador {jugador.apellido} eliminado.")
                    break
            else:
                print("No se encontró ningún jugador con ese número de camiseta.")

        elif opcion == '7':
            break

        else:
            print("Opcion no válida, intentar de nuevo por favor.")

menu()
