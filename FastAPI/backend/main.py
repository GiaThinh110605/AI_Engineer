from typing import Literal
from pydantic import AfterValidator
from typing import Annotated
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from enum import Enum
import random

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

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}")
async def update_item(*, q: str | None = None,item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
    results = {"item_id": item_id, "item": item, "user": user}
    if q:
        results.update({"q": q})
    return results