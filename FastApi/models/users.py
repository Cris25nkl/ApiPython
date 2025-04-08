from pydantic import BaseModel
from typing import Optional

class Userin(BaseModel):
    
    name: str
    email: str
    password: str
    is_active: Optional[bool]
   
class User(Userin):
    id: Optional[str]
    
