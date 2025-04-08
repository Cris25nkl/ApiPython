from motor.motor_asyncio import AsyncIOMotorClient

# URI de conexión a MongoDB Atlas (Reemplaza con tus credenciales)
MONGO_URI = "mongodb+srv://cris25nkl:Cristianflorez25@fastapi.uqmm6ru.mongodb.net/?retryWrites=true&w=majority&appName=FastApi"

# Nombre de la base de datos
DATABASE_NAME = "FastApi"

# Cliente de MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
