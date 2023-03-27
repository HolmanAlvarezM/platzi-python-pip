import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/info_contact', response_class=HTMLResponse)
def get_list():
    # return {'name': "Holman Business SA"}
    return """
        <h1>Bienvenido a Holman Business</h1>
        <p>Esta es mi web personal</p>
    """

def run():
    store.get_categories()
    
if __name__ == "__main__":
    run()