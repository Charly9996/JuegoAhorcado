# ============================================================
# CAPA DE PRESENTACIÓN - Todo lo que ve el jugador
# ============================================================
# Esta capa se encarga de:
#   - Limpiar la pantalla para que no haga scroll
#   - Dibujar el monigote según los errores cometidos
#   - Mostrar la palabra oculta y las letras falladas
#   - Pedir la letra al jugador
# ============================================================

import os

# --- Los 7 estados del monigote (0 errores hasta 6 errores) ---
MONIGOTES = [
    # 0 errores
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    # 1 error - aparece la cabeza
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    # 2 errores - aparece el cuerpo
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # 3 errores - aparece el brazo izquierdo
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # 4 errores - aparece el brazo derecho
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    # 5 errores - aparece la pierna izquierda
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    # 6 errores - ahorcado completo, el jugador perdió
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]


def limpiar_pantalla():
    """Limpia la consola para que el juego no haga scroll."""
    os.system("cls")


def mostrar_estado(errores, palabra_oculta, letras_incorrectas, vidas):
    """
    Borra la pantalla y dibuja todo el estado del juego de nuevo.
    Así siempre se ve limpio y ordenado.
    """
    limpiar_pantalla()

    print("========================================")
    print("     JUEGO DEL AHORCADO")
    print("========================================")

    # Dibuja el monigote según cuántos errores lleva
    print(MONIGOTES[errores])

    # Muestra la palabra con guiones o letras según lo que adivinó
    print("  Palabra:  " + palabra_oculta)
    print()

    # Muestra las letras que ya falló
    if len(letras_incorrectas) == 0:
        print("  Letras falladas:  (ninguna todavia)")
    else:
        print("  Letras falladas:  " + " ".join(letras_incorrectas))

    # Muestra las vidas que quedan
    print("  Vidas restantes:  " + str(vidas))
    print()
    print("========================================")


def mostrar_resultado_final(gano, palabra_secreta):
    """Muestra el mensaje de victoria o derrota al terminar la partida."""
    limpiar_pantalla()

    if gano:
        print()
        print("  ===========================")
        print("  |  ¡¡ GANASTE !!          |")
        print("  ===========================")
    else:
        print(MONIGOTES[6])
        print("  ===========================")
        print("  |  ¡¡ PERDISTE !!         |")
        print("  |  La palabra era: " + palabra_secreta)
        print("  ===========================")
    print()


def pedir_letra():
    """
    Le pide al jugador que ingrese una letra.
    Si ingresa algo que no es una sola letra, vuelve a preguntar.
    """
    while True:
        letra = input("  Ingresa una letra: ").strip().lower()

        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("  ¡Solo puedes ingresar UNA letra!")


def avisar_letra_repetida(letra):
    """Avisa que esa letra ya fue jugada."""
    print("  Ya jugaste la letra '" + letra + "'. Intenta con otra.")
    input("  (Presiona Enter para continuar...)")
