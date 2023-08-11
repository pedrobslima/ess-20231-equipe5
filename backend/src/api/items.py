from fastapi import FastAPI, APIRouter, status
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


@router.get(
    "/", 
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve all items",
    tags=["items"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got all the items",
        }
    },
)
def get_items() -> HttpResponseModel:
    """
    Get all items.

    Returns:
    - A list of all items.

    """

    item_list_response = ItemService.get_items()
    
    return item_list_response


app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    return {"GET": "Bem vindo à ela inicial!"}

@app.get("/{post_id}", 
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve a post by its ID",
    tags=["items"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got post by id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Post not found",
        }
    })
async def get_post(post_id: str) -> HttpResponseModel:
    '''
    Get post by ID
    Parameters:
    - post_id: The ID of the post to retrieve.

    Returns:
    - The post with the specified ID.

    Raises:
    - HTTPException 404: If the post is not found.
    '''
    post_get_response = ItemService.get_item(post_id, 'posts')
    return post_get_response

@app.get("/{post_id}/comments", 
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve the comments in a post by its ID",
    tags=["items"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got post by id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Post not found",
        }
    })
async def get_comments(post_id: str) -> HttpResponseModel:
    '''
    Get comments by the posts ID
    Parameters:
    - post_id: The ID of the post.

    Returns:
    - The comments of the post with the specified ID.

    Raises:
    - HTTPException 404: If the post is not found.
    '''
    comms_get_response = ItemService.get_item(post_id, 'comments')
    return comms_get_response

@app.get("/animes")
async def animes():
    return {"GET": "receber animes organizados por 'default' "}


@app.get("/animes/{order_by}")
async def animes_param(order_by):
    retorno = "receber animes organizados por '{0}' ".format(str(order_by))
    return {"GET": retorno}

@app.get("/home")
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

#@app.post("/posts")
#async def publish():