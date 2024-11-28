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
from maze import Maze
from maze_layouts import *
from agent import Agent
from menu import show_menu, save_report

# Constants
CELL_SIZE = 64
ROWS, COLS = 12, 12
SCREEN_SIZE = (CELL_SIZE * COLS, CELL_SIZE * ROWS)

# Maze definition
defined_maze = assignment_maze

def main():
    pygame.init()

    algorithm, highlight, speed = show_menu(SCREEN_SIZE)
    if algorithm is None:
        return

    # Screen setup
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Terrible Maze")

    # Maze setup
    maze = Maze(defined_maze)

    # Agent setup
    start = (6, 11)
    goal = (10, 0)
    agent = Agent(start[0], start[1])

    # Configure speed
    speed_mapping = {"Slow": 2, "Normal": 5, "Fast": 10}
    clock = pygame.time.Clock()
    frame_rate = speed_mapping[speed]

    # Calculate agent path based on the selected algorithm
    if algorithm == "Breadth-First Search":
        final_path, steps, path = agent.breadth_first_search(maze.maze, start, goal)
    elif algorithm == "Depth-First Search":
        final_path, steps, path = agent.depth_first_search(maze.maze, start, goal)
    elif algorithm == "A* Search":
        final_path, steps, path = agent.a_star_search(maze.maze, start, goal)

    # Game loop
    running = True
    path_index = 0
    reached_goal = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the agent and highlight the path based on the selected option
        if not reached_goal:
            if highlight == "Best Path" and final_path and path_index < len(final_path):
                agent.y, agent.x = final_path[path_index]
                path_index += 1
            elif highlight == "Full Path" and path and path_index < len(path):
                agent.y, agent.x = path[path_index]
                path_index += 1
            elif highlight == "None" and final_path and path_index < len(final_path):
                agent.y, agent.x = final_path[path_index]
                path_index += 1

            # Check if the agent has reached the goal
            if (agent.y, agent.x) == goal:
                reached_goal = True
                print(f"Goal reached! Total steps: {steps}")
                save_report(algorithm, start, goal, steps, final_path, path, maze.maze)

        # Clear the screen
        screen.fill(pygame.Color("black"))

        # Draw the maze
        maze.draw(screen, CELL_SIZE)

        # Draw the path highlight based on the selected option
        if highlight == "Best Path":
            maze.draw_path(screen, final_path[:path_index], "cyan", CELL_SIZE)
        elif highlight == "Full Path":
            maze.draw_path(screen, path[:path_index], "blue", CELL_SIZE)

        # Draw the start and goal positions
        maze.draw_start_goal(screen, start, goal, CELL_SIZE)

        # Draw the agent
        agent.draw(screen, CELL_SIZE)

        # Goal reached message
        if reached_goal:
            font = pygame.font.Font(None, 64)
            text = font.render("Goal reached!", 1, pygame.Color("red"))
            textpos = (10, SCREEN_SIZE[1] - 50)
            screen.blit(text, textpos)

        pygame.display.flip()
        clock.tick(frame_rate)

    pygame.quit()


if __name__ == "__main__":
    main()
