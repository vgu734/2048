def render_board_state(game):
    board_state = []
    
    for i in range(game.size):
        row = []
        for j in range(game.size):
            row.append(game.tiles[i*5 + j].value)
        board_state.append(row)
        
    return board_state

def get_empty_tiles(tiles):
    return [tile for tile in tiles if tile.value == 0]