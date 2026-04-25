from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        frontier = [root]

        while frontier:
            # Sacar el último (LIFO)
            node = frontier.pop()

            # Si ya lo visite, lo salteo
            if node.state in expanded:
                continue

            # Marco como visitado
            expanded[node.state] = True

            # Chequeo objetivo
            if grid.objective_test(node.state):
                return Solution(node, expanded)

            # Expando vecinos
            for action in grid.actions(node.state):
                new_state = grid.result(node.state, action)

                if new_state not in expanded:
                    child = Node(
                        "",
                        state=new_state,
                        cost=node.cost + 1,  # o el costo que corresponda
                        parent=node,
                        action=action
                    )
                    frontier.append(child)

        return NoSolution(expanded)
