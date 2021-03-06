# Práctica 1: Web scraping
## Miembros
-  La actividad se ha relizado individualmente por Joan Miquel Forteza Fuster

## Descripción de la práctica
<p ALIGN="justify">  Esta práctica de l'assignaatura M2-951 - Tipologia y ciclo de vida de los datos del Master universitario de Data Science, corresponde al desarrollo de un Web Scraper con finalidades academicas y de esta manera introducirse y profundizarse un poco en este grandioso mundo. </p>

<p ALIGN="justify"> Para la realización de nuestro Web Scrapper se ha elegido la página de http://www.resultados-futbol.com donde en esta página se recogen los resultados de los partidos de futbol de todas las ligas del mundo y es una página donde recoger un buen ejemplo de datos, en nuestro caso recogeremos los datos de la Premier League, a modo de ejemplo pero serviria para cualquier liga modificando la url de obtencion de datos y el nombre del fichero CSV de nuestro dataset. </p>

## Estructura de la práctica
### Estructura
<ul >
  <li>logos</li>
 <ul >
  <li>teamN.jpg</li>
   <li>...</li>
</ul>
  <li> src </li>
   <ul >
  <li>Main.py</li>
   <li>WebScraper.py</li>
     <li>Objetos.py</li>
</ul>
    <li> PremierLeague.csv </li>
    <li> jff826_TCVD_PRAC1.pdf </li>
    <li> README.md  </li>
    <li> dependencies.txt </li>
</ul>

### Descripción de la estructura
* logos --> Este apartado contiene los logos de los diferentes equipos de la premier
* src/Main.py --> Se utiliza para ejecutar y empezar la descarga de datos
* src/WebScraper.py --> Archivo python que contiene los metodos para genera el dataset de la información que queremos extraer
* src/Objetos.py --> Archivo python donde definimos los objetos que vamos a usar y funciones para tratarlos
* PremierLeague.csv --> Dataset generado en formato csv
* jff826_TCVD_PRAC1.pdf --> Documentación de la práctica.
* dependencies.txt --> Librerias necesarias poder ejecutar el web scrapper.

## Ejecución del Web Scrapper
```shell
#Instalamos las dependencias de nuestro proyecto con el archivo de dependencias
pip install -r dependencies.txt 

#Ejecutamos el main de nuestro web scrapper
python src/Main.py [--csv_data]
```

- El argumento csv_data nos imprimira por consola si ya hemos descargado el archivo para asi evitar tener que hacer otra vez las peticiones solo si existe el fichero, nos mirara si tenemos los datos en ese caso y los imprimirá mostrandonos asi la información sin realizar petición ningúna.

## Recursos
- Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
- Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC. PID_00256968.pdf
- Teguayaco Gutiérrez González, Web scrapiing aviation accidents https://github.com/tteguayco/Web-scraping-aviation-accidents

## Zenodo
Aqui se deja el <a href="https://zenodo.org/record/3750180#.XpS5evgzYZA">link</a> a Zenodo donde esta publicado el dataset y se puede ver una previsualización.

## Licencia
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">licencia de Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional</a>.

