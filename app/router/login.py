from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from ..database.database import database
from ..security.hashing import Hash
from ..security.token import create_access_token

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user = next(database["USERS"].fetch({"email": request.username}))[0]
    password = user["password"]
    email = user["email"]

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

    if not Hash.verify(password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="incorrect password")

    if user:
        access_token = create_access_token(
            data={"sub": email}
        )
        return {"user": user, "access_token": access_token, "token_type": "bearer"}
