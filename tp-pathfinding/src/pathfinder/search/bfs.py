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
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # 2. Verificación rápida: ¿el inicio es la meta?
        if grid.objective_test(root.state):
            return Solution(root, {})

        # 3. Inicializamos la frontera (Cola para BFS) y los alcanzados
        frontier = QueueFrontier()
        frontier.add(root)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root

        # Initialize frontier with the root node
        # TODO Complete the rest!!

        while not frontier.is_empty():
            node = frontier.remove()

            for action in grid.actions(node.state):
                child_state = grid.result(node.state, action)
                
                # Usamos el costo real de la celda
                child_cost = node.cost + grid.individual_cost(node.state, action)
                
                child_node = Node(
                    "", 
                    action=action,
                    state=child_state,
                    cost=child_cost,
                    parent=node,
                )

                if child_state not in reached:
                    # Guardamos el nodo en lugar de solo un booleano
                    reached[child_state] = child_node 

                    # IMPORTANTE: Usar el nombre de tu método en grid.py
                    if grid.objective_test(child_state):
                        return Solution(child_node, reached)

                    frontier.add(child_node)
                           
        return NoSolution(reached)
