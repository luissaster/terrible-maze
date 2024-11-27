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
    start = (4, 11)
    goal = (10, 0)
    agent = Agent(start[0], start[1])
    
    # Calculate agent path
    final_path, steps, path = agent.breadth_first_search(maze.maze, start, goal)

    # Dump agent path into a file
    with open("agent_path.txt", "w") as f:
        for cell in path:
            f.write(f"{cell[0]},{cell[1]}\n")
    
    with open("agent_final_path.txt", "w") as f:
        for cell in final_path:
            f.write(f"{cell[0]},{cell[1]}\n")
    
    # Path visualization
    path_index = 0

    # Game loop
    clock = pygame.time.Clock()
    running = True

    print(f"Steps: {steps}")

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the agent's position along the path
        if final_path and path_index < len(final_path):
            agent.y, agent.x = final_path[path_index]
            path_index += 1

        # Clear the screen
        screen.fill(pygame.Color("black"))

        # Draw the maze
        maze.draw(screen, CELL_SIZE)

        # Draw the best path
        if final_path:
            maze.draw_path(screen, final_path[:path_index], "green", CELL_SIZE)

        # Draw the agent
        agent.draw(screen, CELL_SIZE)
        
        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()
