from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from api.search import router as search_router
from api.post import router as post_router
from api.emalta import router as emAlta_router
from api.most_views import router as most_views_router
from api.best_rated import router as best_rated_router
from api.feed import router as feed_router


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=origins,
)

app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(post_router, prefix="/post", tags=["user post"])
app.include_router(emAlta_router, prefix="/emalta", tags=['Em Alta'])
app.include_router(most_views_router, prefix="/mais-vistos", tags=['mais vistos'])
app.include_router(best_rated_router, prefix="/mais-bem-avaliados", tags=["mais bem avaliados"])
app.include_router(feed_router, prefix="/feed", tags=["feed"])

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777)

@app.get('/')
async def SearchTags():
    return {'resposta': 'Bem Vindo!'}
