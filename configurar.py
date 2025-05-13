#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para reemplazar marcadores en archivos template
Lee las variables de config.env y las aplica a archivos *_template.*
"""

import os
import sys
import re
import glob
from pathlib import Path

def load_config(config_file="config.env"):
    """Carga las variables del archivo config.env"""
    
    if not os.path.exists(config_file):
        print(f"❌ Error: El archivo {config_file} no existe")
        sys.exit(1)
    
    config_vars = {}
    print("🔄 Cargando variables de configuración...")
    
    with open(config_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Ignorar líneas vacías o comentarios
            if not line or line.startswith('#'):
                continue
            
            # Dividir en clave y valor
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Comprobar si está vacía
                if not value:
                    print(f"⚠️  Advertencia: La variable {key} está vacía.")
                
                config_vars[key] = value
                print(f"  - Cargada variable: {key} -> {value}")
    
    return config_vars

def process_template(template_file, config_vars):
    """Procesa un archivo template reemplazando marcadores con valores"""
    
    # Determinar el nombre del archivo de salida (quitando "_template" del nombre)
    path = Path(template_file)
    dir_name = path.parent
    base_name = path.name
    
    # Reemplazar '_template' en el nombre del archivo
    output_name = base_name.replace('_template', '', 1)
    
    # Si no se hizo ningún cambio, el formato es incorrecto
    if output_name == base_name:
        print(f"❌ Error: El archivo {template_file} no sigue el formato *_template.*")
        return
    
    output_file = dir_name / output_name
    print(f"🔄 Procesando {template_file} -> {output_file}")
    
    try:
        # Leer el contenido del archivo template
        with open(template_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Realizar reemplazos para cada variable
        for key, value in config_vars.items():
            k = "${" + key + "}"
            content = content.replace(k, value)
        
        # Escribir el resultado al archivo de salida
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Archivo procesado: {output_file}")
    
    except Exception as e:
        print(f"❌ Error al procesar {template_file}: {str(e)}")

def main():
    """Función principal del script"""
    
    # Cargar configuración
    config_vars = load_config()
    
    # Buscar todos los archivos con el patrón *_template.*
    print("🔎 Buscando archivos de plantilla...")
    template_files = glob.glob("**/*_template.*", recursive=True)
    
    # Verificar si se encontraron archivos de plantilla
    if not template_files:
        print("❌ No se encontraron archivos de plantilla (*_template.*)")
        sys.exit(0)
    
    # Procesar cada archivo de plantilla
    print("🔄 Iniciando procesamiento de plantillas...")
    for template in template_files:
        process_template(template, config_vars)
    
    print("✅ Proceso completado.")

if __name__ == "__main__":
    main()