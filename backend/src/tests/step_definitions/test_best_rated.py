from pytest_bdd import scenario, given, when, then, parsers
from api import best_rated

@scenario(scenario_name="Mudar a forma de ordenação da lista de decrescente para crescente", feature_name="../features/mais_bem_avaliados.feature")
def test_change_best_rated_list_order():
    """"Mudar forma de ordenação da lista"""

@given(parsers.cfparse('estou na página Mais Bem Avaliados'))
def check_current_page():
    pass

@then(parsers.cfparse('eu vejo uma lista de animes ordenada de maneira decrescente'), target_fixture="context")
def mock_get_anime_list():

    context = {}
    context["lista_de_animes_decrescente"] = best_rated.order_best_rated("decrescente", 3)

    assert isinstance(context["lista_de_animes_decrescente"], list)

    return context

@then(parsers.cfparse('o primeiro anime da lista decrescente é "{anime_1}" com nota "{nota_1}"'), target_fixture="context")
def check_first_anime(context, anime_1: str, nota_1: float):

    nota_1 = float(nota_1)

    # Checa se está na lista
    assert context["lista_de_animes_decrescente"][0]["name"] == anime_1
    assert context["lista_de_animes_decrescente"][0]["rating"] == nota_1

    return context

@then(parsers.cfparse('o segundo anime da lista decrescente é "{anime_2}" com nota "{nota_2}"'), target_fixture="context")
def check_second_anime(context, anime_2: str, nota_2: float):

    nota_2 = float(nota_2)

    # Checa se está na lista
    assert context["lista_de_animes_decrescente"][1]["name"] == anime_2
    assert context["lista_de_animes_decrescente"][1]["rating"] == nota_2
    # Checa se a nota é menor que a do item anterior
    assert context["lista_de_animes_decrescente"][1]["rating"] < context["lista_de_animes_decrescente"][0]["rating"]

    return context

@then(parsers.cfparse('o terceiro anime da lista decrescente é "{anime_3}" com nota "{nota_3}"'), target_fixture="context")
def check_third_anime(context, anime_3: str, nota_3: float):

    nota_3 = float(nota_3)
    
    # Checa se está na lista
    assert context["lista_de_animes_decrescente"][2]["name"] == anime_3
    assert context["lista_de_animes_decrescente"][2]["rating"] == nota_3
    # Checa se a nota é menor que a do item anterior
    assert context["lista_de_animes_decrescente"][2]["rating"] < context["lista_de_animes_decrescente"][1]["rating"]

    return context

@when(parsers.cfparse('eu mudo a forma de ordenação para crescente'), target_fixture="context")
def changing_order():
    
    context = {}
    context["lista_de_animes_crescente"] = best_rated.order_best_rated("crescente", 3)

    assert isinstance(context["lista_de_animes_crescente"], list)

    return context

@then(parsers.cfparse('o primeiro anime da lista crescente é "{anime_1_cresc}" com nota "{nota_1_cresc}"'), target_fixture="context")
def check_first_anime2(context, anime_1_cresc, nota_1_cresc):
    
    nota_1_cresc = float(nota_1_cresc)

    # Checa se está na lista
    assert context["lista_de_animes_crescente"][0]["name"] == anime_1_cresc
    assert context["lista_de_animes_crescente"][0]["rating"] == nota_1_cresc

    return context

@then(parsers.cfparse('o segundo anime da lista crescente é "{anime_2_cresc}" com nota "{nota_2_cresc}"'), target_fixture="context")
def check_second_anime2(context, anime_2_cresc, nota_2_cresc):
    
    nota_2_cresc = float(nota_2_cresc)

    # Checa se está na lista
    assert context["lista_de_animes_crescente"][1]["name"] == anime_2_cresc
    assert context["lista_de_animes_crescente"][1]["rating"] == nota_2_cresc
    # Checa se a nota é maior que a do item anterior
    assert context["lista_de_animes_crescente"][1]["rating"] > context["lista_de_animes_crescente"][0]["rating"]

    return context

@then(parsers.cfparse('o terceiro anime da lista crescente é "{anime_3_cresc}" com nota "{nota_3_cresc}"'), target_fixture="context")
def check_third_anime2(context, anime_3_cresc, nota_3_cresc):
    
    nota_3_cresc = float(nota_3_cresc)
    
    # Checa se está na lista
    assert context["lista_de_animes_crescente"][2]["name"] == anime_3_cresc
    assert context["lista_de_animes_crescente"][2]["rating"] == nota_3_cresc
    # Checa se a nota é maior que a do item anterior
    assert context["lista_de_animes_crescente"][2]["rating"] > context["lista_de_animes_crescente"][1]["rating"]







# SEGUNDO TESTE

@scenario(scenario_name="Mudar quantidade máxima de itens na lista", feature_name="../features/mais_bem_avaliados.feature")
def test_change_best_rated_list_size_limit():
    """"Mudar quantidade máxima de itens na lista"""

@given(parsers.cfparse('estou na página Mais Bem Avaliados'))
def check_current_page():
    pass

@then(parsers.cfparse('eu vejo uma lista de animes contendo "{qtd_itens}" itens'), target_fixture="context")
def mock_get_anime_list(qtd_itens: int):
    
    qtd_itens = int(qtd_itens)
    context = {}
    context["lista_de_animes"] = best_rated.order_best_rated("decrescente", qtd_itens)

    assert isinstance(context["lista_de_animes"], list)

    return context

@then(parsers.cfparse('o primeiro anime da lista de "{qtd_itens}" itens é "{anime_1}" com nota "{nota_1}"'), target_fixture="context")
def check_first_anime(context, qtd_itens: int, anime_1: str, nota_1: float):
    
    nota_1 = float(nota_1)

    # Checa se está na lista
    assert context["lista_de_animes"][0]["name"] == anime_1
    assert context["lista_de_animes"][0]["rating"] == nota_1

    return context

@then(parsers.cfparse('o segundo anime da lista de "{qtd_itens}" itens é "{anime_2}" com nota "{nota_2}"'), target_fixture="context")
def check_second_anime(context, qtd_itens: int, anime_2: str, nota_2: float):
    
    nota_2 = float(nota_2)

    # Checa se está na lista
    assert context["lista_de_animes"][1]["name"] == anime_2
    assert context["lista_de_animes"][1]["rating"] == nota_2

    return context

@then(parsers.cfparse('o terceiro anime da lista de "{qtd_itens}" itens é "{anime_3}" com nota "{nota_3}"'), target_fixture="context")
def check_third_anime(context, qtd_itens: int, anime_3: str, nota_3: float):
    
    nota_3 = float(nota_3)
    
    # Checa se está na lista
    assert context["lista_de_animes"][2]["name"] == anime_3
    assert context["lista_de_animes"][2]["rating"] == nota_3

    return context

@when(parsers.cfparse('eu mudo o limite de itens na lista para "{limite}"'), target_fixture="context")
def change_item_limit(limite):
    
    context = {}
    context["limite"] = limite
    context["lista_de_animes"] = best_rated.order_best_rated("decrescente", int(limite))

    assert isinstance(context["lista_de_animes"], list)

    return context

@then(parsers.cfparse('o primeiro anime da lista limitada é "{anime_1}" com nota "{nota_1}"'), target_fixture="context")
def check_first_anime2(context, anime_1: str, nota_1: float):
    
    nota_1 = float(nota_1)

    # Checa se está na lista
    assert context["lista_de_animes"][0]["name"] == anime_1
    assert context["lista_de_animes"][0]["rating"] == nota_1

    return context

@then(parsers.cfparse('o segundo anime da lista limitada é "{anime_2}" com nota "{nota_2}"'), target_fixture="context")
def check_second_anime2(context, anime_2: str, nota_2: float):
    
    nota_2 = float(nota_2)

    # Checa se está na lista
    assert context["lista_de_animes"][1]["name"] == anime_2
    assert context["lista_de_animes"][1]["rating"] == nota_2

    return context

@then(parsers.cfparse('o terceiro anime da lista não é retornado'), target_fixture="context")
def check_third_anime2(context):
    
    assert len(context["lista_de_animes"]) == int(context["limite"])