# ApiPython

# 🚀 API REST con FastAPI + MongoDB

Este proyecto es una API REST construida con **FastAPI** y **MongoDB Atlas**.  
Permite realizar operaciones CRUD sobre una colección de usuarios.


---

## 🧩 Tecnologías usadas

- [FastAPI](https://fastapi.tiangolo.com/) — Framework web asíncrono rápido.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) — Base de datos NoSQL en la nube.
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI rápido para Python.
- [Motor](https://motor.readthedocs.io/en/stable/) — Driver asíncrono para MongoDB.

---

## ⚙️ Instalación local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Cris25nkl/ApiPython.git
2. Instalar dependencias:

   Abres la carpeta del proyecto en el entorno de desrrollo de tu preferencia y ejecutas el comando 
   - pip install -r requirements.txt

   Para descargar las dependencias necesarias para su correcta ejecución.
3. Configuracion de variables de entorno:

   En un archivo .env se configuran las variables de entorno que se leeran para la conexion con la base de datos

   - MONGO_URL=mongodb+srv://usuario:contraseña@cluster.mongodb.net/db?retryWrites=true&w=majority

4. Ejecutar la aplicación:

    Ejecutamos el comando 

    - uvicorn app:app --reload

    El cual se encarga de iniciar el servidor local y de recargar automaticamente al hacerle algun cambio.

5. Ver la documentacio interactiva:
    
    En la url local añadimos /docs al final para acceder a la interfaz y documentacion.

    - http://localhost:8000/docs


## 📖 Documentación de la API
Modelo de Usuario

{

    "name": "Juan Pérez",

    "email": "juan@example.com",

    "password": "123456",

    "is_active": true

}

## 📖 Endpoints
- 📄 GET /users

Obtiene todos los usuarios.

- 🔍 GET /users/{id}

Obtiene un usuario por su ID.

- 📝 POST /users

Crea un nuevo usuario.

- ♻️ PUT /users/{id}

Actualiza un usuario existente.

- 🗑️ DELETE /users/{id}

Elimina un usuario por su ID.

## Api Desplegada 

Para el despliegue de esta api se utilizo Render como servidor en la nube 

- https://apipython-vn41.onrender.com/docs