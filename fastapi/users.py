from fastapi import FastAPI
from pydantic import BaseModel

#contexto inicial de como se va a comportar nuestro servidor
app = FastAPI()

#Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1, name="Belu", surname ="Romero", age=35), 
              User(id=2,name="Jose", surname="lopez", age=30), 
              User(id=3,name="pepe", surname="rodriguez", age=10)
              ]    


# @app.get("/usersjson")
# async def userjson():
#     return [{"id": 1,"name": "Bel", "lastname": "romero", "age": 35},
#             {"id": 2,"name": "pepe", "lastname": "romero", "age": 25},
#             {"id": 3,"name": "jose", "lastname": "lopez","age":30}]

#Directamente BaseModel transforma a json
@app.get("/users")
async def users():
    return users_list

#por PATH
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query    
@app.get("/userquery/") # /?id=1
async def user(id: int):
    return search_user(id)

#La defino para llamarla en las rutas
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except: 
        return {"Error": "No se ha encontrado el usuario"}
    

@app.post("/user/")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error":"El usuario ya existe"}
    else: 
        users_list.append(user)
        #para que no devuelva null
        return user

#PUT
@app.put("/user/")
async def put_user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"No se ha actualizado"}      
    else:
        #Para que no devuelva un null
        return user 

@app.delete("/user/{id}")
async def del_user(id:int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error":"No se ha borrado"}
