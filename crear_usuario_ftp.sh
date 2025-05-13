#!/bin/bash

# Verificar si se pasó un argumento
if [ -z "$1" ]; then
    echo "❌ Error: Debes proporcionar un nombre de usuario."
    echo "Uso: $0 nombre_usuario"
    exit 1
fi

# Variables
USUARIO=$1
DIRECTORIO="server-ftp/ftp-users/$USUARIO"

# Crear el directorio si no existe
if [ -d "$DIRECTORIO" ]; then
    echo "⚠️ El directorio $DIRECTORIO ya existe."
else
    sudo mkdir -p "$DIRECTORIO"
    echo "✅ Carpeta $DIRECTORIO creada exitosamente."
fi

# Asignar permisos 777
sudo chmod 777 "$DIRECTORIO"
echo "🔓 Permisos 777 asignados correctamente a $DIRECTORIO."