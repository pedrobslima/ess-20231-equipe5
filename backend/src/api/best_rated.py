from fastapi import APIRouter
from banco_de_animes.classe_anime import lista_animes as anime_list

# Funções
def order_best_rated(order_by, max):

    descending = True

    if order_by == "crescente":
        descending = False

    best_rated_list = []

    for anime in anime_list:
        best_rated_list.append({"name":anime.nome_anime,"rating":anime.avaliacao_anime, "img_url":anime.img_url})
    
    best_rated_list = sorted(best_rated_list, key=lambda x: x["rating"], reverse=descending)

    return best_rated_list[0:max]

# Router
router = APIRouter()

@router.get("/")
async def best_rated(order_by: str = "decrescente", max: int = 10):
    return {"GET": {"anime_list" : order_best_rated(order_by, max)}}