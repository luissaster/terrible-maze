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

# Just a little tool to help creating mazes

# You can make a maze of any size by just changing the values of ROWS and COLS (default is 12x12)
# Cell Size is more of a personal preference, you can change it to whatever you want, I use 64 because my screen is quite big and it looks better

import pygame
import os
import datetime

# Maze dimensions
ROWS, COLS = 12, 12

CELL_SIZE = 64
WINDOW_WIDTH, WINDOW_HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
GRID_COLOR = (200, 200, 200)
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Editor")
font = pygame.font.Font(None, 36)

defined_maze = []

# Maze initialization
for i in range(ROWS):
    row = [0] * COLS
    defined_maze.append(row)

def draw_maze(maze):
    """
    Draws the given maze on the screen, with each cell being represented as either a path (white) or a wall (black).

    Parameters:
        maze (list of list): A 2D list representing the maze, where 0 represents a wall and 1 represents an open path.
    """
    for row in range(ROWS):
        for col in range(COLS):
            color = WALL_COLOR if maze[row][col] == 0 else PATH_COLOR
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def save_maze(maze):
    """
    Saves the given maze to a file in the "extras/mazes" folder.
    
    The file name is a timestamp in the format "%Y-%m-%d_%H-%M-%S" followed by ".txt".
    
    Prints the full path of the saved file to the console.
    """
    folder_name = "extras/mazes"
    os.makedirs(folder_name, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"maze_{timestamp}.txt"
    filepath = os.path.join(folder_name, filename)
    with open(filepath, "w") as f:
        f.write("[\n")
        for row in maze:
            f.write("    " + str(row) + ",\n")
        f.write("]\n")
    print(f"Maze saved to {os.path.abspath(filepath)}")

def main():
    global defined_maze
    running = True

    while running:
        screen.fill((255, 255, 255))
        draw_maze(defined_maze)

        text = font.render("Press S to save, Q to quit", True, pygame.Color("red"))
        screen.blit(text, (10, WINDOW_HEIGHT - 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE

                # Toggle between wall (0) and path (1)
                defined_maze[row][col] = 1 if defined_maze[row][col] == 0 else 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    save_maze(defined_maze)
                elif event.key == pygame.K_q:
                    running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
