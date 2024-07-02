### Dragons DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.sagas import Dragons
from db.schemas.sagas import dragon, dragons
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/dragons",
                   tags=["dragons"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[Dragons])
async def sagaball():
    return dragons(db_client.Dragons.find())


@router.get("/{id}")  # Path
async def character(id: str):
    return search_character("_id", ObjectId(id))


@router.get("/")  # Query
async def character(id: str):
    return search_character("_id", ObjectId(id))


@router.post("/", response_model=Dragons, status_code=status.HTTP_201_CREATED)
async def character(character: Dragons):
    if type(search_character("name", character.name)) == Dragons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El Dragon ya existe")

    character_dict = dict(character)
    del character_dict["id"]

    id = db_client.Dragons.insert_one(character_dict).inserted_id

    new_character = dragon(db_client.Dragons.find_one({"_id": id}))

    return Dragons(**new_character)


@router.put("/", response_model=Dragons)
async def character(character: Dragons):

    character_dict = dict(character)
    del character_dict["id"]

    try:
        db_client.Dragons.find_one_and_replace(
            {"_id": ObjectId(character.id)}, character_dict)
    except:
        return {"error": "No se ha actualizado el Personaje"}

    return search_character("_id", ObjectId(character.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def character(id: str):

    found = db_client.Dragons.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}

# Helper


def search_character(field: str, key):

    try:
        character = db_client.Dragons.find_one({field: key})
        return Dragons(**dragon(character))
    except:
        return {"error": "No se ha encontrado el usuario"}