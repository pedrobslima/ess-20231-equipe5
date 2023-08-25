from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient
from base64 import b64encode
from src.tests.utils import req_type_to_function


@scenario(scenario_name="Criação de post simples", feature_name="../features/posts.feature")
def test_create_post():
    '''Creating a new post'''

@given(parsers.cfparse('Eu sou o usuário "{username}" e estou na página de criação de post "{url}"'),
       target_fixture="context")
def present_username(context, username, url):
    '''Getting the username and URL'''

    context = {}
    context["post"] = {}
    context["post"]["user"] = username
    context["url"] = url
    return context

@when(parsers.cfparse('Eu monto o meu post com título "{title}", tag "{tags}", corpo "{body}"'),
       target_fixture="context")
def select_new_post(context, title, tags, body):
    '''Getting the posts title, tag and body'''

    context["post"]["title"] = title
    context["post"]["tags"] = tags.split(", ")
    context["post"]["body"] = body
    return context

@when(parsers.cfparse('Faço uma requisição de "{req}" da minha publicação, para a rota atual'),
       target_fixture="context")
def send_post(client: TestClient, context, req):
    '''Posting the new post'''

    context["response"] = req_type_to_function(client, req)(url=context["url"], json=context["post"])

    return context

@then(parsers.cfparse('O status da resposta deve ser "{status}"'),
       target_fixture="context")
def check_status(context, status):
    '''Checking status code'''
    
    assert context["response"].status_code == int(status)

#-------------------------------------------------------

@scenario(scenario_name="Criação de post com imagem", feature_name="../features/posts.feature")
def test_create_post():
    '''Creating a new post with an image attached'''

@given(parsers.cfparse('Eu sou o usuário "{username}" e estou na página de criação de post "{url}"'),
       target_fixture="context")
def present_username(context, username, url):
    '''Getting the username and URL'''

    context = {}
    context["post"] = {}
    context["post"]["user"] = username
    context["url"] = url
    return context

@when(parsers.cfparse('Eu monto o meu post com título "{title}", tag "{tags}", corpo "{body}"'),
       target_fixture="context")
def select_new_post(context, title, tags, body):
    '''Getting the posts title, tag and body'''

    context["post"]["title"] = title
    context["post"]["tags"] = tags.split(", ")
    context["post"]["body"] = body
    return context

@when(parsers.cfparse('Anexo o arquivo "{filename}"'),
       target_fixture="context")
def select_img(context, filename):
    '''Attaching the contents of the image to the context in byte/base64 type'''
    file = open(f'src//tests//attached//{filename}', 'rb')
    context["post"]['img_filename'] = filename
    context["post"]['img_bytes'] = (b64encode(file.read())).decode()
    file.close()
    return context

@when(parsers.cfparse('Faço uma requisição de "{req}" da minha publicação, para a rota atual'),
       target_fixture="context")
def send_post(client: TestClient, context, req):
    '''Posting the new post'''

    context["response"] = req_type_to_function(client, req)(url=context["url"], json=context["post"])
    return context

@then(parsers.cfparse('O status da resposta deve ser "{status}"'),
       target_fixture="context")
def check_status(context, status):
    '''Checking status code'''
    
    assert context["response"].status_code == int(status)