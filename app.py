from fastapi import FastAPI
import os
import sys
from routes.users import users

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()


app.include_router(users)