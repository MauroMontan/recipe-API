
from . import Users, to_do, login, recipies


def initRoutes(app):
    app.include_router(Users.router)
    app.include_router(to_do.router)
    app.include_router(login.router)
    app.include_router(recipies.router)
    # app.include_router(ROUTERNAME.router)
