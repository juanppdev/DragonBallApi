from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import json
import os

router = APIRouter(prefix="/dragonballgt",
                   tags=["dragonballgt"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

DATA_FILE =  os.path.join(os.path.dirname(__file__), 'dragonballgt.json')

class SagaBall(BaseModel):
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
            content = file.read()
            if content:
                try:
                    data = json.loads(content)
                    return data
                except json.JSONDecodeError as e:
                    return []
            else:
                return []
    else:
        save_data([])  # Crear un archivo JSON vacío
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


@router.get("/", response_model=list[SagaBall])
async def sagaball():
    data = load_data()
    print("Datos cargados:", data)  # Añadir log
    return data

@router.get("/{id}")  # Path
async def character(id: int):
    return search_character("id", id)

@router.get("/")  # Query
async def character(id: int):
    return search_character("id", id)

@router.post("/", response_model=SagaBall, status_code=status.HTTP_201_CREATED)
async def character(character: SagaBall):
    data = load_data()
    if any(c['name'] == character.name for c in data):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El Personaje ya existe")

    character_dict = character.dict()
    character_dict["id"] = len(data) + 1
    data.append(character_dict)
    save_data(data)

    return SagaBall(**character_dict)

@router.put("/", response_model=SagaBall)
async def character(character: SagaBall):
    data = load_data()
    for i, c in enumerate(data):
        if c['id'] == character.id:
            data[i] = character.dict()
            save_data(data)
            return SagaBall(**data[i])
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personaje no encontrado")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def character(id: int):
    data = load_data()
    new_data = [c for c in data if c['id'] != id]
    if len(new_data) == len(data):
        return {"error": "No se ha eliminado el Personaje"}
    save_data(new_data)

# Helper

def search_character(field: str, key):
    data = load_data()
    for c in data:
        if c[field] == key:
            return SagaBall(**c)
    return {"error": "No se ha encontrado el Personaje"}
