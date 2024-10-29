from flask import Blueprint, abort, make_response
from app.models.dog import dogs

dogs_bp = Blueprint("dogs_bp", __name__, url_prefix="/dogs")

@dogs_bp.get("")
def get_all_dogs():
    result_dogs = []
    for dog in dogs:
        result_dogs.append(
            {
            "id" : dog.id,
            "breed" : dog.breed,
            "color" : dog.color,
            "age_span" : dog.age_span
            }
        )
    return result_dogs


def validate_dog(dog_id):
    try:
        dog_id = int(dog_id)
    except:
        abort(make_response(f"Dod id: {id} is invalid."), 400)
    for dog in dogs:
        if dog.id == dog_id:
            return dog
    abort(make_response(f"Dod id: {id} not found."), 404)


@dogs_bp.get("/<dog_id>")
def get_one_dog(dog_id):
    dog = validate_dog(dog_id)
    return dog.to_dict(), 200
