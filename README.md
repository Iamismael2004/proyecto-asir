# Proyecto ASIR

## Descripcion
- Pendiente de completar...

## Instrucciones
- Para lanzar todos los contenedores con docker compose (sustituir config.env) por el fichero que queramos...
`docker compose --env-file config.env up -d`

- Para pararlo
`docker compose down`


### Comandos utiles docker
- Para listar los contenedores corriendo
`docker ps`
- Para lanzar una sesion de terminal dentro de un contenedor
`docker exec -it <IDENTIFICADOR_CONTENEDOR> /bin/sh`
- - El identificador vale con poner las tres primeras letras o digitos
- - /bin/sh o /bin/bash (algunos contenedores no traen bash dentro)
- Para ver logs generales de un contenedor:
`docker logs <IDENTIFICADOR_CONTENEDOR>`
- Para eliminar cosas (imagenes, contenedores, volumenes, etc) que no este usando docker:
`docker system prune -a`

## Autores
- Ismael Ahumada