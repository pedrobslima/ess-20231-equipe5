from fastapi import APIRouter, Query, status, File, UploadFile
from db.server import server_;
from schemas.response import HttpResponseModel
from service.impl.search_service import SearchService
#from schemas.post_schema import NewPost

router = APIRouter()
#D:\Users\pbsl\Documents\GitHub\ess-20231-equipe5\backend
@router.get('/', 
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an post by its ID",
    tags=["user post"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got post by id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Post not found",
        }
    })
async def search_for_tags(tags: str = Query(None)):

    return SearchService.search_for_tags(tags.split(','))


@router.get('/all')
async def get_data():
    retorno = server_.getAllPosts()
    print(retorno)
    return retorno