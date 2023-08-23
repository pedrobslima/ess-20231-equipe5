from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class UserPost(BaseModel):
    post_id: str
    user: str
    tags: list[str]
    title: str
    body: str
    img_name: str
    comments: list

class NewPost(BaseModel):
    user: str
    tags: list[str]
    title: str
    body: str
    img_filename: Optional[str] = None
    img_bytes: Optional[str] = None
    def assemble(self) -> dict:
        "Assembles the NewPost object into a dictionary"
        dictio = {}
        dictio['user'] = self.user
        dictio['tags'] = self.tags
        dictio['title'] = self.title
        dictio['body'] = self.body
        if(not self.img_bytes):
            dictio['img_filename'] = None
            dictio['img_bytes'] = None
        else:
            dictio['img_filename'] = str(uuid4()) + self.img_filename[self.img_filename.rfind('.'):]
            dictio['img_bytes'] = self.img_bytes
        dictio['comments'] = []
        return dictio
