import requests
import sys
import os


def obte_ciutat():
    """Retorna la ciutat que l'usuari ha introduït."""
    # Demanem a l'usuari el nom de la ciutat
    ciutat = input("🏙️ Introdueix el nom de la ciutat: ")
    print(f"\nS'ha triat la ciutat: {ciutat}.\n")
    return ciutat

def obte_temperatura(ciutat):
    """Retorna la temperatura que l'usuari ha introduït."""
    # Demanem a l'usuari la temperatura
    while True:
        try:
            temperatura = float(input("🌡️ Introdueix la temperatura en aquesta ciutat: "))
            print(f"\nLa ciutat {ciutat} podria tenir una temperatura de {temperatura} graus.\n")
            return temperatura
        except ValueError:
            print("\033[91mError: Heu d'introduir un valor numeric\033[0m")
    

def obtenir_temperatura(ciutat):
    """Retorna la temperatura actual a la ciutat especificada."""
    api_key = os.getenv("TOKEN_API")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciutat}&appid={api_key}&units=metric"
    try:
        resposta = requests.get(url)
        dades = resposta.json()
        temperatura = dades["main"]["temp"]
    except:
        return None
    return temperatura

def compara_temperatures(temperatura_real, temperatura_suposada, tolerancia=1, mode="facil"):
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
            missatge = f"Les temperatures estan dins de la tolerància. La temperatura real és més alta 👍"
        elif diferència < 0:
            misstage = f"Les temperatures estan dins de la tolerància. La temperatura real és més baixa 👍"
        else:
            missatge = f"Les temperatures estan exactament dins de la tolerància. Diferència: 👍"
    # Si la diferència no està dins de la tolerància
    else:
        if diferència > 0:
            missatge = f"Les temperatures no estan dins de la tolerància. La temperatura real és més alta 👎"
        elif diferència < 0:
            missatge = f"Les temperatures no estan dins de la tolerància. La temperatura real és més baixa 👎"

    if mode == "facil":
        missatge = missatge + f" per {diferència}°."
    print(missatge)

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "dificil":
            mode = "dificil"
        else:
            print("Mode erroni: Utilitza facil o dificil")
            return
    else:
        mode = "facil"

    ascii_art = """
 ▗▄▄▖▄▄▄  ▄▄▄▄  ▄▄▄▄  ▗▞▀▜▌ ▄▄▄ ▗▞▀▜▌▐▌ ▄▄▄   ▄▄▄           
▐▌  █   █ █ █ █ █   █ ▝▚▄▟▌█    ▝▚▄▟▌▐▌█   █ █              
▐▌  ▀▄▄▄▀ █   █ █▄▄▄▀      █      ▗▞▀▜▌▀▄▄▄▀ █              
▝▚▄▄▖           █                 ▝▚▄▟▌                     
                ▀                                           
▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖  ▗▄▖▗▄▄▄▖▗▖ ▗▖▗▄▄▖ ▗▄▄▄▖ ▗▄▄▖
  █  ▐▌   ▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌ █  ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌   
  █  ▐▛▀▀▘▐▌  ▐▌▐▛▀▘ ▐▛▀▀▘▐▛▀▚▖▐▛▀▜▌ █  ▐▌ ▐▌▐▛▀▚▖▐▛▀▀▘ ▝▀▚▖
  █  ▐▙▄▄▖▐▌  ▐▌▐▌   ▐▙▄▄▖▐▌ ▐▌▐▌ ▐▌ █  ▝▚▄▞▘▐▌ ▐▌▐▙▄▄▖▗▄▄▞▘  v0.1
                                                            
"""
    print(ascii_art)
    print(f"Estàs jugant en el mode: {mode}")

    ciutat = obte_ciutat()
    temperatura = obte_temperatura(ciutat)
    while True:
        maybe_temperatura_real = obtenir_temperatura(ciutat)
        if maybe_temperatura_real is None:
            print(f"Ciutat {ciutat} incorrecta")
            ciutat = obte_ciutat()
            continue
        # Estem segurs que la temperatura es un valor valid
        temperatura_real = maybe_temperatura_real
        compara_temperatures(temperatura_real, temperatura, mode=mode)
        break


if __name__ == "__main__":
    main()
