from fastapi import APIRouter
from src.api import items, posts, comments

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(posts.router, prefix="/posts", tags=["user post"]) # se der errado mudar prefix para "/"
api_router.include_router(comments.router, prefix="/comments", tags=["items"])