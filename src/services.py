import requests


def buscarClima(cidade="Brasilia"):
    try:
        # Usando a HG Brasil Weather
        base_url = "https://api.hgbrasil.com/weather?format=json"
        url = f"{base_url}&city_name={cidade}"
        resposta = requests.get(url)
        dados = resposta.json()

        temp = dados['results']['temp']
        condicao = dados['results']['description']
        return {"temp": temp, "condicao": condicao}
    except Exception:
        return None
