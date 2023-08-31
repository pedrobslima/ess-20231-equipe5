from fastapi import APIRouter
from db.server import server_;

router = APIRouter()
@router.get('')
async def getFeed():
    recents = server_.getRecents()
    retrn = []

    for i in recents:
        retrn.append({'id': i})

    return {'posts': retrn}
    '''return {"posts":[
        {'id':7},
        {'id':6},
        {'id':5},
        {'id':4},
        {'id':3},
        {'id':2},
        {'id':1},
        {'id':0}]}'''