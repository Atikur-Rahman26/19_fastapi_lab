from pydantic import BaseModel

class Registration(BaseModel):
    username:str
    password:str
    email:str
    phone_number:str