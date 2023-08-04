from pydantic import BaseModel
from typing import Optional

class Anime(BaseModel):
    nome_anime: str
    views: Optional[int] = 0
    