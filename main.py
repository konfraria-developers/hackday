import requests
import sys
import os


def obte_ciutat_i_temperatura():
    """Retorna la ciutat i la temperatura que l'usuari ha introduït."""
    return None, None

def obtenir_temperatura(ciutat):
    """Retorna la temperatura actual a la ciutat especificada."""
    api_key = os.getenv("TOKEN_API")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciutat}&appid={api_key}&units=metric"
    resposta = requests.get(url)
    dades = resposta.json()
    temperatura = dades["main"]["temp"]
    return temperatura

def compara_temperatures(temperatura_real, temperatura_suposada, tolerancia=1):
    """Calcula la diferència entre la temperatura real i la suposada i comprova si està dins de la tolerància."""
    pass

def main():
    ciutat, temperatura = obte_ciutat_i_temperatura()
    temperatura_real = obtenir_temperatura(ciutat)
    compara_temperatures(temperatura_real, temperatura)

if __name__ == "__main__":
    main()
