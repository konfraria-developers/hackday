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
    pass

def compara_temperatures(temperatura_real, temperatura_suposada, tolerancia=1):
    """Calcula la diferència entre la temperatura real i la suposada i comprova si està dins de la tolerància."""
    diferència = abs(temperatura_real - temperatura_suposada)
    if diferència <= tolerancia:
        print(f"Les temperatures estan dins de la tolerància. Diferència: {diferència}°")
    else:
        print(f"Les temperatures no estan dins de la tolerància. Diferència: {diferència}°")

def main():
    ciutat, temperatura = obte_ciutat_i_temperatura()
    temperatura_real = obtenir_temperatura(ciutat)
    compara_temperatures(temperatura_real, temperatura)


if __name__ == "__main__":
    main()
