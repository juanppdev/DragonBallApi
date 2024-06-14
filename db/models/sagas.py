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

#class SagaBallZ(BaseModel):
