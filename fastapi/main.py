from fastapi import FastAPI

#contexto inicial de como se va a comportar nuestro servidor
app = FastAPI()

#accedo al contexto de fastapi
@app.get("/")
async def root():
    return 'Hola mundo'