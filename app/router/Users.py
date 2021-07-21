from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from ..database.database import database
from ..security.hashing import Hash
from ..models.models import UserModel
from ..schemas.schemas import userSchema

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/")
async def insert(request: userSchema):

    hashedPassword = Hash.bcrypt(request.password)
    user = database["USERS"].insert(
        UserModel(request.name, request.username, request.email, hashedPassword))
    return user


@router.get("/")
async def getUsers(name):
    users = database["USERS"].fetch()
    return jsonable_encoder(users)
