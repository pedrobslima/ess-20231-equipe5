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

@when(parsers.cfparse('uma requisição GET for enviada para "/{route}"'))
def func2(context, route):
    context['response'] = requests.get(url + f"{route}")
    pass

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'))
def func3(context, status_code):
    assert context['response'].status_code == int(status_code)
    pass

@then(parsers.cfparse('o JSON da resposta deve ser uma lista composta por {key}'))
def func4(context, key):
    context['post_ids'] = context['response'].json()['posts']

    for post_id in context['post_ids']:
        dict_key = list(post_id.keys())[0]
        assert dict_key == key

    pass

@then(parsers.cfparse('o post com id "{post_id}" tem posição "{post_position}" na lista'))
def func5(context, post_id, post_position):
    actual_position = context['post_ids'].index({'id': int(post_id)})
    assert actual_position == int(post_position)

