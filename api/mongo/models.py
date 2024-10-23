from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    genre: str
    year: int
    rating: float
