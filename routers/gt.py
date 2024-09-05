#!/usr/bin/python

from fastapi import APIRouter, HTTPException, status
from db.models.sagas import SagaBallGT
from db.schemas.gt import gt_schema, gts_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/ballgt",
                   tags=["ballgt"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[GT])
async def gts():
    return gts_schema(db_client.gts.find())


@router.get("/{id}")  # Path
async def gt(id: str):
    return search_gt("_id", ObjectId(id))


@router.get("/")  # Query
async def gt(id: str):
    return search_gt("_id", ObjectId(id))


@router.post("/", response_model=GT, status_code=status.HTTP_201_CREATED)
async def gt(gt: GT):
    if type(search_gt("email", gt.email)) == GT:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El GT ya existe")

    gt_dict = dict(gt)
    del gt_dict["id"]

    id = db_client.gts.insert_one(gt_dict).inserted_id

    new_gt = gt_schema(db_client.gts.find_one({"_id": id}))

    return GT(**new_gt)


@router.put("/", response_model=GT)
async def gt(gt: GT):

    gt_dict = dict(gt)
    del gt_dict["id"]

    try:
        db_client.gts.find_one_and_replace(
            {"_id": ObjectId(gt.id)}, gt_dict)
    except:
        return {"error": "No se ha actualizado el GT"}

    return search_gt("_id", ObjectId(gt.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def gt(id: str):

    found = db_client.gts.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el GT"}

# Helper


def search_gt(field: str, key):

    try:
        gt = db_client.gts.find_one({field: key})
        return GT(**gt_schema(gt))
    except:
        return {"error": "No se ha encontrado el GT"}
