def saga_schema(user) -> dict:  # Primera Saga
    return {"id": str(user["_id"]),
            "name": user["name"],
            "genre": user["genre"],
            "race": user["race"],
            "image": user["image"],
            "planet": user["planet"],
            "description": user["description"],
            "biography": user["biography"]}


def sagas_schema(sagaball) -> list: # Primera Saga
    return [saga_schema(user) for user in sagaball]