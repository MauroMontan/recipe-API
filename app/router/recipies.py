
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from ..schemas.schemas import Recipie, UserKey, Recipie_key, userSchema
from ..security.oauth2 import getCurrentUser
from ..database.database import database
from ..models.models import RecipieModel

router = APIRouter(prefix="/recipies", tags=["recipies"])


@router.post("/")
async def createRecipie(request: Recipie, currentUser: userSchema = Depends(getCurrentUser)):
    userKey = next(database["USERS"].fetch({"name": currentUser.name}))[0]
    recipie = database["RECIPIES"].insert(RecipieModel(
        request.recipie_name, request.author, request.cook_time, request.prepare_time, request.ingredients, request.directions, request.card_color, userKey))
    return recipie


@router.post("/user-recipies")
async def get_recipies_by_user(currentUser: userSchema = Depends(getCurrentUser)):
    userKey = next(database["USERS"].fetch({"name": currentUser.name}))[0]
    userRecipies = database["RECIPIES"].fetch({"userKey": userKey["key"]})
    return userRecipies


@router.delete("/delete-recipie")
async def delete_recipie(request: Recipie_key):
    deleted_recipie = database["RECIPIES"].delete(request.key)

    return deleted_recipie


@router.put("/update-recipie/")
async def update_recipe(request: Recipie,currentUser: userSchema = Depends(getCurrentUser)):
    userKey = next(database["USERS"].fetch({"name": currentUser.name}))[0]
    payload = {
        "recipie_name": request.recipie_name,
        "author": request.author,
        "cook_time": request.cook_time,
        "prepare_time": request.prepare_time,
        "ingredients": request.ingredients,
        "directions": request.directions,
        "card_color": request.card_color,
        "userKey":userKey["key"],
    }
    
    record = database["RECIPIES"].put(data=payload, key=request.key)

    return record
