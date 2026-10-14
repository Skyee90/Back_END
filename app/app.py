from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostCreate
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run when the application starts
    await create_db_and_tables()

    yield

    # Run when the application shuts down
    pass



app = FastAPI(lifespan=lifespan)

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit is not None:
        return dict(list(text_posts.items())[:limit])
    return text_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    post = text_posts.get(post_id)
    if post:
        return text_posts.get(post_id)
    else:
        return {"error": "Post not found"}

@app.post("/posts")
def create_post(post: PostCreate):
    new_id = max(text_posts.keys(), default=0) + 1
    new_post = {"title": post.title, "content": post.content, "published": post.published}
    text_posts[new_id] = new_post
    return new_post

