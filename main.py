from dataclasses import dataclass
from typing import Annotated
from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

@dataclass
class Credential:
    school: str
    username: str
    password: str

@app.get("/")
def read_root():
    return {"key": "Hello world!"}

@app.get("/authenticity")
def read_items(school: Annotated[str, Header()], username: Annotated[str, Header()], password: Annotated[str, Header()]):
    return {"message": f'Successfully logged in as {username}!'}
