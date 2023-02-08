from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"msg": "welcome to root"}


@app.get("/item/a")
def get_a():
    return {"msg": "welcome to a path"}


@app.get("/item/b")
def get_b():
    return {"msg": "welcome to b path"}


@app.get("/item/c")
def get_c():
    return {"msg": "welcome to c path"}


@app.post("/item/post")
def post_item():
    return {"msg": "post item"}