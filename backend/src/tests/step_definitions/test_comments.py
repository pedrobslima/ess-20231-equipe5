from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient
from src.tests.utils import req_type_to_function

@scenario(scenario_name="Comentando uma Postagem", feature_name="../features/post_comment.feature")
def test_create_post():
    '''Posting a new comment on a post'''
    pass

@given(parsers.cfparse('Eu sou o usuário "{username}" e estou na página "{url}"'),
       target_fixture="context")
def present_username(context, username, url):
    '''Getting the username and URL'''

    context = {}
    context["comment"] = {}
    context["comment"]["user"] = username
    context["url"] = url
    return context

@when(parsers.cfparse('Eu monto o meu comentário com corpo "{body}"'),
       target_fixture="context")
def select_new_comment(context, body):
    '''Getting the posts title, tag and body'''

    context["comment"]["body"] = body
    return context

@when(parsers.cfparse('Faço uma requisição de "{req}" do meu comentário, para a rota atual'),
       target_fixture="context")
def send_comment(client: TestClient, context, req):
    '''Posting the new comment'''

    context["response"] = req_type_to_function(client, req)(url=context["url"], json=context["comment"])
    
    return context

@then(parsers.cfparse('O status da resposta deve ser "{status}"'),
       target_fixture="context")
def check_status(context, status):
    '''Checking status code'''
    
    assert context["response"].status_code == int(status)