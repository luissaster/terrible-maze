import pygame
from collections import deque

class Agent:
    def __init__(self, x, y):
        """
        Initializes the Agent with a starting position.

        Parameters:
            x (int): The initial column position of the agent.
            y (int): The initial row position of the agent.
        """

        self.x = x
        self.y = y

    def move(self, direction, maze, ROWS, COLS):
        """
        Moves the agent in the specified direction if the move is valid.

        Parameters:
            direction (str): The direction to move the agent. Must be one of "up", "down", "left", or "right".
            maze (list): A 2D list representing the maze. 0 represents a wall and 1 represents an open path.
            ROWS (int): The number of rows in the maze.
            COLS (int): The number of columns in the maze.
        """
        
        if direction == "up" and self.y > 0 and maze[self.y - 1][self.x] == 1:
            self.y -= 1
        elif direction == "down" and self.y < ROWS - 1 and maze[self.y + 1][self.x] == 1:
            self.y += 1
        elif direction == "left" and self.x > 0 and maze[self.y][self.x - 1] == 1:
            self.x -= 1
        elif direction == "right" and self.x < COLS - 1 and maze[self.y][self.x + 1] == 1:
            self.x += 1

    
    def draw(self, screen, CELL_SIZE):
        """
        Draws the agent on the given screen at its current position.

        Parameters:
            screen (pygame.Surface): The screen to draw on.
            CELL_SIZE (int): The size of each cell in the maze.
        """
        
        pygame.draw.rect(screen, pygame.color.Color("purple"), (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def get_neighbors(self, maze, pos):
        """
        Finds and returns all neighboring cells that are open paths (value 1) 
        from a given position in the maze.

        Parameters:
            maze (list of list of int): A 2D list representing the maze, 
                where 0 represents a wall and 1 represents an open path.
            pos (tuple): The current position in the maze as a tuple (row, column).

        Returns:
            list of tuple: A list of neighboring positions (row, column) that 
                are open paths, checked in the order: up, left, right, down.
        """
        row, col = pos
        neighbors = []

        # Check in the order specified in the assignment
        # ↑ up, ← left, → right, ↓ down
        if row > 0 and maze[row - 1][col] == 1:                 # Up
            neighbors.append((row - 1, col))
        if col > 0 and maze[row][col - 1] == 1:                 # Left
            neighbors.append((row, col - 1))
        if col < len(maze[0]) - 1 and maze[row][col + 1] == 1:  # Right
            neighbors.append((row, col + 1))
        if row < len(maze) - 1 and maze[row + 1][col] == 1:     # Down
            neighbors.append((row + 1, col))

        return neighbors

    def breadth_first_search(self, maze, start, goal):
        """
        Performs a breadth-first search to find the shortest path from the start to the goal.

        Parameters:
            maze (list): A 2D list representing the maze. 0 represents a wall and 1 represents an open path.
            start (tuple): The starting position of the search. A tuple of two integers (row, column).
            goal (tuple): The goal position of the search. A tuple of two integers (row, column).

        Returns:
            tuple: A tuple containing the shortest path as a list of tuples, the total number of steps taken, 
                and a list of all visited cells.
        """
        queue = deque([start])
        visited = set()  # To keep track of visited cells
        came_from = {}  # To reconstruct the shortest path
        all_visited = []  # List to store all visited cells for drawing

        visited.add(start)

        steps = 0

        while queue:
            current = queue.popleft()

            # Add the current cell to the list of visited cells
            all_visited.append(current)

            # Check if we reached the goal
            if current == goal:
                # Reconstruct the path to the goal
                path = []
                while current:
                    path.append(current)
                    current = came_from.get(current)
                return path[::-1], steps, all_visited  # Return the path, total steps, and all visited cells

            # Explore neighbors (in the order: ↑ up, ← left, → right, ↓ down)
            neighbors = self.get_neighbors(maze, current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current

            steps += 1

        return None, steps, all_visited
    
    def depth_first_search(self, maze, start, goal):
        """
        Performs a depth-first search to find the shortest path from the start to the goal.

        Parameters:
            maze (list): A 2D list representing the maze. 0 represents a wall and 1 represents an open path.
            start (tuple): The starting position of the search. A tuple of two integers (row, column).
            goal (tuple): The goal position of the search. A tuple of two integers (row, column).

        Returns:
            tuple: A tuple containing the shortest path as a list of tuples, the total number of steps taken,
                and a list of all visited cells.
        """

        stack = [start]
        visited = set()  # To keep track of visited cells
        came_from = {}  # To reconstruct the shortest path
        all_visited = []  # List to store all visited cells for drawing

        visited.add(start)

        steps = 0

        while stack:
            current = stack.pop()

            # Add the current cell to the list of visited cells
            all_visited.append(current)

            # Check if we reached the goal
            if current == goal:
                # Reconstruct the path to the goal
                path = []
                while current:
                    path.append(current)
                    current = came_from.get(current)
                return path[::-1], steps, all_visited  # Return the path, total steps, and all visited cells

            # Explore neighbors (in the order: ↑ up, ← left, → right, ↓ down)
            neighbors = self.get_neighbors(maze, current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current

            steps += 1

        return None, steps, all_visited

