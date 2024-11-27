import os
import datetime
import pygame
from maze import Maze
from agent import Agent
from menu import show_menu

# Constants
CELL_SIZE = 64
ROWS, COLS = 12, 12
SCREEN_SIZE = (CELL_SIZE * COLS, CELL_SIZE * ROWS)

# Maze definition
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

def save_report(algorithm, start, goal, final_path, path):
    """
    Saves the maze solving details to a report file inside the 'txt' folder.

    Parameters:
        algorithm (str): The algorithm used to solve the maze.
        start (tuple): The start position (row, col).
        goal (tuple): The goal position (row, col).
        final_path (list): The final path taken by the agent.
        path (list): The complete path explored by the algorithm.
    """
    # Ensure the 'txt' folder exists
    folder_name = "txt"
    os.makedirs(folder_name, exist_ok=True)

    # Create a timestamped file name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder_name, f"maze_report_{timestamp}.txt")

    # Write report data to the file
    with open(filename, "w") as file:
        file.write(f"Algorithm Used: {algorithm}\n")
        file.write(f"Start Position: {start}\n")
        file.write(f"Goal Position: {goal}\n\n")
        file.write("Complete Path (Explored):\n")
        file.write(", ".join(map(str, path)) + "\n\n")
        file.write("Final Path (Optimal):\n")
        file.write(", ".join(map(str, final_path)) + "\n")
    
    print(f"Report saved to {filename}")


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
    start = (4, 11)
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
                save_report(algorithm, start, goal, final_path, path)

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

        pygame.display.flip()
        clock.tick(frame_rate)

    pygame.quit()


if __name__ == "__main__":
    main()
