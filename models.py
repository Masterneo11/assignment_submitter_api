from pydantic import BaseModel

class Course(BaseModel):
    id: int 
    name: str

class Assignments(BaseModel):
    id: int
    name: str
