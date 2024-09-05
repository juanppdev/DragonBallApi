#!/usr/bin/python

from fastapi import APIRouter, HTTPException, status
from db.models.super import Super
from db.schemas.super import super_schema, supers_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/ballsuper",
                   tags=["ballsuper"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[Super])
async def supers():
    return supers_schema(db_client.supers.find())


@router.get("/{id}")  # Path
async def super(id: str):
    return search_super("_id", ObjectId(id))


@router.get("/")  # Query
async def super(id: str):
    return search_super("_id", ObjectId(id))


@router.post("/", response_model=Super, status_code=status.HTTP_201_CREATED)
async def super(super: Super):
    if type(search_super("email", super.email)) == Super:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El super ya existe")

    super_dict = dict(super)
    del super_dict["id"]

    id = db_client.supers.insert_one(super_dict).inserted_id

    new_super = super_schema(db_client.supers.find_one({"_id": id}))

    return Super(**new_super)


@router.put("/", response_model=Super)
async def super(super: Super):

    super_dict = dict(super)
    del super_dict["id"]

    try:
        db_client.supers.find_one_and_replace(
            {"_id": ObjectId(super.id)}, super_dict)
    except:
        return {"error": "No se ha actualizado el super"}

    return search_super("_id", ObjectId(super.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def super(id: str):

    found = db_client.supers.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el super"}

# Helper


def search_super(field: str, key):

    try:
        super = db_client.supers.find_one({field: key})
        return Super(**super_schema(super))
    except:
        return {"error": "No se ha encontrado el super"}
