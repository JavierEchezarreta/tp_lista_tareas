# Lista de tareas - Trabajo práctico de Programación II

## Presentación del proyecto. Por Javier Echezarreta.

Este gestor de tareas simple fue desarrollado en Python con PySide6 para la interfaz gráfica, siguiendo la metodología Test-Driven Development (TDD). La aplicación permite agregar, completar y eliminar tareas, gestionando las acciones del usuario de manera concreta.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente: 
- **Python 3.10 o superior ---> [Ver] (https://kinsta.com/es/base-de-conocimiento/instalar-python/)
- **Pip ----> [Ver] (https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/) 
- **Git (opcional)----> [Ver] (https://www.hostinger.com.ar/tutoriales/instalar-git-en-distintos-sistemas-operativos)

## Instalación

Para clonar el repositorio desde GitHub ejecuta: 
``` 
git clone https://github.com/JavierEchezarreta/tp_lista_tareas.git
```
Si no tienes Git, también puedes descargar el proyecto como archivo ZIP y descomprimirlo en tu máquina.

## Configuración del Entorno Virtual

Es recomendable trabajar con un entorno virtual para aislar las dependencias del proyecto. A continuación, se muestran los pasos para configurar el entorno virtual usando la herramienta 'venv' de Python. Para crear un entorno virtual con venv en el directorio del proyecto primero ejecuta:
``` 
python3 -m venv venv'
```
Una ves creado el entorno virtual debes ponerlo en funcionamiento ejecutando:

En Linux/Mac:
``` 
source venv/bin/activate
```
En Windows:
``` 
venv\Scripts\activate' 
```

## Instalación de Dependencias

Con el entorno virtual activado, instala las dependencias necesarias ejecutando el siguiente comando: 
``` 
'pip install -r requirements.txt'. 
```

## Ejecución de la Aplicación

Con las dependencias instaladas, puedes ejecutar la aplicación con el siguiente comando: 
``` 
python3 main.py
```
Esto abrirá la interfaz gráfica del gestor de tareas, lista para que empieces a agregar, completar y eliminar tareas.

## Uso de la Aplicación

Agregar Tarea: ingresa la descripción de la tarea en el campo de texto y presiona el botón "Agregar". Completar Tarea: selecciona la tarea en la lista y presiona "Completar". La tarea se marcará como completada. Eliminar Tarea: selecciona la tarea en la lista y presiona "Eliminar". La tarea será eliminada.




