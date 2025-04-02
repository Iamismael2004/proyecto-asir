# Usa la imagen oficial de Alpine como base
FROM alpine:3.18

# Instalar vsftpd
RUN apk update && \
    apk add vsftpd

RUN echo "seccomp_sandbox=NO" >> /etc/vsftpd/vsftpd.conf

# Exponer el puerto 21 (puerto por defecto de FTP)
EXPOSE 21

# Ejecutar vsftpd en primer plano
CMD ["vsftpd", "/etc/vsftpd/vsftpd.conf"]
