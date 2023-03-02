# nodes-demo

Una aplicación sencilla que por el momento muestra algunos nodos. Basada en este [tutorial](https://towardsdatascience.com/how-to-visualize-a-social-network-in-python-with-a-graph-database-flask-docker-d3-js-af451db57330) 

Para inicializar la aplicación se necesita instalar *Docker-Compose*.

Primero escriba el comando:
```
docker-compose build
```
Esto instalara todas las dependencias necesarias en un docker.
Tardara unos segundos en construirse. Una vez hecho esto escriba el comando:
```
docker-compose up
```
Una vez el docker este arrancado, dirigase a `http://localhost:5000/`. Se mostraran los nodos y podra interactuar con ellos.