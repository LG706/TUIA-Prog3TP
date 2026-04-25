from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, grid.heuristic(root.state))

        while len(frontier.frontier) > 0:
            node = frontier.pop()

            # Llegó al objetivo
            if grid.objective_test(node.state):
                return Solution(node, reached)

            # Expandir vecinos
            for action in grid.actions(node.state):
                new_state = grid.result(node.state, action)
                new_cost = node.cost + 1

                if new_state not in reached or new_cost < reached[new_state]:
                    child = Node(
                        "",
                        state=new_state,
                        cost=new_cost,
                        parent=node,
                        action=action
                    )

                    reached[new_state] = new_cost

                    # PRIORIDAD = heurística
                    frontier.add(child, grid.heuristic(new_state))

        return NoSolution(reached)
