# Usa la imagen oficial de Nginx como base
FROM nginx:1.27.4-alpine

# Crear el directorio donde se alojará la web
RUN mkdir -p /usr/share/nginx/pagina_web

# Copiar fichero de configuracion
COPY default.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80 y 443 (puertos por defecto de Nginx)
EXPOSE 80 443

# Ejecutar Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
