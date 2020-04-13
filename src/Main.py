import argparse
import csv
import os

FileCsv = "PremierLeague.csv"

parser = argparse.ArgumentParser(description='Scrapper para obtener los datos de futbol.')
parser.add_argument('--csv_data', help='Obtener los datos si el csv ya existe', action='store_true')
args = parser.parse_args()

if not args.csv_data:
    from WebScraper import Scrape
    Scrape()
else:
    if os.path.isfile(FileCsv):
            with open(FileCsv, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    print(', '.join(row))
    else:
        print("El archivo no existe para usar esta opcion")
