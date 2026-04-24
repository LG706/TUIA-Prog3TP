from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # 1. Inicializar nodo raíz (punto de inicio)
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # 2. Mantener registro de nodos ya visitados con su costo mínimo
        reached = {}
        reached[root.state] = root

        # 3. Inicializar frontera con el nodo raíz (cola de prioridad)
        # La prioridad es el costo acumulado (g)
        frontier = PriorityQueueFrontier()
        frontier.add(root, priority=0)

        # 4. Bucle principal de exploración
        while not frontier.is_empty():
            # 5. Extraer el nodo con menor costo acumulado (g)
            # UCS garantiza que siempre procesamos el camino más barato primero
            node = frontier.pop()

            # 6. Test de objetivo al DESENCOLAR (crucial en UCS)
            # En UCS verificamos al extraer porque podríamos haber encontrado
            # un camino más barato después de insertar el nodo
            if grid.objective_test(node.state):
                return Solution(node, reached)

            # 7. Expandir sucesores
            for action in grid.actions(node.state):
                child_state = grid.result(node.state, action)
                # 8. Calcular costo acumulado (costo del padre + costo de la celda)
                child_cost = node.cost + grid.individual_cost(node.state, action)

                # 9. Si no fue alcanzado O encontramos un camino más barato
                # Esto es crucial: si ya visitamos el nodo pero encontramos
                # un camino más barato, debemos actualizarlo
                if child_state not in reached or child_cost < reached[child_state].cost:
                    # 10. Crear nodo hijo
                    child_node = Node(
                        "", 
                        state=child_state, 
                        cost=child_cost, 
                        parent=node, 
                        action=action
                    )
                    
                    # 11. Actualizar o agregar el nuevo mejor camino a esa celda
                    reached[child_state] = child_node
                    frontier.add(child_node, priority=child_cost)
                    

        # 12. Si se agotan los nodos sin encontrar la meta, no hay solución
        return NoSolution(reached)
