from flask import Flask, request, jsonify, render_template
from services.game import Game, Tile
from services.utils import render_board_state, get_empty_tiles, is_game_over
from services.colors import generate_color_mapping

import random
import copy

app = Flask(__name__)

game = Game()
prev_game_state = copy.deepcopy(game)  # Initialize the previous game state

@app.route('/', methods=['GET', 'POST'])
def main():
    global game, prev_game_state
    color_mapping = generate_color_mapping(game.size)
    
    if request.method == 'POST':
        data = request.json
        
        if data['key'] == 'undo':
            game = copy.deepcopy(prev_game_state)
            game_over = is_game_over(game)
            return jsonify(
                grid_data=render_board_state(game),
                color_mapping=color_mapping,
                game_over=game_over,
                score=game.score
            )
        
        if data['key'] in ['ArrowUp', 'ArrowLeft', 'ArrowDown', 'ArrowRight']:
            prev_game_state = copy.deepcopy(game)
            if data['key'] == 'ArrowUp':
                game.moveUp()
            elif data['key'] == 'ArrowLeft':
                game.moveLeft()
            elif data['key'] == 'ArrowDown':
                game.moveDown()
            elif data['key'] == 'ArrowRight':
                game.moveRight()

            if len(get_empty_tiles(game.tiles)) != 0 and game.tiles != prev_game_state.tiles:
                random.choice(get_empty_tiles(game.tiles)).value = 2 if random.random() < game.p_two else 4

            game_over = is_game_over(game)
        
        elif data['key'] == 'restart':
            game = Game()
            prev_game_state = copy.deepcopy(game)
            game_over = is_game_over(game)
        
        return jsonify(
            grid_data=render_board_state(game),
            color_mapping=color_mapping,
            game_over=game_over,
            score=game.score
        )
    
    game_over = is_game_over(game)
    return render_template('grid.html', grid_data=render_board_state(game), color_mapping=color_mapping, game_over=game_over, score=game.score)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
