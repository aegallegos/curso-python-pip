from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import store

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_root():
    return """
        <h1>Esta es la pagina de inicio</h1>
        <p>Para ver los contactos, vaya a <a href="/contact">/contact</a></p>
        <p>Para ver las categorias, vaya a <a href="/categories">/categories</a></p>
    """
    
@app.get("/contact")
def get_contacts():
    return store.get_contacts()

@app.get("/categories")
def categories():
    return store.get_categories()

def run():
    store.get_categories()

if __name__ == '__main__':
    run()