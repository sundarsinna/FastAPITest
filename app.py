from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel,Field
from fastapi import status
from fastapi import HTTPException

#Create class variable
app = FastAPI(title="My First fast API Test Program")

@app.get("/Sundar")
def root():
    return {"message" : "Hellp Fast API"}

@app.get("/users/{userid}") #{userid} is a variable
def getusername(userid: int):
    return {"UserName" : userid, "type" : str(type(userid))}

@app.get("/search") #Get multiple parameter
def search(q: str, page: int = 1, limit: int = 10):
    return {"q": q, "page" : page, "limit" : limit}


class UserCreate(BaseModel):
    name: str
    email: str
    age: int | None = None

@app.post("/users")
def create_user(payload: UserCreate):
    return {"Created" : True, "user" : payload.model_dump()}


class CreateProduct(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

@app.post("/products")
def create_product(p: CreateProduct):
    return p.model_dump()

@app.post("/items",status_code=status.HTTP_201_CREATED)
def create_item():
    return {"created" : True}

FAKE_DB={1: "Sundar", 2: "Haasini"}

@app.get("/users/db/{user_id}")
def userfromdb(user_id: int):
    if user_id not in FAKE_DB:
        raise HTTPException(status_code=404, detail = "user not found")
    return {"id" : user_id, "name" : FAKE_DB[user_id]}