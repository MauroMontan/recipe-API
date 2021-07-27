

# user model

def UserModel(name: str, username: str, email: str, hashedPassword: str) -> dict:
    User = {
        "name": name,
        "username": username,
        "email": email,
        "password": hashedPassword,
    }
    return User


# tasks model

def TaskModel(title, task, date, userKey) -> dict:
    Task = {
        "title": title,
        "task": task,
        "date": date,
        "userKey": userKey["name"],
    }
    return Task


# Recipie models

def RecipieModel(recipie_name, author, cook_time, prepare_time, ingredients, directions,card_color,dish_picure, userKey) -> dict:
    Recipie = {
        "recipie_name": recipie_name,
        "author": author,
        "cook_time": cook_time,
        "prepare_time": prepare_time,
        "ingredients": ingredients,
        "directions": directions,
        "card_color":card_color,
        "picture_name":dish_picure,
        "userKey": userKey["key"],
    }
    return Recipie
