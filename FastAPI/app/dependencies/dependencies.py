
from fastapi import HTTPException
from typing import Annotated
from fastapi import Header

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def get_query_token(token: str):
    if token != "thinh":
        raise HTTPException(status_code=400, detail="No thinh token provided")