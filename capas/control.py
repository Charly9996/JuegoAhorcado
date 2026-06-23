# ============================================================
# CAPA DE CONTROL - El director del juego
# ============================================================
# Esta capa se encarga de:
#   - Arrancar y manejar el ciclo principal del juego
#   - Recibir la letra del jugador (desde Presentación)
#   - Enviarla al Modelo para verificarla
#   - Pedirle a Presentación que actualice la pantalla
#   - Preguntar si el jugador quiere jugar otra vez
# ============================================================

import capas.modelo as modelo
import capas.presentacion as pantalla


def jugar_partida(lista_palabras):
    """
    Maneja una partida completa de principio a fin.
    El ciclo corre mientras el jugador tenga vidas y no haya ganado.
    """

    # Preparar una partida nueva (elige palabra, reinicia vidas)
    modelo.nueva_partida(lista_palabras)

    # --- Ciclo principal del juego ---
    # Se repite mientras el jugador no haya ganado ni perdido
    while not modelo.jugador_gano() and not modelo.jugador_perdio():

        # 1. Calcular cuántos errores lleva (para elegir el monigote)
        errores = 6 - modelo.vidas

        # 2. Mostrar el estado actual en pantalla
        pantalla.mostrar_estado(
            errores,
            modelo.obtener_palabra_oculta(),
            modelo.letras_incorrectas,
            modelo.vidas
        )

        # 3. Pedir una letra al jugador
        letra = pantalla.pedir_letra()

        # 4. Revisar si esa letra ya fue jugada antes
        if modelo.letra_ya_fue_usada(letra):
            pantalla.avisar_letra_repetida(letra)
            continue   # Volver al inicio del ciclo sin gastar un turno

        # 5. Verificar la letra en el modelo
        modelo.verificar_letra(letra)

    # --- El ciclo terminó: mostrar resultado ---
    pantalla.mostrar_resultado_final(modelo.jugador_gano(), modelo.palabra_secreta)


def preguntar_revancha():
    """
    Pregunta si el jugador quiere jugar otra partida.
    Devuelve True si dice que sí, False si dice que no.
    """
    while True:
        respuesta = input("  ¿Quieres jugar de nuevo? (s/n): ").strip().lower()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("  Escribe 's' para sí o 'n' para no.")
