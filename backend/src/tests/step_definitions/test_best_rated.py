from pytest_bdd import scenario, given, when, then, parsers
from service.impl.item_service import ItemService
from schemas.response import HttpResponseModel, HTTPResponses

@scenario(scenario_name="Acessar lista de animes mais bem avaliados na ordem decrescente", feature_name="../features/mais_bem_avaliados.feature")
def test_get_br_descending():
    pass

@given(parsers.cfparse('order_best_rated retorna uma lista de animes'))
def mock_order_best_rated_response_list():

    ItemService.get_best_rated_descending = lambda id: HttpResponseModel(
        message=HTTPResponses.ITEM_FOUND().message,
        status_code=HTTPResponses.ITEM_FOUND().status_code,
        data={"lista_de_animes": [   
                {"nome": "One Piece",           "nota": 8.9},
                {"nome": "Kimetsu no Yaiba",    "nota": 8.7},
                {"nome": "Naruto",              "nota": 8.4}
                ]
            }
    )

@when(parsers.cfparse('uma requisicao "{req_type}" for enviada para "{req_url}"'),target_fixture = "context")
def send_get_best_rated_request(client, context, req_url: str):
    response = client.get(req_url)
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'),target_fixture = "context")
def check_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve conter uma lista de animes'), target_fixture="context")
def check_response_json(context):
    animes = context["response"].json()["data"]["lista_de_animes"]
    assert isinstance(animes, list)
    count = 0
    for anime in animes:
        assert isinstance(anime, dict)
        assert "nome" in anime and isinstance(anime["nome"], str)
        assert "nota" in anime and isinstance(anime["nota"], float)

        if count > 0:
            assert anime["nota"] < animes[count-1]["nota"]
        count += 1
    
    return context