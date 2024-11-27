import pygame

class Maze:
    def __init__(self, maze):
        self.maze = maze

    def draw(self, screen, CELL_SIZE):
        """
        Draws the maze on the given screen with the specified cell size.

        Parameters:
            screen (pygame.Surface): The screen to draw on.
            CELL_SIZE (int): The size of each cell in the maze.
        """
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == 0:
                    pygame.draw.rect(screen, pygame.color.Color("black"), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif self.maze[row][col] == 1:
                    pygame.draw.rect(screen, pygame.color.Color("white"), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    def draw_path(self, screen, path, color, CELL_SIZE):
        """
        Draws a path on the given screen.

        Parameters:
            screen (pygame.Surface): The screen to draw on.
            path (list of tuple): A list of (row, column) tuples representing the path to draw.
            color (str): The color to use for drawing the path.
            CELL_SIZE (int): The size of each cell in the maze.
        """
        for cell in path:
            pygame.draw.rect(screen, pygame.color.Color(color), (cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

