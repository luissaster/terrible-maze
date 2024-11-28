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

def draw_menu(screen, options, selected_index):
    """
    Draws the menu screen with the given options and highlights the selected option.

    Parameters:
        screen (pygame.Surface): The screen to draw the menu on.
        options (list of str): A list of option strings to display on the menu.
        selected_index (int): The index of the currently selected option to be highlighted.
    """
    screen.fill((30, 30, 30))
    title_font = pygame.font.Font(None, 74)
    option_font = pygame.font.Font(None, 48)
    help_font = pygame.font.Font(None, 32)

    # Title
    title = title_font.render("Terrible Maze", True, (255, 255, 255))
    screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 50))

    # Options
    for i, option in enumerate(options):
        color = (255, 255, 255) if i != selected_index else (0, 255, 0)
        option_text = option_font.render(option, True, color)
        screen.blit(option_text, (screen.get_width() // 2 - option_text.get_width() // 2, 150 + i * 50))

    # Help text
    help = help_font.render("Use the arrow keys to navigate, press Enter to select", True, (255, 255, 255))
    screen.blit(help, (screen.get_width() // 2 - help.get_width() // 2, screen.get_height() - 50))

    pygame.display.flip()

def show_menu(SCREEN_SIZE) -> tuple:
    """
    Shows the main menu and waits for user input. Returns the selected algorithm, highlight option, and agent speed as a tuple of three strings. If the user selects Exit, returns (None, None, None).

    Returns:
        tuple of three str: (algorithm, highlight, speed)
    """
    
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Terrible Maze")
    clock = pygame.time.Clock()

    options = [
        "Start Game",
        "Algorithm: Breadth-First Search",
        "Highlight: Best Path",
        "Agent Speed: Normal",
        "Exit"
    ]

    available_algorithms = ["Breadth-First Search", "Depth-First Search", "A* Search"]
    available_highlights = ["Best Path", "Full Path", "None"]
    available_speeds = ["Slow", "Normal", "Fast"]

    selected_index = 0
    current_algorithm_index = 0
    current_highlight_index = 0
    current_speed_index = 1

    running = True
    while running:
        draw_menu(screen, options, selected_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:         # Start Game
                        return (
                            available_algorithms[current_algorithm_index],
                            available_highlights[current_highlight_index],
                            available_speeds[current_speed_index]
                        )
                    elif selected_index == 1:       # Change algorithm
                        current_algorithm_index = (
                            current_algorithm_index + 1
                        ) % len(available_algorithms)
                        options[1] = (
                            f"Algorithm: {available_algorithms[current_algorithm_index]}"
                        )
                    elif selected_index == 2:       # Change highlight
                        current_highlight_index = (
                            current_highlight_index + 1
                        ) % len(available_highlights)
                        options[2] = (
                            f"Highlight: {available_highlights[current_highlight_index]}"
                        )
                    elif selected_index == 3:       # Change agent speed (a.k.a. game framerate)
                        current_speed_index = (
                            current_speed_index + 1
                        ) % len(available_speeds)
                        options[3] = (
                            f"Agent Speed: {available_speeds[current_speed_index]}"
                        )
                    elif selected_index == 4:       # Exit
                        running = False

        clock.tick(30)
        
    pygame.quit()

    return None, None, None