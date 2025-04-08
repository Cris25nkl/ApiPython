from fastapi import APIRouter, HTTPException , responses
from config.database import db
from schemas.users import userEntity, usersEntity
from models.users import Userin
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


users = APIRouter()

 #------------------ Request GET ----------------- #
@users.get("/users")
async def get_all_users():
    return usersEntity(await db.users.find().to_list(1000))

@users.get("/users/{user_id}")
async def get_user(user_id: str):
    
    return userEntity(await db.users.find_one({"_id": ObjectId(user_id)}))


#------------------ Request POST ----------------- #

@users.post("/users")
async def create_user(user: Userin):
    new_user = user.dict()
    new_user["password"] = sha256_crypt.hash(new_user["password"])
    result = await db.users.insert_one(new_user)
    user = await db.users.find_one({"_id": result.inserted_id})
    
    return {"message": "Usuario creado", "user": userEntity(user)}

#------------------ Request PUT ----------------- #

@users.put("/users/{user_id}")

async def update_user(user_id: str, user: Userin):
    return userEntity(await db.users.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": user.dict()}))
   


#------------------ Request DELETE ----------------- #

@users.delete("/users/{user_id}")
async def delete_user(user_id: str):
    userEntity(await db.users.find_one_and_delete({"_id": ObjectId(user_id)}))
    return responses.JSONResponse(status_code=HTTP_204_NO_CONTENT, content={"message": "Usuario eliminado"})