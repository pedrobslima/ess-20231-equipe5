from fastapi import APIRouter
from banco_de_animes.classe_anime import lista_animes as anime_list

# Funções
def is_reverse(order_by):
    if order_by == "crescente":
        return False
    else:
        return True

def order_best_rated(order_by, max):

    # Cria uma lista de dicionarios contendo os detalhes dos animes
    best_rated_list = []
    for anime in anime_list:
        best_rated_list.append({"name":anime.nome_anime,"rating":anime.avaliacao_anime, "img_url":anime.img_url})
    
    # Ordena a lista baseado na chave "rating" de cada dicionário
    best_rated_list = sorted(best_rated_list, key=lambda x: x["rating"], reverse=is_reverse(order_by))

    return best_rated_list[0:max]

# Router
router = APIRouter()

@router.get("/")
async def best_rated(order_by: str = "decrescente", max: int = 10):
    return {"GET": {"anime_list" : order_best_rated(order_by, max)}}