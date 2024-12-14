import requests
import sys
import os


def obte_ciutat_i_temperatura():
    """Retorna la ciutat i la temperatura que l'usuari ha introduït."""
    print("SUPER COMPARADOR DE TEMPERATURES\n")
    # Demanem a l'usuari el nom de la ciutat
    ciutat = input("Introdueix el nom de la ciutat: ")

    # Demanem a l'usuari la temperatura
    temperatura = int(input("Introdueix la temperatura en aquesta ciutat: "))

    # Mostrem la informació amb format
    print(f"\nLa ciutat {ciutat} podria tenir una temperatura de {temperatura} graus.\n")
    return ciutat, temperatura

def obtenir_temperatura(ciutat):
    """Retorna la temperatura actual a la ciutat especificada."""
    api_key = os.getenv("TOKEN_API")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciutat}&appid={api_key}&units=metric"
    resposta = requests.get(url)
    dades = resposta.json()
    temperatura = dades["main"]["temp"]
    return temperatura

def compara_temperatures(temperatura_real, temperatura_suposada, tolerancia=1):
    """Calcula la diferència entre la temperatura real i la suposada i comprova si està dins de la tolerància,
    mostrant si la diferència és positiva o negativa i afegint emojis per indicar encerts o errors."""
    # Calcular la diferència entre les dues temperatures
    diferència = temperatura_real - temperatura_suposada  # La diferència pot ser positiva o negativa
    # Comprovar si les temperatures són exactament iguals
    if temperatura_real == temperatura_suposada:
        print(f"Les temperatures són exactament iguals. Diferència: 0°. 👍")
    
    # Comprovar si la diferència està dins de la tolerància
    elif abs(diferència) <= tolerancia:
        if diferència > 0:
            print(f"Les temperatures estan dins de la tolerància. La temperatura real és més alta per {diferència}°. 👍")
        elif diferència < 0:
            print(f"Les temperatures estan dins de la tolerància. La temperatura real és més baixa per {diferència}°. 👍")
        else:
            print(f"Les temperatures estan exactament dins de la tolerància. Diferència: {diferència}°. 👍")
    # Si la diferència no està dins de la tolerància
    else:
        if diferència > 0:
            print(f"Les temperatures no estan dins de la tolerància. La temperatura real és més alta per {diferència}°. 👎")
        elif diferència < 0:
            print(f"Les temperatures no estan dins de la tolerància. La temperatura real és més baixa per {diferència}°. 👎")

def main():
    ciutat, temperatura = obte_ciutat_i_temperatura()
    temperatura_real = obtenir_temperatura(ciutat)
    compara_temperatures(temperatura_real, temperatura)


if __name__ == "__main__":
    main()
