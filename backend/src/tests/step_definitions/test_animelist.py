from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient
import pytest
from banco_de_animes.classe_anime import Anime
from tests.utils import get_response_items_list


def test_send_request_emalta(client):

    '''Teste request Ok e se o corpo é uma lista'''
    response = client.get("/emalta")
    body = response.json()

    assert response.status_code == 200
    assert isinstance(body, list)

def test_list_anime(client):

    '''Teste se é uma lista de Animes'''

    response = client.get("/emalta")
    body = response.json()

    for i in body:
        assert isinstance(i, Anime)

#unit tests  



     

