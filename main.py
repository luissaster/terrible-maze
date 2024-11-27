import pygame
from maze import Maze
from agent import Agent
# Constants
CELL_SIZE = 64
ROWS, COLS = 12, 12
SCREEN_SIZE = (CELL_SIZE * COLS, CELL_SIZE * ROWS)

# Maze defined on the assignment
# 0 = wall, 1 = path
defined_maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def main():
    pygame.init()

    # Screen setup
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Terrible Maze")

    # Maze setup
    maze = Maze(defined_maze)

    # Agent setup
    agent_start = (4, 11)
    agent_goal = (10, 0)
    agent = Agent(agent_start[0], agent_start[1])
    
    # Calculate agent path
    agent_final_path, agent_path = agent.breadth_first_search(maze.maze, agent_start, agent_goal)
    
    # Path visualization
    path_index = 0

    # Game loop
    clock = pygame.time.Clock()
    running = True
    print(agent_final_path)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            """
            Agent input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    agent.move("up", maze.maze, ROWS, COLS)
                elif event.key == pygame.K_DOWN:
                    agent.move("down", maze.maze, ROWS, COLS)
                elif event.key == pygame.K_LEFT:
                    agent.move("left", maze.maze, ROWS, COLS)
                elif event.key == pygame.K_RIGHT:
                    agent.move("right", maze.maze, ROWS, COLS)
            """

        # Update the agent's position along the path
        if agent_final_path and path_index < len(agent_final_path):
            agent.y, agent.x = agent_final_path[path_index]
            path_index += 1

        # Clear the screen
        screen.fill(pygame.Color("black"))

        # Draw the maze
        maze.draw(screen, CELL_SIZE)

        # Draw the best path
        if agent_final_path:
            maze.draw_path(screen, agent_final_path[:path_index], "green", CELL_SIZE)

        # Draw the agent
        agent.draw(screen, CELL_SIZE)
        
        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(5)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
