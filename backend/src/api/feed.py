from fastapi import APIRouter
from db.server import server_;

router = APIRouter()
@router.get('')
async def getFeed():
    aux = server_.getRecents()
    print(aux)
    #return {'posts': aux}
    return {"posts":[7,6,5,4,3,2,1,0]}