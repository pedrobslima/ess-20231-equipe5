from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from uuid import uuid4

def create_id():
    "Returns a random id"
    return uuid4() 

class UserPost(BaseModel):
    post_id: str
    user: str
    tags: list
    title: str
    body: str
    attached: list
    comments: list

class NewPost(BaseModel):
    user: str
    tags: list
    title: str
    body: str
    attached: list

def assemble(post: NewPost) -> dict:
    "Assembles the NewPost object into a dictionary"
    dictio = {}
    dictio['user'] = post.user
    dictio['tags'] = post.tags
    dictio['title'] = post.title
    dictio['body'] = post.body
    dictio['attached'] = post.attached
    dictio['comments'] = []
    return dictio