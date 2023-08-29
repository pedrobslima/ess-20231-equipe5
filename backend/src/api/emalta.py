from fastapi import APIRouter
from banco_de_animes.classe_anime import lista_animes, cont_ano, cont_trimestre, cont_semana, cont_dia

banco_animes = lista_animes

router = APIRouter()

@router.get('/')
async def get_emAlta():
    return {"Bem Vindo pagina": "Em Alta"}

@router.get('/ano')
async def emalta_ano():
    cont_ano()

    banco_animes.sort(reverse=True, key=lambda anime: anime.assistidos_periodo)
    return banco_animes

@router.get('/trimestre')
async def emalta_trimestre():
    cont_trimestre()

    banco_animes.sort(reverse=True, key=lambda anime: anime.assistidos_periodo)
    return banco_animes

@router.get('/semana')
async def emalta_semana():
    cont_semana()

    banco_animes.sort(reverse=True, key=lambda anime: anime.assistidos_periodo)
    return banco_animes

@router.get('/dia')
async def emalta_dia():
    cont_dia()

    banco_animes.sort(reverse=True, key=lambda anime: anime.assistidos_periodo)
    return banco_animes    