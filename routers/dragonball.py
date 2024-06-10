### sagaball DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.sagas import SagaBall
from db.schemas.sagas import saga_schema, sagas_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/dragonball",
                   tags=["dragonball"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[SagaBall])
async def sagaball():
    return sagas_schema(db_client.sagaball.find())


@router.get("/{id}")  # Path
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.get("/")  # Query
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.post("/", response_model=SagaBall, status_code=status.HTTP_201_CREATED)
async def user(user: SagaBall):
    if type(search_user("name", user.name)) == SagaBall:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.sagaball.insert_one(user_dict).inserted_id

    new_user = saga_schema(db_client.sagaball.find_one({"_id": id}))

    return SagaBall(**new_user)


@router.put("/", response_model=SagaBall)
async def user(user: SagaBall):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.sagaball.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

    found = db_client.sagaball.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}

# Helper


def search_user(field: str, key):

    try:
        user = db_client.sagaball.find_one({field: key})
        return SagaBall(**saga_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}