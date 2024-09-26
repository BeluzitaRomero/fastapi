from fastapi import FastAPI

#contexto inicial de como se va a comportar nuestro servidor
app = FastAPI()

#accedo al contexto de fastapi
#Comando para levantar el servidor: uvicorn main:app --reload
# para acceder a la autodocumentacion /docs en el root
# para acceder a la autodocumentacion /redoc en el root
@app.get("/")
async def root():
    return 'Hola mundo !'