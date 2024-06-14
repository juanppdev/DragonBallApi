### sagaballz DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.sagas import SagaBallZ
from db.schemas.sagas import saga_schemaZ, saga_schemaZ
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/dragonballz",
                   tags=["dragonballz"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[SagaBallZ])
async def sagaball():
    return saga_schemaZ(db_client.sagaballz.find())


@router.get("/{id}")  # Path
async def character(id: str):
    return search_character("_id", ObjectId(id))


@router.get("/")  # Query
async def character(id: str):
    return search_character("_id", ObjectId(id))


@router.post("/", response_model=SagaBallZ, status_code=status.HTTP_201_CREATED)
async def character(character: SagaBallZ):
    if type(search_character("name", character.name)) == SagaBallZ:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El Personaje ya existe")

    character_dict = dict(character)
    del character_dict["id"]

    id = db_client.sagaballz.insert_one(character_dict).inserted_id

    new_character = saga_schemaZ(db_client.sagaballz.find_one({"_id": id}))

    return SagaBallZ(**new_character)


@router.put("/", response_model=SagaBallZ)
async def character(character: SagaBallZ):

    character_dict = dict(character)
    del character_dict["id"]

    try:
        db_client.sagaballz.find_one_and_replace(
            {"_id": ObjectId(character.id)}, character_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_character("_id", ObjectId(character.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def character(id: str):

    found = db_client.sagaballz.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}

# Helper


def search_character(field: str, key):

    try:
        character = db_client.sagaballz.find_one({field: key})
        return SagaBallZ(**saga_schemaZ(character))
    except:
        return {"error": "No se ha encontrado el usuario"}