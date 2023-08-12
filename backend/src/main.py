from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status, File, UploadFile
from src.api.router import api_router
from fastapi.responses import HTMLResponse
from src.schemas.response import HttpResponseModel
from src.service.impl.item_service import ItemService
from src.schemas.post_schema import NewPost
from src.schemas.comnt_schema import NewComment

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
    description="Retrieve an post by its ID",
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
    post_get_response = ItemService.get_item(post_id)
    return post_get_response

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

@app.post("/new_post", response_model=HttpResponseModel,)
async def publish_post(post: NewPost, image: UploadFile = File(None)) -> HttpResponseModel:
    '''
    Post/Publish a post on the forum
    Parameters:
    - post: The post and its contents.
    - image (Optional): The image file attached to the post.

    Returns:
    - A message confirming the creation and storage of the post.

    Raises:
    - HTTPException 415: If the type of the sent file isn't a JPEG or a PNG
    - HTTPException 500: If the server can't generate a unique id for the post.
    '''
    if(image):
        content = await image.read()
        post_create_response = ItemService.create_post(post.assemble(image.filename), content)
    else:
        post_create_response = ItemService.create_post(post.assemble())
    return post_create_response

@app.post("/{post_id}/new_comment", response_model=HttpResponseModel,)
async def publish_comment(comment: NewComment, post_id: str) -> HttpResponseModel:
    '''
    Post a comment on a post from the forum
    Parameters:
    - comment: The comment and its contents.
    - post_id: The ID of the post being commented on.

    Returns:
    - A message confirming the creation and storage of the comment.

    Raises:
    - HTTPException 500: If the server can't generate a unique id for the comment.
    '''
    comnt_create_response = ItemService.create_comment(comment.assemble(), post_id)
    return comnt_create_response