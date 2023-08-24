from pytest_bdd import parsers, given, when, then, scenario
import pytest
import requests

url = 'http://localhost:8000/'

""" Scenario: Obter 10 ultimos posts decrescente """
@scenario(scenario_name="Obter 10 ultimos posts decrescente", feature_name="../features/feed.feature")
def test_get_feed():
    """ Get items by tag """
    pass

@given(parsers.cfparse('o ItemService retorna uma lista de id'))
def func1(context):
    pass

@when(parsers.cfparse('uma requisição GET for enviada para "/feed"'))
def func2(context):
    context['response'] = requests.get(url + "feed/")
    pass

@then(parsers.cfparse('o status da resposta deve ser "{200}"'))
def func3(context, param):
    pass

@then(parsers.cfparse('o JSON da resposta deve ser uma lista composta por id'))
def func4(context):
    pass

@then(parsers.cfparse('o post com id "{param1}" tem posição "{param2}" na lista'))
def func5(context):
    pass
