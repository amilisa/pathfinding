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
