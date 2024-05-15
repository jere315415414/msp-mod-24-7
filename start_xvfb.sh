#!/bin/bash

# Iniciar Xvfb en el fondo
Xvfb :99 -screen 0 1024x768x16 &

# Esperar un momento para asegurarse de que Xvfb se inicie correctamente
sleep 2

# Exportar la variable DISPLAY
export DISPLAY=:99

# Ejecutar el script principal de Python
python3 /workspaces/msp-mod-24-7/server.py

