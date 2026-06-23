# ============================================================
# CAPA DE MODELO - Lógica del juego
# ============================================================
# Esta capa se encarga de:
#   - Cargar las palabras del archivo .txt
#   - Elegir una palabra al azar
#   - Guardar el estado del juego (vidas, letras usadas)
#   - Verificar si una letra está en la palabra
# ============================================================

import random

# --- Variables del estado del juego ---
palabra_secreta = ""
letras_correctas = []    # Letras que el jugador acertó
letras_incorrectas = []  # Letras que el jugador falló
vidas = 6


def cargar_palabras(ruta):
    """Lee el archivo .txt y devuelve una lista de palabras."""
    archivo = open(ruta, "r", encoding="utf-8")
    palabras = []
    for linea in archivo:
        palabra = linea.strip().lower()
        if palabra != "":
            palabras.append(palabra)
    archivo.close()
    return palabras


def elegir_palabra(lista_palabras):
    """Elige una palabra al azar de la lista."""
    return random.choice(lista_palabras)


def nueva_partida(lista_palabras):
    """Reinicia todas las variables para empezar una partida nueva."""
    global palabra_secreta, letras_correctas, letras_incorrectas, vidas
    palabra_secreta    = elegir_palabra(lista_palabras)
    letras_correctas   = []
    letras_incorrectas = []
    vidas              = 6


def letra_ya_fue_usada(letra):
    """Revisa si la letra ya fue jugada antes (correcta o incorrecta)."""
    return letra in letras_correctas or letra in letras_incorrectas


def verificar_letra(letra):
    """
    Comprueba si la letra está en la palabra secreta.
    - Si está: la agrega a letras_correctas y devuelve True
    - Si no:  la agrega a letras_incorrectas, resta una vida y devuelve False
    """
    global vidas
    if letra in palabra_secreta:
        letras_correctas.append(letra)
        return True
    else:
        letras_incorrectas.append(letra)
        vidas = vidas - 1
        return False


def obtener_palabra_oculta():
    """
    Devuelve la palabra mostrando solo las letras adivinadas.
    Las letras que faltan se muestran como guión bajo _.
    Ejemplo: si la palabra es 'gato' y solo se adivinó la 'a'
             devuelve '_ a _ _'
    """
    resultado = ""
    for letra in palabra_secreta:
        if letra in letras_correctas:
            resultado = resultado + letra + " "
        else:
            resultado = resultado + "_ "
    return resultado.strip()


def jugador_gano():
    """Devuelve True si todas las letras de la palabra fueron adivinadas."""
    for letra in palabra_secreta:
        if letra not in letras_correctas:
            return False
    return True


def jugador_perdio():
    """Devuelve True si el jugador se quedó sin vidas."""
    return vidas <= 0
