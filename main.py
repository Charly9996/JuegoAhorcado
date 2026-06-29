# ============================================================
# JUEGO DEL AHORCADO - Versión en Python
# ============================================================
# Este archivo arranca el juego.
# Solo hace tres cosas:
#   1. Cargar las palabras del archivo .txt
#   2. Iniciar una partida
#   3. Preguntar si quiere jugar de nuevo
# ============================================================

import capas.modelo as modelo
import capas.control as control


# --- Ruta al archivo de palabras ---
RUTA_PALABRAS = "data/prueba.txt"


# --- Cargar las palabras una sola vez al inicio ---
lista_palabras = modelo.cargar_palabras(RUTA_PALABRAS)

# --- Bucle de sesión: permite jugar varias partidas seguidas ---
while True:
    control.jugar_partida(lista_palabras)

    # Preguntar si quiere otra partida
    if not control.preguntar_revancha():
        print()
        print("  ¡Hasta luego!")
        print()
        break
