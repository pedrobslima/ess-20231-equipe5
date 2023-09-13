from datetime import datetime, timedelta
from fastapi import APIRouter
from banco_de_animes.classe_anime import lista_animes as anime_list

# Funções
def is_reverse(order_by):
    if order_by == "crescente":
        return False
    else:
        return True

def get_days_back(time_period):
    # O time_period armazena quantos dias abrange o período selecionado
    # ele será subtraído da data atual para obter a data alvo
    match time_period:
        case "dia":
            return 1
        case "semana":
            return 7
        case "mes":
            return 30
        case "trimestre":
            return 90
        case "ano":
            return 365
        case _:
            return 0

def select_dates_by_period(time_period, qtd_assistido_list):

    # Armazena a data atual
    today_date = datetime.today().date()

    # Armazena quantos dias abrange o período selecionado
    days_back = get_days_back(time_period)

    # Armazena a data em que o período desejado iniciou
    target_date = today_date - timedelta(days=days_back)

    # Por padrão, o time_period é None, o que significa que não há período especificado
    if time_period != None:
        # É criada e retornada uma lista contendo apenas datas no período desejado
        trimmed_list = [date for date in qtd_assistido_list if date > target_date and date <= today_date]
        return trimmed_list
    
    # Como não foi especificado um período, todas as datas são consideradas válidas, então a lista inteira é retornada
    return qtd_assistido_list
    
    
def order_most_views(order_by, max, time_period):

    # Quando não há querie de período, o frontend envia o time_period como uma string vazia, que deve ser convertida para None
    if time_period == '':
        time_period = None

    # Cria uma lista de dicionarios contendo os detalhes dos animes
    lista_mais_vistos = []
    for anime in anime_list:
        lista_mais_vistos.append({"name":anime.nome_anime,"views":len(select_dates_by_period(time_period, anime.qtd_assistido)), "img_url":anime.img_url})
    
    # Ordena a lista baseado na chave "views" de cada dicionário
    lista_mais_vistos = sorted(lista_mais_vistos, key=lambda x: x["views"], reverse=is_reverse(order_by))

    return lista_mais_vistos[0:max]

# Router
router = APIRouter()

@router.get("/")
async def mais_vistos(order_by: str = "decrescente", max: int = 10, t: str | None = None):
    return {"GET" : {"anime_list": order_most_views(order_by, max, t)}}