from pytest_bdd import parsers, given, when, then, scenario
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.impl.item_service import ItemService
from fastapi.testclient import TestClient