from fastapi.security import OAuth2PasswordRequestForm
from fastapi.types import DependencyCacheKey
from cv2 import TonemapMantiuk
from fastapi.openapi.models import OAuth2
from fastapi import responses
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi import Request
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi import UploadFile
from fastapi import status
from numpy import full
from pydantic import EmailStr
from pydantic import HttpUrl
from typing import Literal
from pydantic import AfterValidator
from typing import Annotated
from fastapi import FastAPI, Query, Path, Body, Header, Cookie, Response, Form, File
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse, RedirectResponse
from enum import Enum
import random
from typing import Any
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from datetime import timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
import time
from fastapi.middleware.cors import CORSMiddleware

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

# class FormData(BaseModel):
#     username: str
#     password: str
#     model_config = {"extra": "forbid"}

# @app.post("/login/")
# async def login(data: Annotated[FormData, Form()]):
#     return data

# # file lưu ở ram (bộ nhớ tạm)
# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
#     return {"file_size": len(file)}

# # file nhẹ thì lưu ở ram (bộ nhớ tạm), file nặng thì lưu ở disk (ổ cứng)
# @app.post("/uploadfile/")
# async def create_upload_file(file: Annotated[UploadFile, File(description="kkk")]):
#     return {"filename": file.filename}

# @app.post("/files/")
# async def create_files(files: Annotated[list[bytes], File()]):
#     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")
# async def create_upload_files(files: list[UploadFile]):
#     return {"filenames": [file.filename for file in files]}


# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)

# @app.post("/files/")
# async def create_file(
#     file: Annotated[bytes, File()],
#     fileb: Annotated[UploadFile, File()],
#     token: Annotated[str, Form()]
# ):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb": fileb.content_type
#     }

# items = {"Gia Thinh": "He is very handsome"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
# #         raise HTTPException(
# #             status_code=404, 
# #             detail="Item not found",
# #             headers={"X-Error": "kkk"}
# #         )
# #     return {"item": items[item_id]}

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name

# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )

# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}

# # xử lý http chuẩn (như 404, 401, 500)
# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# # xử lý lỗi dữ liệu đầu vào
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc: RequestValidationError):
#     message = "Validation Error:"
#     for error in exc.errors():
#         message += f"\nField: {error['loc']}, Error: {error['msg']}"
#     return PlainTextResponse(message, status_code=400)

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3")
#     return {"item_id": item_id}

# fake_db = {}

# class Item(BaseModel):
#     title: str
#     timestamp: datetime
#     description: str | None = None

# @app.put("/items/{id}")
# def update_item(id: str, item: Item):
#     js = jsonable_encoder(item)
#     fake_db[id] = js

# @app.get("/items/")
# def get_items():
#     return fake_db

# class Item(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None
#     tax: float = 10.5
#     tags: list[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]


# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     print(item)
#     update_item_encoded = jsonable_encoder(item)
#     print(update_item_encoded)
#     items[item_id] = update_item_encoded
#     return update_item_encoded

# class Item(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None
#     tax: float = 10.5
#     tags: list[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]


# @app.patch("/items/{item_id}")
# async def update_item(item_id: str, item: Item) -> Item:
#     stored_item_data = items[item_id]
#     stored_item_model = Item(**stored_item_data)
#     update_data = item.model_dump(exclude_unset=True)
#     updated_item = stored_item_model.model_copy(update=update_data)
#     items[item_id] = jsonable_encoder(updated_item)
#     return updated_item



# fluffy = Cat(name="Mr Fluffy")
# print(fluffy.name)

# dependency: là callable (có thể gọi được)
# (something) hoặc () -> python chạy không lỗi là callable
# class Cat:
#     def __init__(self, name: str):
#         self.name = name
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# class CommonQueryParams:
#     def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit
    
# @app.get("/items/")
# async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
#     responses = {}
#     if commons.q:
#         responses.update({"q": commons.q})
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]
#     responses.update({"items": items})
#     return responses

# async def verify_token(x_token: Annotated[str, Header()]):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")


# async def verify_key(x_key: Annotated[str, Header()]):
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(status_code=400, detail="X-Key header invalid")
#     return x_key


# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [{"item": "Foo"}, {"item": "Bar"}]

# class InternalError(Exception):
#     pass


# def get_username():
#     try:
#         yield "Rick"
#     except InternalError:
#         print("Oops, we didn't raise again, Britney 😱")
#         raise


# @app.get("/items/{item_id}")
# def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
#     if item_id == "portal-gun":
#         raise InternalError(
#             f"The portal gun is too dangerous to be owned by {username}"
#         )
#     if item_id != "plumbus":
#         raise HTTPException(
#             status_code=404, detail="Item not found, there's only a plumbus here"
#         )
#     return item_id

# def get_username():
#     try:
#         yield "Rick"
#     finally:
#         print("Clean up before response is sent")

# @app.get("/users/me")
# def get_user_me(username: Annotated[str, Depends(get_username, scope='function')]):
#     return username

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None

# def fake_decode_token(token: str):
#     return User(
#         username=token + "fakedecoded", email="thinh@gmail.com",
#         full_name="Tran Gia Thinh", disabled=False
#     )

# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid authentication credentials")
#     return user

# @app.get("/users/me")
# async def read_user_me(current_user: Annotated[User, Depends(get_current_user)]):
#     return current_user

# from datetime import datetime, timedelta, timezone
# from typing import Annotated

# import jwt
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jwt.exceptions import InvalidTokenError
# from pwdlib import PasswordHash
# from pydantic import BaseModel

# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
#         "disabled": False,
#     }
# }


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# class UserInDB(User):
#     hashed_password: str


# password_hash = PasswordHash.recommended()

# DUMMY_HASH = password_hash.hash("dummypassword")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# app = FastAPI()


# def verify_password(plain_password, hashed_password):
#     return password_hash.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return password_hash.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         verify_password(password, DUMMY_HASH)
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except InvalidTokenError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)],
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token")
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
# ) -> Token:
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return Token(access_token=access_token, token_type="bearer")


# @app.get("/users/me/")
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ) -> User:
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.perf_counter()
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response
    
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
