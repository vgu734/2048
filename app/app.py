from flask import Flask, request, jsonify, render_template
from services.game import Game, Tile
from services.utils import render_board_state, get_empty_tiles, is_game_over
from services.colors import generate_color_mapping

import random
import copy

app = Flask(__name__)

game = Game()

@app.route('/', methods=['GET', 'POST'])
def main():
    global game
    color_mapping = generate_color_mapping(game.size)
    
    game_over = is_game_over(game)
    original_tiles = copy.deepcopy(game.tiles)
    
    if request.method == 'POST':  
        data = request.json
        if data['key'] == 'ArrowUp':
            game.moveUp()
        elif data['key'] == 'ArrowLeft':
            game.moveLeft()
        elif data['key'] == 'ArrowDown':
            game.moveDown()
        elif data['key'] == 'ArrowRight':
            game.moveRight()
        elif data['key'] == 'restart':
            game = Game()
            game_over = is_game_over(game)
        
        if len(get_empty_tiles(game.tiles)) != 0 and game.tiles != original_tiles:
            random.choice(get_empty_tiles(game.tiles)).value = 2 if random.random() < game.p_two else 4
            
        return jsonify(grid_data=render_board_state(game), color_mapping=color_mapping, game_over=game_over)
    
    return render_template('grid.html', grid_data=render_board_state(game), color_mapping=color_mapping, game_over=game_over)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
