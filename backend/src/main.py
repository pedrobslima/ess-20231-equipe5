from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status
from src.api.router import api_router
from fastapi.responses import HTMLResponse
from src.schemas.response import HttpResponseModel
from src.service.impl.item_service import ItemService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"GET": "Bem vindo à ela inicial!"}

@app.get("/{post_id}", 
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
    })
async def posts(post_id):
    '''
    Get post by ID
    Parameters:
    - post_id: The ID of the post to retrieve.

    Returns:
    - The post with the specified ID.

    Raises:
    - HTTPException 404: If the post is not found.
    '''
    item_get_response = ItemService.get_item(post_id)
    return item_get_response

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