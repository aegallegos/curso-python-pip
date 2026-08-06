from fastapi import FastAPI 
import store

app = FastAPI()

@app.get("/categories")
def categories():
    return store.get_categories()


if __name__ == '__main__':
    pass