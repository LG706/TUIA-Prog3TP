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
    def MAX(tateti , estado): return valor
        if problema.TEST-TERMINAL(estado) then
            return problema.UTILIDAD(estado,MAX)
        valor = -1
        forall acción in problema.ACCIONES(estado) do
            sucesor = problema.RESULTADO(estado, acción)
            valor = max(valor,
                        MIN(problema, sucesor)
        return valor

    def MIN(tateti, estado) return valor
        if problema.TEST-TERMINAL(estado) then
            return problema.UTILIDAD(estado,MAX)
        valor = +1
        forall acción in problema.ACCIONES(estado) do
            sucesor = problema.RESULTADO(estado, acción)
            valor = min(valor,
                        MAX(problema, sucesor)
        return valor

    
    if tateti.jugador(estado) == MAX:
        sucs = {acción: estrategia_minimax-MIN(tateti, tateti.resultado(estado, acción))
            for acción in tateti.acciones(estado)}
        return max(sucs, key=sucs.get) # obtiene la clave con el mayor valor
    if tateti.jugador(estado) == MIN:
        sucs = {acción: estrategia_minimax-MAX(tateti, tateti.resultado(estado, acción))
            for acción in tateti.acciones(estado)}
        return min(sucs, key=sucs.get) # obtiene la clave con el menor valor

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