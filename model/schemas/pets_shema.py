from voluptuous import Schema, PREVENT_EXTRA


id_and_name = Schema(
    {
        "id": int,
        "name": str
    }
)


pet_shema = Schema(
    {
        "id": int,
        "category": id_and_name,
        "name": str,
        "photoUrls": [str],
        "tags": [id_and_name],
        "status": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

three_default_values = Schema(
    {
        "code": int,
        "type": str,
        "message": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

get_single_pet = Schema(pet_shema)

get_pet_not_found = Schema(three_default_values)

create_single_pet = Schema(pet_shema)




