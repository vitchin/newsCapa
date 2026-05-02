import requests as res
from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

API_KEY = os.getenv("NEWS_API_KEY", "a8ea83f2550941a5b5a757b5bbd6ca7a")
BASE_URL = "https://newsapi.org/v2/everything" #ajustar o endpoint correto

@app.route('/')
@app.route('/index.html')
def index():

    sort_by = request.args.get('sortBy', 'publishedAt')
    pesquisa = request.args.get('q', '')

    parametros = {
        "qInTitle": pesquisa,
        "language": "pt",
        "sortBy": sort_by,
        "pageSize": 20,
        "apiKey": API_KEY
    }

    try: 
        response = res.get(BASE_URL, params=parametros, timeout=10)
        
        #case !=200
        response.raise_for_status()

        data=response.json()

        noticias=data.get('articles', [])

        for noticia in noticias:

            noticia['publishedAt'] = date_formated(noticia.get('publishedAt', ''))
    
    except res.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        noticias = []


    return render_template('index.html', noticias=noticias, pesquisa=pesquisa, sort_by=sort_by)

def date_formated(date_iso):

    try:
        date = datetime.strptime(date_iso, "%Y-%m-%dT%H:%M:%SZ")

        return date.strftime("%d/%m/%Y às %H:%M")
    
    except:
        return "Data indisponivel"

if __name__ == '__main__':
    app.run(debug=True)