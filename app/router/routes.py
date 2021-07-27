
from . import Users,login, recipies

def initRoutes(app):
     # app.include_router(ROUTERNAME.router)
    app.include_router(Users.router)
    app.include_router(login.router)
    app.include_router(recipies.router)
