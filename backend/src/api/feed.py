from fastapi import APIRouter
from db.server import server_;

router = APIRouter()
@router.get('')
async def getFeed():
    aux = server_.getRecents()
    print(aux)
    #return {'posts': aux}
    #return {"posts":[7,6,5,4,3,2,1,0]}
    return {"posts":[
        {'id':7},
        {'id':6},
        {'id':5},
        {'id':4},
        {'id':3},
        {'id':2},
        {'id':1},
        {'id':0}]}