from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # 1. Inicializar nodo raíz (punto de inicio)
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # 2. Verificación rápida: ¿el inicio es la meta?
        if grid.objective_test(root.state):
            return Solution(root, {})

        # 3. Inicializamos la frontera (Cola para BFS) y los alcanzados
        frontier = QueueFrontier()
        frontier.add(root)

        # 4. Mantener registro de nodos ya visitados para evitar ciclos
        reached = {}
        reached[root.state] = root

        # 5. Bucle principal de exploración
        while not frontier.is_empty():
            node = frontier.remove()

            # 6. Para cada acción posible desde el estado actual
            for action in grid.actions(node.state):
                child_state = grid.result(node.state, action)
                
                # 7. Calcular costo acumulado (costo del padre + costo de la celda)
                child_cost = node.cost + grid.individual_cost(node.state, action)
                
                # 8. Crear nodo hijo con la información del camino
                child_node = Node(
                    "", 
                    action=action,
                    state=child_state,
                    cost=child_cost,
                    parent=node,
                )

                # 9. Solo explorar si no fue visitado antes (evita ciclos)
                if child_state not in reached:
                    # Guardamos el nodo en lugar de solo un booleano
                    reached[child_state] = child_node 

                    # 10. Verificar si llegamos a la meta
                    # IMPORTANTE: Usar el nombre de tu método en grid.py
                    if grid.objective_test(child_state):
                        return Solution(child_node, reached)

                    # 11. Agregar a la frontera para explorar sus vecinos
                    frontier.add(child_node)
                           
        # 12. Si se agotan los nodos sin encontrar la meta, no hay solución
        return NoSolution(reached)
