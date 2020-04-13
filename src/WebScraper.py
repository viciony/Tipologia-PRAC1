import os
import sys
import time
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen

from objetos import Partido, Jornada, Liga

#Constantes de nuestro fichero, se podria generar un fichero para asi que fuera más fácil modificar sin tener que modificar código pero se obvia ya que no es necesario para dicha práctica.
url_pagina = "http://www.resultados-futbol.com/premier{}/grupo1/calendario"
AñoInicio = 2000
AñoFin = 2020
nombre_carpeta_logos = 'logos'
f = open('PremierLeague.csv', "w", encoding="utf8")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'

#Función donde guardamos la imagen del logo, con el nombre del equipo
def Obtener_logo(nombre_team, src):
    path = '%s/%s.jpg' % (nombre_carpeta_logos, nombre_team)
    #Comprobamos si ya existe dicho logo sino no lo guardamos
    if not os.path.isfile(path):
        txt = open(path, "wb")
        img = urlopen(src)
        txt.write(img.read())
        txt.close()

#Función que devuelve una jornada en concreto de la liga
def Obtener_jornada(paquete):
    #Array de partidos de la jornada
    partidos = []

    #Numero de la jornada
    id = paquete.find('span', attrs={'class': 'titlebox'}).text.split()[-1]
    #Obtenemos todos los partidos de la jornada
    trs = paquete.tbody.find_all('tr')
    #Recorremos los tags de los partidos de la jornada y vamos agregando los partidos al array y llamamos as la función de otro fichero donde definimos la estructura de nuestro objeto Jornada, al igual que la función
    #Obtener_partido que nos devuelve un objeto Partido
    for tr in trs:
        Partido = Obtener_Partido(tr)
        partidos.append(Partido)
    return Jornada(id, partidos)

#Función que devuelve mediante el tag html los datos de un partido en concreto de la jornada
def Obtener_Partido(tr):
    #Recorremos los diferentes tags html de la información que queremos obtener
    fecha_td = tr.td
    teamLocal_td = fecha_td.find_next_sibling()
    marcador_td = teamLocal_td.find_next_sibling()
    teamVisitante_td = marcador_td.find_next_sibling()

    fecha = fecha_td.text.strip()
    Estadio = tr.find('span', attrs={'class': 'location'}).text.strip()
    team_Local = teamLocal_td.a.text.strip()
    Obtener_logo(team_Local, teamLocal_td.a.img['src'])
    team_Visitante = teamVisitante_td.a.text.strip()
    Obtener_logo(team_Visitante, teamVisitante_td.a.img['src'])
    marcador = marcador_td.a.text
    if marcador_td.find('-') == -1:
        raise Exception("El simbolo '-' no se ha encontrado!")
    marcador_team_Local = marcador.split('-')[0].strip()
    marcador_team_Visitante = marcador.split('-')[1].strip()

    #Devolvemos el objeto partido pasandole asi los datos obtenidos del tag, para que asi nos devuelva el objeto deseado.
    return Partido(fecha, Estadio, team_Local, team_Visitante, marcador_team_Local, marcador_team_Visitante)

#Funcón que nos devuelve todas las jornadas de una temporada
def Obtener_jornadas(temporada):
    #Array de jornadas
    jornadas = []
    #Obtenemos la url de la cual extraeremos la información deseada y la mostramos
    url = url_pagina.format(temporada)
    print("usando:", url)

    #Utilizamos nuestro user agent definido en las costantes para simular un navegador web 
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    try:
        page = urlopen(req)
    except:
        print('Algo ha pasado obteniendo los datos')
        sys.exit(-1)

    #Utilizamos beautifulSoup para el tratamiento del HTML, además de controlar la obtención de las jornadas por si hubiera fallos en las peticiones.
    soup = BeautifulSoup(page.read(), "html.parser")
    try:
        Paquete_jornadas = soup.find('div',
                                        attrs={'class': 'b2col-container'})
        cajas = Paquete_jornadas.find_all('div',
                                             attrs={'class': 'boxhome-2col'})

        for caja in cajas:
            try:
                jornada = Obtener_jornada(caja)
                jornadas.append(jornada)
            except Exception:
                print("Exception")
                break
    except Exception:
        print(
            soup.find('div', attrs={'class': 'ld-infohistorical'}).text.strip())
    return jornadas


#Función que graba los datos de cada temporada en nuestro fichero csv.
def TemporadaLiga_csv(liga):
    for jornada in liga.jornadas:
        for partido in jornada.partidos:
            print(
                "{},{},{},{},{},{},{},{},{},{},{}".format(liga.temporada,
                                                             jornada.id,
                                                             partido.fecha,
                                                             partido.Estadio,
                                                             partido.team_local,
                                                             partido.logo_team_local,
                                                             partido.team_visitante,
                                                             partido.logo_team_visitante,
                                                             partido.marcador_team_local,
                                                             partido.marcador_team_visitante,
                                                             partido.obtener_ganador()),
                file=f)




#Función que nos mira si existe nuestra carpeta de logos sino nos la crea
def directorio_logos():
    if not os.path.isdir(nombre_carpeta_logos):
        os.makedirs(nombre_carpeta_logos)

#Función que inicia la obtención del periodo de temporadas deseado
def obtener_informacion():
    directorio_logos()
    for i in range(AñoInicio, AñoFin + 1):
        print("Temporada", str(i-1) + "/"+ str(i))
        LigaAtr = Liga(str(i-1) + "/"+ str(i), Obtener_jornadas(i))
        print(LigaAtr)
        TemporadaLiga_csv(LigaAtr)
        #Waiter para no saturar el servidor de 10 segundos
        time.sleep(10)

    
#Función principal que inicia todo el proceso
def Scrape():    
    print("Temporada,jornada,fecha,estadio,teamLocal,logo_teamLocal,teamVisitante,logo_teamVisitante,Marcador_TeamLocal,Marcador_TeamVisitante,Ganador_Partido",file=f)
    print("Resultados de futbol de la premier league' información de https://www.resultados-futbol.com/ ")
    
    # Start timer para tener controlado el tiempo que dura la ejecución del web scrapper
    start_time = time.time()  
    print("Este proceso empieza: " + time.asctime( time.localtime(time.time())))
    obtener_informacion()
    #End Timer
    end_time = time.time()
    print("Este proceso acaba: " + time.asctime(time.localtime(time.time())))

    # Tiempo transcurrido
    print("\n tiempo transcurrido: " + \
            str(round(((end_time - start_time) / 60) , 2)) + " minutos")
    f.close()
                



