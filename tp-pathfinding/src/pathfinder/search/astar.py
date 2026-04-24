from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # 1. Inicializar nodo raíz (punto de inicio)
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # 2. Calcular heurística para el nodo raíz (distancia a la meta)
        root.estimated_distance = abs(root.state[0] - grid.end[0]) + abs(root.state[1] - grid.end[1])

        # 3. Mantener registro de nodos ya visitados con su costo mínimo
        reached = {}
        reached[root.state] = root

        # 4. Inicializar frontera con el nodo raíz (cola de prioridad)
        # La prioridad es f = g + h (costo acumulado + heurística)
        frontier = PriorityQueueFrontier()
        frontier.add(root, priority=root.cost + root.estimated_distance)

        # 5. Bucle principal de exploración
        while not frontier.is_empty():
            # 6. Extraer el nodo con menor f = g + h
            # A* garantiza que siempre procesamos el camino más prometedor
            node = frontier.pop()

            # 7. Test de objetivo al DESENCOLAR (crucial en A*)
            # En A* verificamos al extraer porque podríamos haber encontrado
            # un camino más barato después de insertar el nodo
            if grid.objective_test(node.state):
                return Solution(node, reached)

            # 8. Expandir sucesores
            for action in grid.actions(node.state):
                child_state = grid.result(node.state, action)
                # 9. Calcular costo acumulado (costo del padre + costo de la celda)
                child_cost = node.cost + grid.individual_cost(node.state, action)

                # 10. Calcular heurística (distancia Manhattan a la meta)
                estimated_distance = abs(child_state[0] - grid.end[0]) + abs(child_state[1] - grid.end[1])

                # 11. Si no fue alcanzado O encontramos un camino más barato
                # Esto es crucial: si ya visitamos el nodo pero encontramos
                # un camino más barato (menor g), debemos actualizarlo
                if child_state not in reached or child_cost < reached[child_state].cost:
                    # 12. Crear nodo hijo
                    child_node = Node(
                        "",
                        state=child_state,
                        cost=child_cost,
                        parent=node,
                        action=action
                    )
                    child_node.estimated_distance = estimated_distance

                    # 13. Actualizar o agregar el nuevo mejor camino a esa celda
                    reached[child_state] = child_node
                    # 14. Agregar a la frontera con prioridad f = g + h
                    frontier.add(child_node, priority=child_cost + estimated_distance)

        # 15. Si se agotan los nodos sin encontrar la meta, no hay solución
        return NoSolution(reached)