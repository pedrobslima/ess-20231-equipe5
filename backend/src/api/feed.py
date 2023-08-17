from fastapi import APIRouter
from db.server import server_;

router = APIRouter()
@router.get('')
async def getFeed():
    return {'posts': server_.getRecents()}
