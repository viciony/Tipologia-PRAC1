import argparse
import csv
import os
#Fichero main ejecutor de nuestro proyecto


#Nombre de nuestro fichero dataset
FileCsv = "PremierLeague.csv"

#Creamos los argumentos que queremos utilizar
parser = argparse.ArgumentParser(description='Scrapper para obtener los datos de futbol.')
parser.add_argument('--csv_data', help='Obtener los datos si el csv ya existe', action='store_true')
args = parser.parse_args()

#Comprovamos que no se haya pasado ningun argumento, por lo tanto ejecutamos el web scraper, mediante la importación de una función de otro fichero.
if not args.csv_data:
    from WebScraper import Scrape
    Scrape()
#Sino es asi y se ha pasado argumento, csv_data. Miramos si existe el fichero, si es asi imprimimos su contenido sino avisamos de que no existe
else:
    if os.path.isfile(FileCsv):
            with open(FileCsv, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    print(', '.join(row))
    else:
        print("El archivo no existe para usar esta opcion")
