from pytest_bdd import parsers, given, when, then, scenario
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.impl.item_service import ItemService
from fastapi.testclient import TestClient

@scenario(scenario_name="Comentando uma Postagem", feature_name="../features/post_comment.feature")
def test_create_post():
    '''Posting a new comment on a post'''
    pass

@given(parsers.cfparse('Eu estou na página "{page}"'))
def mock_initial_state_response(page: str):
    return page

@given(parsers.cfparse('eu sou o usuário "{username}"'),
       target_fixture="context")
def present_username(context, username: str):
    '''Getting the username'''

    context["comment"] = {}
    context["comment"]["user"] = username
    return context

@given(parsers.cfparse('na pagina inicial, há a postagem do usuario "{post_user}" de titulo "{post_title}", e id igual a "{post_id}"'),
       target_fixture="context")
def target_post(context, post_user, post_title, post_id):
    '''Description of the post about to be selected'''

    context["post_id"] = post_id
    context["post_user"] = post_user
    context["post_title"] = post_title

    return context

@when(parsers.cfparse('Seleciono o post'),
       target_fixture="context")
def select_post(client: TestClient, context):
    '''Getting the post, its information, and all of its comments'''

    context["url"] = f'/post/{context["post_id"]}'
    context["post"] = client.get(context["url"])
    
    assert context["post_id"] == context["post"].json()["data"]['id']
    assert context["post_user"] == context["post"].json()["data"]['user']
    assert context["post_title"] == context["post"].json()["data"]['title']

    return context

@when(parsers.cfparse('seleciono a opção de criar comentário'),
       target_fixture="context")
def start_new_comment(context):
    '''A new requisition URL for the new comment'''

    context["url"] = f"/comments/{context['post_id']}/new_comment"
    
    return context

@when(parsers.cfparse('escrevo no corpo "{body}"'),
       target_fixture="context")
def choose_tag(context, body: str):
    '''Choosing the body of the comment'''

    context["comment"]["body"] = body

    return context

@when(parsers.cfparse('seleciono publicar comentário'),
       target_fixture="context")
def post_comment(client: TestClient, context):
    '''Posting the comment'''
    
    context["POST_response"] = client.post(url=context["url"], json=context["comment"])

    return context

@then(parsers.cfparse('meu comentário foi publicado com o campo de usuário sendo "{user}", corpo sendo "{body}", na página do post de id "{id}"'),
       target_fixture="context")
def redirect_comm_post(client: TestClient, context, user, body, id):
    '''Redirecting to page of commented post and checking the comment'''
    
    context["url"] = f'/post/{id}'
    
    expected = {'id': context["POST_response"].json()["data"]['id'],
                'user': user,
                'body': body}

    context["GET_response"] = client.get(context["url"])
    
    comment_list = context["GET_response"].json()["data"]["comments"]

    assert (expected in comment_list)

    return context