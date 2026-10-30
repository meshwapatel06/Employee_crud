from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Employee(BaseModel):
    id : Optional[int] = None 
    name: str
    email: str
    department: str
    salary: int