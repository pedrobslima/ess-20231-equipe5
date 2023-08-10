from fastapi import FastAPI
from banco_de_animes.classe_anime import lista_animes 

app = FastAPI()

banco_animes = lista_animes

@app.get('/em-alta')
def listar_animes():
    #nomes_animes = []
    #for i in banco_animes:
    #    nomes_animes.append(i.nome_anime)
    return banco_animes
    #return nomes_animes