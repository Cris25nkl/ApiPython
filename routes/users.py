from fastapi import APIRouter, responses, status
from config.database import db
from schemas.users import userEntity, usersEntity
from models.users import Userin, User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


users = APIRouter()

 #------------------ Request GET ----------------- #
@users.get("/users", response_model=list[User], tags=["users"])
async def get_all_users():
    return usersEntity(await db.users.find().to_list(1000))

@users.get("/users/{user_id}", response_model=Userin, tags=["users"])
async def get_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        return responses.JSONResponse(status_code=400, content={"message": "El usuario no existe o el id es incorrecto"})
    
    
    return userEntity(await db.users.find_one({"_id": ObjectId(user_id)}))


#------------------ Request POST ----------------- #

@users.post("/users", response_model=Userin, tags=["users"])
async def create_user(user: Userin):
    new_user = user.dict()
    new_user["password"] = sha256_crypt.hash(new_user["password"])
    result = await db.users.insert_one(new_user)
    user = await db.users.find_one({"_id": result.inserted_id})
    
    return {"message": "Usuario creado", "user": userEntity(user)}

#------------------ Request PUT ----------------- #

@users.put("/users/{user_id}", response_model=Userin, tags=["users"])

async def update_user(user_id: str, user: Userin):
    return userEntity(await db.users.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": user.dict()}))
   


#------------------ Request DELETE ----------------- #

@users.delete("/users/{user_id}", status_code=HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(user_id: str):
    userEntity(await db.users.find_one_and_delete({"_id": ObjectId(user_id)}))
    return responses.JSONResponse(status_code=HTTP_204_NO_CONTENT, content={"message": "Usuario eliminado"})