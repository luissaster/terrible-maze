# +---------------------------------------------+
# |     SIN 323 - Inteligência Artificial       |
# |     Universidade Federal de Viçosa -        |
# |     Campus Rio Paranaíba                    |
# |                                             |
# |     Luís Fernando Almeida - 8102            |
# |     luis.almeida1@ufv.br                    |
# |                                             |                               
# |                                             |
# |     Projeto 01 - Busca em Labirinto         | 
# +---------------------------------------------+

import pygame

class Maze:
    def __init__(self, maze):
        self.maze = maze

    def draw(self, screen, cell_size):
        """
        Draws the maze on the given screen with the specified cell size.

        Parameters:
            screen (pygame.Surface): The screen to draw on.
            cell_size (int): The size of each cell in the maze.
        """
        for row_index, row in enumerate(self.maze):
            for col_index, cell in enumerate(row):
                if cell == 0:
                    color = pygame.color.Color("black")
                elif cell == 1:
                    color = pygame.color.Color("white")

                pygame.draw.rect(screen, color, (col_index * cell_size, row_index * cell_size, cell_size, cell_size))

                pygame.draw.rect(screen, (200, 200, 200), (col_index * cell_size, row_index * cell_size, cell_size, cell_size), 1)
    
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

    def draw_start_goal(self, screen, start, goal, CELL_SIZE):
        """
        Draws the start and goal positions on the given screen.

        Parameters:
            screen (pygame.Surface): The screen to draw on.
            start (tuple): A tuple representing the start position as (row, column).
            goal (tuple): A tuple representing the goal position as (row, column).
            CELL_SIZE (int): The size of each cell in the maze.
        """
        pygame.draw.rect(screen, pygame.color.Color("red"), (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, pygame.color.Color("green"), (goal[1] * CELL_SIZE, goal[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

