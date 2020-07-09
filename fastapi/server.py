from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FilmPost(BaseModel):
    title: str
    option: str

@app.post("/postfilm/")
async def new_film(item: FilmPost):
    return {
        "YourTitle": item.title,
        "YourOption": item.option
    }
