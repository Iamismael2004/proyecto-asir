# Proyecto ASIR

## Descripcion
- Pendiente de completar...

## Instrucciones
- Para lanzar todos los contenedores con docker compose (sustituir config.env) por el fichero que queramos...
`docker compose --env-file config.env up -d`


### Comandos utiles docker
- Para listar los contenedores corriendo
`docker ps`
- Para lanzar una sesion de terminal dentro de un contenedor
`docker exec -it <IDENTIFICADOR_CONTENEDOR> /bin/sh`
- - El identificador vale con poner las tres primeras letras o digitos
- - /bin/sh o /bin/bash (algunos contenedores no traen bash dentro)


## Autores
- Ismael Ahumadamar