from fastapi.params import Depends
from ..models.models import TaskModel
from fastapi import APIRouter
from ..database.database import database
from ..schemas.schemas import userSchema,UserKey
from ..security.oauth2 import getCurrentUser


router = APIRouter(prefix="/todo", tags=["todo"])


@router.post("/create_todo")
async def insert(name: str, task: str, title: str, date,currentUser: userSchema = Depends(getCurrentUser)):
    userKey = next(database["USERS"].fetch({"name": name}))[0]
    user = database["TASKS"].insert(TaskModel(title, task, date, userKey))
    return user


@router.post("/")
async def get_posts_by_user(request:UserKey):
    user =database["TASKS"].fetch({"userKey": request.name})

    return user
