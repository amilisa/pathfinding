def is_index_valid(row, column, min_index, max_index):
    if row < min_index or row > max_index:
        return False
    if column < min_index or column > max_index:
        return False
    return True


def transform_to_index(y, x, cell_size):
    i = int(y // cell_size)
    j = int(x // cell_size)
    return i, j


def init_path_points(grid, start_row, start_column, end_row, end_column):
    start_point = grid[start_row][start_column]
    end_point = grid[end_row][end_column]
    grid[start_row][start_column].is_path_point = True
    grid[end_row][end_column].is_path_point = True
    return start_point, end_point
