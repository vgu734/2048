def render_board_state(game):
    '''
    Render the board state to be html readable.
    '''
    board_state = []
    
    for i in range(game.size):
        row = []
        for j in range(game.size):
            row.append(game.tiles[i*game.size + j].value)
        board_state.append(row)
        
    return board_state

def get_empty_tiles(tiles):
    '''
    Return list of empty, value 0, tiles from a list of tiles.
    '''
    return [tile for tile in tiles if tile.value == 0]

def is_game_over(game):
    '''
    Return if the game is over or not.
    '''
    grid = [[0 for _ in range(game.size)] for _ in range(game.size)]
    for tile in game.tiles:
        x, y = tile.index
        grid[x][y] = tile.value

    def can_merge(x1, y1, x2, y2):
        return grid[x1][y1] == grid[x2][y2] and grid[x1][y1] != 0

    for row in grid:
        if 0 in row:
            return False

    for x in range(game.size):
        for y in range(game.size - 1):
            if can_merge(x, y, x, y + 1):
                return False

    for y in range(game.size):
        for x in range(game.size - 1):
            if can_merge(x, y, x + 1, y):
                return False

    return True
