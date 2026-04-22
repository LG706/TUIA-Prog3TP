"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    # TODO: Implementar algoritmo minimax

    # INSTRUCCIONES:
    # 1. Eliminar la línea 'raise NotImplementedError...' de abajo
    # 2. Implementar el algoritmo minimax aquí
    # 3. La función debe retornar una tupla (fila, columna) con la mejor jugada

    #desde aca agregue cosas con las funciones max y min comentados funciona pero nunca responde la ia con un movimiento
#def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    """
    
    def max_value(estado_actual):
        # Usamos el nombre exacto: test_terminal
        if tateti.test_terminal(estado_actual):
            return tateti.utilidad(estado_actual, JUGADOR_MAX)
        
        v = float('-inf')
        for accion in tateti.acciones(estado_actual):
            v = max(v, min_value(tateti.resultado(estado_actual, accion)))
        return v

    def min_value(estado_actual):
        if tateti.test_terminal(estado_actual):
            # Calculamos la utilidad siempre desde la perspectiva de MAX 
            # para que los valores sean consistentes (1 gana MAX, 0 pierde MAX)
            return tateti.utilidad(estado_actual, JUGADOR_MAX)
        
        v = float('inf')
        for accion in tateti.acciones(estado_actual):
            v = min(v, max_value(tateti.resultado(estado_actual, accion)))
        return v

    # --- Lógica de selección de la mejor jugada ---
    jugador_actual = tateti.jugador(estado)
    acciones_posibles = tateti.acciones(estado)

    if jugador_actual == JUGADOR_MAX:
        # MAX quiere la jugada que le devuelva el mayor valor
        return max(acciones_posibles, key=lambda a: min_value(tateti.resultado(estado, a)))
    else:
        # MIN quiere la jugada que le devuelva el menor valor para MAX
        return min(acciones_posibles, key=lambda a: max_value(tateti.resultado(estado, a)))
       
    #Hasta aca, lo de abajo estaba y lo comente para no borrarlo
    """
    la comento para no borrarla

    raise NotImplementedError(
        "\n" + "="*60 +
        "\n🚫 ALGORITMO MINIMAX NO IMPLEMENTADO" +
        "\n" + "="*60 +
        "\n\nPara usar la estrategia Minimax debe implementarla primero." +
        "\n\nInstrucciones:" +
        "\n1. Abra el archivo 'estrategias.py'" +
        "\n2. Busque la función 'estrategia_minimax()'" +
        "\n3. Elimine la línea 'raise NotImplementedError(...)'" +
        "\n4. Implemente el algoritmo minimax" +
        "\n\nMientras tanto, use la 'Estrategia Aleatoria'." +
        "\n" + "="*60
    )
    """