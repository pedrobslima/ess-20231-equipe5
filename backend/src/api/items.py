from fastapi import APIRouter, status, File, UploadFile
from src.api.router import api_router
from src.schemas.response import HttpResponseModel
from src.service.impl.item_service import ItemService
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get(
    "/{item_id}", 
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an item by its ID",
    tags=["items"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got item by id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Item not found",
        }
    },
)
def get_item(item_id: str) -> HttpResponseModel:
    """
    Get item by ID.

    Parameters:
    - item_id: The ID of the item to retrieve.

    Returns:
    - The item with the specified ID.

    Raises:
    - HTTPException 404: If the item is not found.

    """
    item_get_response = ItemService.get_item(item_id)
    return item_get_response


@router.get("/")
async def root():
    return {"GET": "Bem vindo à ela inicial!"}

@router.get("/animes")
async def animes():
    return {"GET": "receber animes organizados por 'default' "}


@router.get("/animes/{order_by}")
async def animes_param(order_by):
    retorno = "receber animes organizados por '{0}' ".format(str(order_by))
    return {"GET": retorno}

@router.get("/home")
async def home():
    html_content = """
    <html>
        <head>
            <title>titulo</title>
        </head>
        <body>
            <h1>Tela inicial</h1>
            <input type='text' placeholder='pesquisar anime'>
            <button>pesquisar</button>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
