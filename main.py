import pygame
import sys
import window_tools
import drawing_tools
import misc
import path_finding_algorithm
import Maze_algorithm

from constants.colors import *
from constants.sizes import *
from Cell import Cell
from EntryWindow import EntryWindow

# Fps 
FPS = 60

# algorithims
algorithms = {
    "Breadth-first Search": path_finding_algorithm.breadth_first_search,
    "Depth-first Search": path_finding_algorithm.depth_first_search,
    "Dijkstra's Algorithm": path_finding_algorithm.dijkstra,
    "A-star Search": path_finding_algorithm.A_star
}

# def main function
def main():
    grid = [[Cell(i, j) for i in range(COLUMNS_NUMBER)] for j in range(ROWS_NUMBER)]
    pygame.init()
    clock = pygame.time.Clock()
    WINDOW = window_tools.create_main_window(WIDTH, HEIGHT, GREY, "Path Finding")
    drawing_tools.draw_instructions(WINDOW, SUB_ORIGIN, HEIGHT, WHITE)

    grid_wrapper = drawing_tools.create_grid_wrapper(WINDOW, SUB_ORIGIN, SUB_ORIGIN, GRID_SIZE, GRID_SIZE, WHITE)
    drawing_tools.draw_grid(grid_wrapper, grid, ROWS_NUMBER, COLUMNS_NUMBER, CELL_SIZE, SGILIGHTGRAY)

    pygame.display.update()

    start_point = None
    end_point = None
    selected_algorithm = None

    running = True
    while running:
        pygame.event.pump()
        
        clock.tick(FPS)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                sys.exit()

            # left click - 0
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                i, j = misc.transform_to_index(y - SUB_ORIGIN, x - SUB_ORIGIN, CELL_SIZE)
                if misc.is_index_valid(i, j, MIN_INDEX, MAX_INDEX):
                    cell = grid[i][j]
                    if pygame.key.get_pressed()[pygame.K_m]:
                        maze_start = cell
                        start_point = None
                        end_point = None   
                        Maze_algorithm.prims_maze(maze_start, grid, grid_wrapper)
                        grid[i][j].is_active = True 
                    elif not start_point and cell is not end_point:
                        start_point = cell
                        drawing_tools.draw_path_point(i, j, grid_wrapper, grid, CELL_SIZE, RED)
                    elif not end_point and cell is not start_point:
                        end_point = cell
                        drawing_tools.draw_path_point(i, j, grid_wrapper, grid, CELL_SIZE, DARK_GREEN)
                    elif cell is not start_point and cell is not end_point and pygame.key.get_pressed()[pygame.K_1]:
                        drawing_tools.draw_weight_1(i, j, grid_wrapper, grid, CELL_SIZE, Weight1)
                    elif cell is not start_point and cell is not end_point and pygame.key.get_pressed()[pygame.K_2]:
                        drawing_tools.draw_weight_2(i, j, grid_wrapper, grid, CELL_SIZE, Weight2)
                    elif cell is not start_point and cell is not end_point and pygame.key.get_pressed()[pygame.K_3]:
                        drawing_tools.draw_weight_3(i, j, grid_wrapper, grid, CELL_SIZE, Weight3)
                    elif cell is not start_point and cell is not end_point:
                        drawing_tools.draw_obstacle(i, j, grid_wrapper, grid, CELL_SIZE, IVORYBLACK)

            # right click - 2
            elif pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                i, j = misc.transform_to_index(y - SUB_ORIGIN, x - SUB_ORIGIN, CELL_SIZE)
                if misc.is_index_valid(i, j, MIN_INDEX, MAX_INDEX):
                    cell = grid[i][j]
                    cell.draw_cell(grid_wrapper, CELL_SIZE, WHITE)

                    if cell is start_point:
                        start_point.is_path_point = False
                        start_point = None
                    elif cell is end_point:
                        end_point.is_path_point = False
                        end_point = None
                    elif cell is not start_point and cell is not end_point:
                        cell.is_active = True

            drawing_tools.draw_grid(grid_wrapper, grid, ROWS_NUMBER, COLUMNS_NUMBER, CELL_SIZE, SGILIGHTGRAY)

        if pygame.key.get_pressed()[pygame.K_f] and selected_algorithm:
            running = False
        elif pygame.key.get_pressed()[pygame.K_c]:
            entry_window = EntryWindow()
            entry_window.mainloop()
            selected_algorithm = entry_window.selected_algorithm

    algorithm = algorithms[selected_algorithm]
    path = algorithm(start_point, end_point, grid, grid_wrapper)
    if path:
        drawing_tools.draw_path(path, grid_wrapper, end_point, CELL_SIZE, LIGHT_GREEN, grid)
        path_length = len(path)
        message = f"The shortest path has been found!\nThe path length is {path_length} cost."
    else:
        message = "There is no path between the points."
    answer = window_tools.show_message(message)

    if answer:
        main()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()


if __name__ == "__main__":
    main()
