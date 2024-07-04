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


# Segunda Saga

def saga_schemaZ(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "genre": user["genre"],
            "race": user["race"],
            "image": user["image"],
            "planet": user["planet"],
            "description": user["description"],
            "biography": user["biography"],
            "transformations": user["transformations"]}


def sagas_schemaZ(sagaball) -> list:
    return [saga_schemaZ(user) for user in sagaball]


# Dragones

def dragon(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "image": user["image"],
            "description": user["description"],
            "biography": user["biography"]}


def dragons(sagaball) -> list:
    return [dragon(user) for user in sagaball]