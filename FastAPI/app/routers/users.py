from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def read_users():
    return [{"username": "Thinh"}, {"username": "Duong"}]

@router.get("/me")
async def read_user_me():
    return {"username": "thinh"}

@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}