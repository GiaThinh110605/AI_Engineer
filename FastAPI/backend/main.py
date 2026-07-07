from fastapi import status
from numpy import full
from pydantic import EmailStr
from pydantic import HttpUrl
from typing import Literal
from pydantic import AfterValidator
from typing import Annotated
from fastapi import FastAPI, Query, Path, Body, Header, Cookie, Response, Form
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse, RedirectResponse
from enum import Enum
import random
from typing import Any

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "good"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return { "item_id": item_id }

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# items=[{"item_name": "Thinh", "item_name": "Huy", "item_name": "Nhi"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return items[skip: skip + limit]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is a long description"})
#     return item

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is a long description"})
#     return item
    
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(title="thinh", description="query to learn", alias="item-query",max_length=50, pattern="^fixedquery$" )] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn", "imdb")):
        raise ValueError("Invalid ID")
    return id

# @app.get("/items/")
# async def read_items(id: Annotated[str|None, AfterValidator(check_valid_id)] = None):
#     if id:
#         item = data.get(id)
#     else:
#         id, item = random.choice(list(data.items()))
#     return {"id": id, "name": item}

# @app.get("/items/{item_id}")
# async def read_items(q: str, item_id: Annotated[float, Path(title="KKK", ge=1, le=10.5)]):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# class FilterParams(BaseModel):
#     model_config = { "extra": "forbid" }
#     limit: int = Field(100, gt=0, le=100)
#     skip: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []

# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(*, q: str | None = None,item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
#     results = {"item_id": item_id, "item": item, "user": user}
#     if q:
#         results.update({"q": q})
#     return results

# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     images: list[Image] | None = None

# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]

# @app.put("/items/{item_id}")
# async def update_item(offer: Offer):
#     return offer


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# @app.get("/items/")
# async def read_items(user_agent: Annotated[str | None, Header(convert_underscores=False)] = None):
#     return {"User-Agent": user_agent}

# class Cookies(BaseModel):
#     model_config = {"extra": "forbid"}
#     session_id: str
#     facebook_tracker: str | None = None
#     googleall_tracker: str | None = None

# @app.get("/items/")
# async def read_items(cookies: Annotated[Cookies, Cookie()]):
#     return cookies

# class CommonHeaders(BaseModel):
#     model_config = { "extra": "forbid" }
#     host: str
#     save_data: bool
#     if_modified_since: str | None = None
#     traceparent: str | None = None
#     x_tag: list[str] = []

# @app.get("/items/")
# async def read_items(
#     headers: Annotated[CommonHeaders, Header(convert_underscores=False)]
# ):
#     return headers

# Chỉ trả về những cái cần thiết
# class UserIn(BaseModel):
#     user_name: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# # không trả về password
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# @app.post("/user/", response_model=UserOut) # không trả về password
# async def create_user(user: UserIn) -> Any:
#     return user

# @app.get("/portal", response_model=None) # response_model=None để tắt kiểm tra pydantic
# async def get_portal(teleport: bool = False) -> Response | dict:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []

# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }

# # response_model_exclude_unset=True: không trả về những cái không được gán giá trị
# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True) 
# async def read_item(item_id: str):
#     return items[item_id]

# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# class UserIn(UserBase):
#     password: str

# class UserOut(UserBase):
#     pass

# class UserInDB(UserBase):
#     hashed_password: str

# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password

# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(
#         **user_in.model_dump(),
#         hashed_password=hashed_password
#     )
#     print(user_in_db)
#     return user_in_db

# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

# class Item(BaseModel):
#     name: str
#     description: str

# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"}
# ]

# @app.get("/items/", response_model=list[Item])
# async def read_items():
#     return items

# @app.get("/keyword-weights/", response_model=dict[str, float])
# async def read_keyword_weights():
#     return {"foo": 2.3, "bar": 3.4}

# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# async def create_item(name: str):
#     return {"name": name}

class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data