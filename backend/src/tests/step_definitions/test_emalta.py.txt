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

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'),
      target_fixture="context")
def status_code_response(context, status_code: str):
    """
    Checking the status code
    """
    assert context["response"].status_code == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve ser uma lista composta por animes'),
      target_fixture="context")
def check_json(context):
    """Testing if JSON is a list of Objects"""
    animes = context["response"].json()["data"]["animes"] #Observar corretude dessa linha
    
    assert isinstance(animes, list)
    
    for anime in animes:
        assert isinstance(anime, dict)
        assert "nome_anime" in anime
        assert "avaliacao_anime" in anime
        assert "qtd_assistido" in anime
        
    return context

@then(parsers.cfparse('o anime com nome "{nome_ani}", avaliacao "{aval_ani}" e assistidos "{qtd_views}" está na lista'),
      target_fixture="context")
def check_anime_in_list(context, nome_ani: str, aval_ani: str, qtd_views: str):
    """Check if anime 'x' with aval 'y' and views 'w' is in List"""
    animes = context["response"].json()["data"]["animes"] #observar corretude dessa linha
    
    assert {"nome_anime": nome_ani, "avaliacao_anime": aval_ani, "qtd_assistido": qtd_views} in animes
    return context            