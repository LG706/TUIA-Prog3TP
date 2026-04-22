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
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        frontier = PriorityQueueFrontier()
        frontier.add(root, priority=0)

        while not frontier.is_empty():
            # Extraemos el nodo con menor costo acumulado (g)
            node = frontier.pop()

            # 4. Test de objetivo al DESENCOLAR (crucial en UCS)
            if grid.objective_test(node.state):
                return Solution(node, reached)

            # 5. Expandir sucesores
            for action in grid.actions(node.state):
                child_state = grid.result(node.state, action)
                child_cost = node.cost + grid.individual_cost(node.state, action)

                # 6. Si no fue alcanzado O encontramos un camino más barato
                if child_state not in reached or child_cost < reached[child_state].cost:
                    child_node = Node(
                        "", 
                        state=child_state, 
                        cost=child_cost, 
                        parent=node, 
                        action=action
                    )
                    
                    # Actualizamos o agregamos el nuevo mejor camino a esa celda
                    reached[child_state] = child_node
                    frontier.add(child_node, priority=child_cost)
                    

        return NoSolution(reached)
