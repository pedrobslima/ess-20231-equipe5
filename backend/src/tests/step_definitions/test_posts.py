from pytest_bdd import parsers, given, when, then, scenario
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.impl.item_service import ItemService
from fastapi.testclient import TestClient
from base64 import b64encode

@scenario(scenario_name="Criação de post simples", feature_name="../features/posts.feature")
def test_create_post():
    '''Creating a new post'''

@given(parsers.cfparse('Eu estou na página "{page}"'))
def mock_initial_state_response(page: str):
    return page

@given(parsers.cfparse('Eu sou o usuário "{username}"'),
       target_fixture="context")
def present_username(context, username: str):
    '''Getting the username'''

    context["post"] = {}
    context["post"]["user"] = username
    return context

@given(parsers.cfparse('A tag "Review" já existe no sistema'))
def existent_tag():
    '''Stating that the tag exists'''
    pass

@when(parsers.cfparse('Seleciono a opção de criar um novo post'),
       target_fixture="context")
def select_new_post(context):
    '''Requesition URL'''

    context["req_url"] = '/post/new_post'
    return context

@when(parsers.cfparse('Com o título de post "{title}"'),
       target_fixture="context")
def choose_title(context, title: str):
    '''Choosing the title of the post'''

    context["post"]["title"] = title
    return context

@when(parsers.cfparse('Escolho a tag "{tag}"'),
       target_fixture="context")
def choose_tag(context, tag: str):
    '''Choosing the tag of the post'''

    context["post"]["tags"] = tag.split(', ')
    return context

@when(parsers.cfparse('Escrevo no corpo "{body}"'),
       target_fixture="context")
def write_body(context, body: str):
    '''Choosing the body of the post'''

    context["post"]["body"] = body
    return context

@then(parsers.cfparse('Minha review é publicada'),
       target_fixture="context")
def mock_post_request(client: TestClient, context):
    '''Mocking'''
    ItemService.create_post = lambda post: HttpResponseModel(
                message=HTTPResponses.ITEM_CREATED().message,
                status_code=HTTPResponses.ITEM_CREATED().status_code,
                data={
                    'user': 'pedro12', 
                    'tags': ['Review'], 
                    'title': 'Review episódio 1 de Jujutsu Kaisen', 
                    'body': 'Epiódio legal.', 
                    'img_filename': None, 
                    'img_bytes': None, 
                    'comments': []
                }
            )
    
    context["response"] = client.post(url=context["req_url"], json=context["post"])
    
    return context

@then(parsers.cfparse('Eu vejo o post do usuário "{username}" com título "{title}", com conteúdo "{body}" e tags "{tag}"'),
       target_fixture="context")
def final_check(context, username, title, body, tag, img_filename = None):
    '''Confirms the expected answer of:
        - user
        - title
        - body
        - tags
        - the lack of an image file'''
    
    posted = context['response'].json()['data']

    assert posted['user'] == username
    assert posted['title'] == title
    assert posted['body'] == body
    assert posted['tags'] == tag.split(', ')
    assert posted['img_filename'] == img_filename

    return context

#-------------------------------------------------------

@scenario(scenario_name="Criação de post com imagem", feature_name="../features/posts.feature")
def test_create_post():
    '''Creating a new post with an image attached'''

@given(parsers.cfparse('Eu estou na página "{page}"'))
def mock_initial_state_response(page: str):
    return page

@given(parsers.cfparse('Eu sou o usuário "{username}"'),
       target_fixture="context")
def present_username(context, username: str):
    '''Getting the username'''

    context["post"] = {}
    context["post"]["user"] = username
    return context

@given(parsers.cfparse('A tag "Review" já existe no sistema'))
def existent_tag():
    '''Stating that the tag exists'''
    pass

@when(parsers.cfparse('Seleciono a opção de criar um novo post'),
       target_fixture="context")
def select_new_post(context):
    '''Requesition URL'''

    context["req_url"] = '/post/new_post'
    return context

@when(parsers.cfparse('Com o título de post "{title}"'),
       target_fixture="context")
def choose_title(context, title: str):
    '''Choosing the title of the post'''

    context["post"]["title"] = title
    return context

@when(parsers.cfparse('Escolho a tag "{tag}"'),
       target_fixture="context")
def choose_tag(context, tag: str):
    '''Choosing the tag of the post'''

    context["post"]["tags"] = tag.split(', ')
    return context

@when(parsers.cfparse('Escrevo no corpo "{body}"'),
       target_fixture="context")
def write_body(context, body: str):
    '''Choosing the body of the post'''

    context["post"]["body"] = body
    return context


@when(parsers.cfparse('Seleciono a opção de anexar um arquivo local de mídia'))
def attach_img():
    '''Selecting option to attach image'''
    pass

@when(parsers.cfparse('Seleciono o arquivo "{filename}"'),
       target_fixture="context")
def select_img(context, filename):
    '''Attaching the contents of the image to the context in byte/base64 type'''
    file = open(f'src//tests//attached//{filename}', 'rb')
    context["post"]['img_filename'] = filename
    context["post"]['img_bytes'] = (b64encode(file.read())).decode()
    file.close()
    return context

@then(parsers.cfparse('Minha review com imagem é publicada'),
       target_fixture="context")
def mock_post_request(client: TestClient, context):
    '''Mocking'''
    ItemService.create_post = lambda post: HttpResponseModel(
                message=HTTPResponses.ITEM_CREATED().message,
                status_code=HTTPResponses.ITEM_CREATED().status_code,
                data={
                    'user': 'pedro12', 
                    'tags': ['Review'], 
                    'title': 'Review episódio 2 de Jujutsu Kaisen', 
                    'body': 'Essa segunda temporada de Jujutsu Kaisen está muito boa! Episódio fantástico!', 
                    #'img_filename': context["post"]['img_filename'], 
                    'img_bytes': context["post"]['img_bytes'], 
                    'comments': []
                }
            )
    
    context["response"] = client.post(url=context["req_url"], json=context["post"])

    return context

@then(parsers.cfparse('Eu vejo o post do usuário "{username}" com título "{title}" e conteúdo "{body}" e tags "{tag}"'),
       target_fixture="context")
def final_check(context, username, title, body, tag, img_filename = None):
    '''Confirms the expected answer of:
        - user
        - title
        - body
        - tags
        - contents of image sent'''

    posted = context['response'].json()['data']

    assert posted['user'] == username
    assert posted['title'] == title
    assert posted['body'] == body
    assert posted['tags'] == tag.split(', ')
    assert posted['img_bytes'] == context["post"]['img_bytes']
    
    return context