# Juego del Ahorcado — Python

Proyecto académico desarrollado en Python para la materia de **Lógica de Programación**.  
Implementa el clásico juego del Ahorcado en consola, aplicando una **Arquitectura en 3 Capas**.

---

## Estructura del Proyecto

```
JuegoAhorcado/
│
├── main.py                  # Punto de entrada del programa
│
├── capas/
│   |
│   ├── modelo.py            # Lógica de negocio (validación, estado del juego)
│   ├── control.py           # Game loop y coordinación de turnos
│   └── presentacion.py      # Interfaz de consola y monigote ASCII
│
├── data/
│   └── palabras.txt         # Banco de palabras del juego
│
├── diagramas/               # Diagramas de flujo y casos de uso
│
└── README.md
```

---

## Arquitectura en 3 Capas

| Capa             | Archivo           | Responsabilidad                                                       |
|------------------|-------------------|-----------------------------------------------------------------------|
| **Presentación** | `presentacion.py` | Dibuja la consola, el monigote ASCII y captura la entrada del usuario |
| **Control**      | `control.py`      | Mantiene el game loop y coordina los turnos entre capas               |
| **Modelo**       | `modelo.py`       | Valida letras, administra vidas y determina el estado del juego       |

---

> No se requieren librerías externas. Solo Python estándar.

---

## Características

-  Pantalla que se redibuja en tiempo real (sin scroll)
-  Monigote ASCII con 7 estados progresivos
-  6 vidas por partida
-  Banco de palabras externo en `.txt`
-  Detección de letras repetidas sin penalización
-  Opción de jugar múltiples partidas seguidas

---

## Materia

Lógica de Programación — Arquitectura en Capas aplicada a consola Python.
