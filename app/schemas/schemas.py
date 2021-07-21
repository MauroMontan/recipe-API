from pydantic import BaseModel


class UserKey(BaseModel):
    name: str


class Recipie_key(BaseModel):
    key: str


class Recipie(BaseModel):
    key: str
    recipie_name: str
    author: str
    cook_time: str
    prepare_time: str
    ingredients: str
    directions: str
    card_color: str


class userSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: str
    email: str
    username: str
