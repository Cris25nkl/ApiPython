from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env

load_dotenv()

# URI de conexión a MongoDB Atlas (Reemplaza con tus credenciales)
MONGO_URI = os.getenv("MONGO_URI")
# Nombre de la base de datos
DATABASE_NAME = os.getenv("MONGO_NAME")

# Cliente de MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
