#Objeto partido
class Partido:
    #Función de inicializacion del objeto
    def __init__(self, fecha, Estadio, team_local, team_visitante, marcador_team_local,
                 marcador_team_visitante):

        self.fecha = fecha
        self.Estadio = Estadio
        self.team_local = team_local
        self.logo_team_local = team_local + '.jpg'
        self.team_visitante = team_visitante
        self.logo_team_visitante = team_visitante + '.jpg'
        self.marcador_team_local = marcador_team_local
        self.marcador_team_visitante = marcador_team_visitante

    #Funcion para obtener el ganador de un partido segun el marcador
    def obtener_ganador(self):
        if self.marcador_team_local == self.marcador_team_visitante:  
            return 'Empate'
        elif self.marcador_team_local > self.marcador_team_visitante:  
            return self.team_local
        else:  
            return self.team_visitante

    #Funcion por si queremos imprimir en un fomato más visual la información de un partido
    def __str__(self):
        return "{} {} {}|{}| vs {} |{}| --> [{}-{}] *Ganador: {}*".format(self.fecha,
                                                                  self.Estadio,
                                                                  self.team_local,
                                                                  self.logo_team_local,
                                                                  self.team_visitante,
                                                                  self.logo_team_visitante,
                                                                  self.marcador_team_local,
                                                                  self.marcador_team_visitante,
                                                                  self.obtener_ganador())


#Objeto jornada
class Jornada:
    #Función de inicializacion del objeto
    def __init__(self, id, partidos):
        self.id = id
        self.partidos = partidos
    #Funcion para imprimir los datos de una jornada mas visuales
    def __str__(self):
        return "Jornada {}\n{}".format(self.id, "\n".join(
            [str(partido) for partido in self.partidos]))


#objeto liga
class Liga:
    #Función de inicializacion de objeto
    def __init__(self, temporada, jornadas):
        self.temporada = temporada
        self.jornadas = jornadas
    #Funcion para imprimir los datos de la liga mas visuales
    def __str__(self):
        return "Liga {}\n{}".format(self.temporada, "\n".join(
            [str(jornada) for jornada in self.jornadas]))


