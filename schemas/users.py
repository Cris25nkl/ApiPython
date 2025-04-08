
def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "is_active": user["is_active"]
    }
    
def usersEntity(users) -> list:
    return [userEntity(user) for user in users]