from pytest_bdd import scenario, given, when, then, parsers
from api import most_views

@scenario(scenario_name="Mudar periodo de tempo", feature_name="../features/mais_vistos.feature")
def test_change_most_viewed_time_period():
    """"Mudar periodo de tempo"""

@given(parsers.cfparse('estou na página Mais Vistos'))
def check_current_page():
    pass

@then(parsers.cfparse('eu vejo uma lista de animes sem periodo de tempo definido'), target_fixture="context")
def mock_get_anime_list():
    
    context = {}
    context["mais_vistos_sempre"] = most_views.order_most_views("decrescente", 3, None)

    assert isinstance(context["mais_vistos_sempre"], list)

    return context

@then(parsers.cfparse('o primeiro anime da lista desde sempre é "{anime_1}" com "{views_1}" visualizacoes'), target_fixture="context")
def check_first_anime(context, anime_1: str, views_1: int):
        
    views_1 = int(views_1)

    # Checa se está na lista
    assert context["mais_vistos_sempre"][0]["name"] == anime_1
    assert context["mais_vistos_sempre"][0]["views"] == views_1

    return context

@then(parsers.cfparse('o segundo anime da lista desde sempre é "{anime_2}" com "{views_2}" visualizacoes'), target_fixture="context")
def check_second_anime(context, anime_2: str, views_2: int):
            
    views_2 = int(views_2)

    # Checa se está na lista
    assert context["mais_vistos_sempre"][1]["name"] == anime_2
    assert context["mais_vistos_sempre"][1]["views"] == views_2
    # Checa ordenacao
    assert context["mais_vistos_sempre"][1]["views"] < context["mais_vistos_sempre"][0]["views"]

    return context

@then(parsers.cfparse('o terceiro anime da lista desde sempre é "{anime_3}" com "{views_3}" visualizacoes'), target_fixture="context")
def check_third_anime(context, anime_3: str, views_3: int):
                
    views_3 = int(views_3)
    
    # Checa se está na lista
    assert context["mais_vistos_sempre"][2]["name"] == anime_3
    assert context["mais_vistos_sempre"][2]["views"] == views_3
    # Checa ordenacao
    assert context["mais_vistos_sempre"][2]["views"] < context["mais_vistos_sempre"][1]["views"]

    return context

@when(parsers.cfparse('eu seleciono que o periodo da lista seja do último "{periodo}"'), target_fixture="context")
def changing_time_period(context, periodo: str):
    
    #context = {}
    context["mais_vistos_mes"] = most_views.order_most_views("decrescente", 3, periodo)
    
    return context

@then(parsers.cfparse('o primeiro anime da lista do ultimo mes é "{anime_1}" com "{views_1}" visualizacoes'), target_fixture="context")
def check_first_anime(context, anime_1: str, views_1: int):
        
    views_1 = int(views_1)

    # Checa se está na lista
    assert context["mais_vistos_mes"][0]["name"] == anime_1
    assert context["mais_vistos_mes"][0]["views"] == views_1
    # Checa logica
    assert context["mais_vistos_mes"][0]["views"] < context["mais_vistos_sempre"][0]["views"]

    return context

@then(parsers.cfparse('o segundo anime da lista do ultimo mes é "{anime_2}" com "{views_2}" visualizacoes'), target_fixture="context")
def check_second_anime(context, anime_2: str, views_2: int):
                
    views_2 = int(views_2)

    # Checa se está na lista
    assert context["mais_vistos_mes"][1]["name"] == anime_2
    assert context["mais_vistos_mes"][1]["views"] == views_2
    # Checa ordenacao
    assert context["mais_vistos_mes"][1]["views"] < context["mais_vistos_mes"][0]["views"]
    # Checa logica
    assert context["mais_vistos_mes"][1]["views"] < context["mais_vistos_sempre"][1]["views"]

    return context

@then(parsers.cfparse('o terceiro anime da lista do ultimo mes é "{anime_3}" com "{views_3}" visualizacoes'), target_fixture="context")
def check_third_anime(context, anime_3: str, views_3: int):
                        
    views_3 = int(views_3)
    
    # Checa se está na lista
    assert context["mais_vistos_mes"][2]["name"] == anime_3
    assert context["mais_vistos_mes"][2]["views"] == views_3
    # Checa ordenacao
    assert context["mais_vistos_mes"][2]["views"] < context["mais_vistos_mes"][1]["views"]
    # Checa logica
    assert context["mais_vistos_mes"][2]["views"] < context["mais_vistos_sempre"][2]["views"]

    return context