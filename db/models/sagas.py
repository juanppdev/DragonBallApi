from pydantic import BaseModel


class SagaBall(BaseModel): # Primera Saga
    id: str
    name: str
    genre: str
    race: str
    image: str
    planet: str
    description: str
    biography: str

class SagaBallZ(BaseModel):
    id: str
    name: str
    genre: str
    race: str
    image: str
    planet: str
    description: str
    biography: str
    transformations: list[dict]

class Dragons(BaseModel):
    id: str
    name: str
    image: str
    description: str
    biography: str