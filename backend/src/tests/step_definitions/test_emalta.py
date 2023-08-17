from pytest_bdd import parsers, given, when, then, scenario
from service.impl.item_service import ItemService
from schemas.response import HttpResponseModel, HTTPResponses

@scenario(scenario_name="Obter lista de animes", feature_name="../features/animes.feature")
def get_anime_list():
    """Get Anime List"""    

@given(parsers.cfparse('a ClasseAnime retorna uma lista de objetos anime'))
def mock_anime_response_list():
    
    ItemService.get_animes = lambda: HttpResponseModel(
        message=HTTPResponses.ITEM_FOUND().message,
        status_code=HTTPResponses.ITEM_FOUND().status_code,
        data={
            'animes': [
                {"nome_anime": "Naruto", "avaliacao_anime": "7.0", "qtd_assistido": "120"},
                {"nome_anime": "Kimetsu No Yaiba", "avaliacao_anime": "7.2", "qtd_assistido": "90"},
                {"nome_anime": "One Piece", "avaliacao_anime": "7.4", "qtd_assistido": "130"}
            ]
        }
        
        
    )
    
@when(parsers.cfparse('uma requisição "GET" for enviada para "{req_url}"'),
      target_fixture="context")
def get_anime_request(client, context, req_url: str):
    response = client.get(req_url)
    context["response"] = response
    return context