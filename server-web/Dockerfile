# Usa la imagen oficial de Nginx como base
FROM nginx:1.27.4-alpine

# Exponer el puerto 80 y 443 (puertos por defecto de Nginx)
EXPOSE 80 443

# Ejecutar Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
