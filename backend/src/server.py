from fastapi import FastAPI
from banco_de_animes.classe_anime import lista_animes 

app = FastAPI()

banco_animes = lista_animes

@app.get('/em-alta')
def listar_animes():
    
    return banco_animes
    