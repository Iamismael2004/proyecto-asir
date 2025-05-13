# Proyecto ASIR

## Descripcion

## Instrucciones
Ir a config.env y adaptar variables
Revisar dhcpd.conf
Revisar ficheros dns (named conf y zone)

Lanzar configurar.sh

## Comandos docker compose

- Para lanzar todos los contenedores con docker compose (sustituir config.env) por el fichero que queramos...
`docker compose --env-file config.env up -d`

- Para pararlo
`docker compose down`

## Arrancar
`./lanzar.sh`

## Parar
`./parar.sh`

### Utilidades LDAP
- Para generar un fichero de estructura de usuarios, grupos, etc (se puede usar la plantilla base estructura_template.ldif)

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

### Comprobar resolucion DNS
nslookup name_to_search dns_ip_server
nslookup impresora.instituto.lan 10.0.2.10

### Creacion de usuarios
Cuando se cree un usuario en ldap, debemos crear su usuario en ftp
Podemos usar el script crear_usuario_ftp.sh
`./crear_usuario_ftp.sh <nombre_usuario>`

## Autores
- Ismael Ahumada