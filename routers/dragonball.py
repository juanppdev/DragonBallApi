### sagaball DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.sagas import SagaBall
from db.schemas.sagas import saga_schema, sagas_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/dragonballz",
                   tags=["dragonball"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[SagaBall])
async def sagaball():
    return sagas_schema(db_client.sagaball.find())


@router.get("/{id}")  # Path
async def character(id: str):
    return search_character("_id", ObjectId(id))


@router.get("/")  # Query
async def character(id: str):
    return search_character("_id", ObjectId(id))


@router.post("/", response_model=SagaBall, status_code=status.HTTP_201_CREATED)
async def character(character: SagaBall):
    if type(search_character("name", character.name)) == SagaBall:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    character_dict = dict(character)
    del character_dict["id"]

    id = db_client.sagaball.insert_one(character_dict).inserted_id

    new_character = saga_schema(db_client.sagaball.find_one({"_id": id}))

    return SagaBall(**new_character)


@router.put("/", response_model=SagaBall)
async def character(character: SagaBall):

    character_dict = dict(character)
    del character_dict["id"]

    try:
        db_client.sagaball.find_one_and_replace(
            {"_id": ObjectId(character.id)}, character_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_character("_id", ObjectId(character.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def character(id: str):

    found = db_client.sagaball.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}

# Helper


def search_character(field: str, key):

    try:
        character = db_client.sagaball.find_one({field: key})
        return SagaBall(**saga_schema(character))
    except:
        return {"error": "No se ha encontrado el usuario"}