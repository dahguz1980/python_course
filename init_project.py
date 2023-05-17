import os
import subprocess
import platform
import urllib.parse
import urllib.request
import json
import time

# Ruta al directorio del entorno virtual
virtualenv_path = "entorno_virtual"

# Comprobar el sistema operativo
is_windows = platform.system() == "Windows"

# Comando para crear el entorno virtual
if is_windows:
    create_venv_command = ["python", "-m", "venv", virtualenv_path]
else:
    create_venv_command = ["python3", "-m", "venv", virtualenv_path]

# Crear el entorno virtual
subprocess.run(create_venv_command, check=True)

# Activar el entorno virtual
if is_windows:
    activate_script = os.path.join(virtualenv_path, "Scripts", "activate.bat")
else:
    activate_script = os.path.join(virtualenv_path, "bin", "activate")

# Ejecutar el comando para activar el entorno virtual
activate_command = f"{activate_script}" if is_windows else f"source {activate_script}"
result = subprocess.run(activate_command, shell=True)
print(result)

# Actualizar pip dentro del entorno virtual e instalar librerias necesarias
if is_windows:
    pip_command = os.path.join(virtualenv_path, "Scripts", "pip.exe")
    subprocess.run(
        [pip_command, "-m", "pip", "install", "--upgrade", "pip"], check=True
    )
    subprocess.run(
        [pip_command, "-m", "pip", "install", "-r", "requirements.txt"], check=True
    )
else:
    pip_command = os.path.join(virtualenv_path, "bin", "pip")
    subprocess.run([pip_command, "install", "--upgrade", "pip"], check=True)
    subprocess.run([pip_command, "install", "-r", "requirements.txt"], check=True)


# Obtener la ruta absoluta al directorio del script actual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta relativa al proyecto Django
project_directory = os.path.join(
    script_directory, "MiProyecto"
)  # Reemplaza "ruta_relativa_al_proyecto" con la ruta relativa a tu proyecto Django

# Sync Models
manage_py_path = os.path.join(project_directory, "manage.py")
if is_windows:
    process = subprocess.run(
        [pip_command, manage_py_path, "makemigrations"], check=True
    )
    process = subprocess.run([pip_command, manage_py_path, "migrate"], check=True)
else:
    process = subprocess.run(["python3", manage_py_path, "makemigrations"], check=True)
    process = subprocess.run(["python3", manage_py_path, "migrate"], check=True)
