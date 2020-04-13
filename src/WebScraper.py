import os
import sys
import time
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen

from objetos import Partido, Jornada, Liga

url_pagina = "http://www.resultados-futbol.com/premier{}/grupo1/calendario"
AñoInicio = 2000
AñoFin = 2020
nombre_carpeta_logos = 'logos'
f = open('PremierLeague.csv', "w", encoding="utf8")


def Obtener_logo(nombre_team, src):
    path = '%s/%s.jpg' % (nombre_carpeta_logos, nombre_team)
    if not os.path.isfile(path):
        txt = open(path, "wb")
        img = urlopen(src)
        txt.write(img.read())
        txt.close()

def Obtener_jornada(paquete):
    partidos = []
    id = paquete.find('span', attrs={'class': 'titlebox'}).text.split()[-1]
    trs = paquete.tbody.find_all('tr')
   
    for tr in trs:
        Partido = Obtener_Partido(tr)
        partidos.append(Partido)
    return Jornada(id, partidos)

def Obtener_Partido(tr):
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

    return Partido(fecha, Estadio, team_Local, team_Visitante, marcador_team_Local, marcador_team_Visitante)


def Obtener_jornadas(temporada):
    jornadas = []
    url = url_pagina.format(temporada)
    print("usando:", url)

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    try:
        page = urlopen(req)
    except:
        print('Algo ha pasado obteniendo los datos')
        sys.exit(-1)

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
                #print(jornada)
            except Exception:
                print("Exception")
                break
    except Exception:
        print(
            soup.find('div', attrs={'class': 'ld-infohistorical'}).text.strip())
    return jornadas



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





def directorio_logos():
    if not os.path.isdir(nombre_carpeta_logos):
        os.makedirs(nombre_carpeta_logos)


def obtener_informacion():
    directorio_logos()
    for i in range(AñoInicio, AñoFin):
        print("Temporada", str(i-1) + "/"+ str(i))
        LigaAtr = Liga(i, Obtener_jornadas(i))
        TemporadaLiga_csv(LigaAtr)
        time.sleep(10)

def main():
    print("Resultados de futbol de la premier league' información de https://www.resultados-futbol.com/ ")
    
    # Start timer
    start_time = time.time()  
    print("Este proceso empieza: " + time.asctime( time.localtime(time.time())))
    obtener_informacion()
    #End Timer
    end_time = time.time()
    print("Este proceso acaba: " + time.asctime(time.localtime(time.time())))

    # Tiempo transcurrido
    print("\n tiempo transcurrido: " + \
            str(round(((end_time - start_time) / 60) , 2)) + " minutos")
    

def Scrape():
    print("Temporada,jornada,fecha,estadio,teamLocal,logo_teamLocal,teamVisitante,logo_teamVisitante,Marcador_TeamLocal,Marcador_TeamVisitante,Ganador_Partido",file=f)
    main()
    f.close()
                



