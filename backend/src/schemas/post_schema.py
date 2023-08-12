from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserPost(BaseModel):
    post_id: str
    user: str
    tags: list
    title: str
    body: str
    img_name: str
    comments: list

class NewPost(BaseModel):
    user: str
    tags: list = []
    title: str
    body: str

def assemble(post: NewPost, img_name: str = "") -> dict:
    "Assembles the NewPost object into a dictionary"
    dictio = {}
    dictio['user'] = post.user
    dictio['tags'] = post.tags
    dictio['title'] = post.title
    dictio['body'] = post.body
    dictio['image'] = img_name
    dictio['comments'] = []
    return dictio