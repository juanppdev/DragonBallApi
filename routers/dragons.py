from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import json
import os

router = APIRouter(prefix="/dragons",
                   tags=["dragons"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

DATA_FILE = os.path.join(os.path.dirname(__file__), 'dragons.json')

class Dragons(BaseModel):
    id: int
    name: str
    genre: str
    race: str
    image: str
    planet: str
    description: str
    biography: str
    transformations: list

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@router.get("/", response_model=list[Dragons])
async def sagaball():
    data = load_data()
    return data

@router.get("/{id}")  # Path
async def character(id: int):
    return search_character("id", id)

@router.get("/")  # Query
async def character(id: int):
    return search_character("id", id)

@router.post("/", response_model=Dragons, status_code=status.HTTP_201_CREATED)
async def character(character: Dragons):
    data = load_data()
    if any(c['name'] == character.name for c in data):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El Dragon ya existe")

    character_dict = character.dict()
    character_dict["id"] = len(data) + 1
    data.append(character_dict)
    save_data(data)

    return Dragons(**character_dict)

@router.put("/", response_model=Dragons)
async def character(character: Dragons):
    data = load_data()
    for i, c in enumerate(data):
        if c['id'] == character.id:
            data[i] = character.dict()
            save_data(data)
            return Dragons(**data[i])
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dragon no encontrado")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def character(id: int):
    data = load_data()
    new_data = [c for c in data if c['id'] != id]
    if len(new_data) == len(data):
        return {"error": "No se ha eliminado el Dragon"}
    save_data(new_data)

# Helper

def search_character(field: str, key):
    data = load_data()
    for c in data:
        if c[field] == key:
            return Dragons(**c)
    return {"error": "No se ha encontrado el Dragon"}
