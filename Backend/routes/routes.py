from fastapi import APIRouter

from models.registration import Registration
from databaseConfiguration.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router=APIRouter()

@router.get("/")
async def get_users_info():
    registrations=list_serial(collection_name.find())
    return registrations

@router.post("/")
async def post_registration_info(registration:Registration):
    collection_name.insert_one(dict(registration))


@router.get("/username/{username}")
async def get_username(username:str):
    users=collection_name.find_one({"username":username})
    if users:
        return True
    return False

@router.get("/email/{email}")
async def get_email(email:str):
    users=collection_name.find_one({"email":email})
    if users:
        return True
    return False

@router.get("/phone_number/{phone_number}")
async def get_phone_number(phone_number:str):
    users=collection_name.find_one({"phone_number":phone_number})
    if users:
        return True
    return False

@router.delete("/{id}")
async def delete_todo(id:str,registration:Registration):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})