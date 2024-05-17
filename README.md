
Configuración del Servidor de Minecraft
Este tutorial te guiará a través del proceso de hacer un fork de este repositorio, clonar el repositorio, instalar dependencias, ejecutar el script en Python y configurar UptimeRobot para mantener el servidor activo.

Paso 1: Crear un Fork del Repositorio
Visita este repositorio en GitHub:

Ve a la página de este repositorio en GitHub.
Haz clic en el botón de Fork:

En la parte superior derecha de la página, haz clic en el botón de "Fork".
Selecciona tu cuenta:

Selecciona tu cuenta personal o la organización donde deseas crear el fork del repositorio.
Paso 2: Clonar el Repositorio Forkeado
Ve al repositorio forkeado:

Después de hacer el fork, serás redirigido a tu copia del repositorio.
Clona el repositorio:

Copia la URL del repositorio (usa el botón de "Code" y selecciona HTTPS o SSH).

Abre una terminal en tu computadora y ejecuta el siguiente comando, reemplazando URL_DEL_REPOSITORIO con la URL que copiaste:


git clone URL_DEL_REPOSITORIO
Navega al directorio del repositorio:

bash

cd mi-servidor-minecraft
Paso 3: Instalar Dependencias
Instala Python:

Asegúrate de tener Python instalado. Puedes descargarlo desde python.org.
Instala las dependencias:

Ejecuta los siguientes comandos en tu terminal para instalar las dependencias necesarias:


pip install schedule pyautogui flask requests threading
Paso 4: Ejecutar el Script
Ejecuta el script:

Ejecuta el siguiente comando para iniciar el servidor:


python server.py
Copia la URL pública de Codespaces:

Si estás utilizando GitHub Codespaces, copia la URL pública que se mostrará en la terminal.
Paso 5: Configurar UptimeRobot
Crea una cuenta en UptimeRobot:

Ve a UptimeRobot y crea una cuenta si no tienes una.
Añadir un nuevo monitor:

Inicia sesión y selecciona "Add New Monitor".
Selecciona "HTTP(s)" como el tipo de monitor.
Ingresa la URL pública de tu servidor en el campo de URL.
Configura el intervalo de monitoreo a 5 minutos o lo que prefieras.
Guarda los cambios.
