import requests
import sys
import os


def obte_ciutat():
    """Retorna la ciutat que l'usuari ha introduït."""
    # Demanem a l'usuari el nom de la ciutat
    ciutat = input("Introdueix el nom de la ciutat: ")
    # Mostrem la informació amb format
    print(f"\nS'ha triat la ciutat: {ciutat}.\n")
    return ciutat

def obte_temperatura(ciutat):
    """Retorna la temperatura que l'usuari ha introduït."""
    # Demanem a l'usuari la temperatura
    while True:
        try:
            temperatura = float(input("Introdueix la temperatura en aquesta ciutat: "))
            print(f"\nLa ciutat {ciutat} podria tenir una temperatura de {temperatura} graus.\n")
            return temperatura
            break
        except ValueError:
            print("\033[91mError: Heu d'introduir un valor numeric\033[0m")
            # Mostrem la informació amb format
#Tornem a executar la funcio
    

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
    diferència = abs(temperatura_real - temperatura_suposada)
    if diferència <= tolerancia:
        print(f"Les temperatures estan dins de la tolerància. Diferència: {diferència}°")
    else:
        print(f"Les temperatures no estan dins de la tolerància. Diferència: {diferència}°")

def main():
    print("SUPER COMPARADOR DE TEMPERATURES\n")
    ciutat = obte_ciutat()
    temperatura = obte_temperatura(ciutat)
    #temperatura_real = obtenir_temperatura(ciutat)
    #compara_temperatures(temperatura_real, temperatura)


if __name__ == "__main__":
    main()
