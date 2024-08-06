from flask import Flask, request, jsonify, render_template
from services.game import Game, Tile
from services.utils import render_board_state, get_empty_tiles
from services.colors import generate_color_mapping

import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    global game
    color_mapping = generate_color_mapping(game.size)
    
    if request.method == 'POST':  
        data = request.json
        
        if (data['key'] == 'ArrowUp'):
            game.moveUp()
        elif (data['key'] == 'ArrowLeft'):
            game.moveLeft()
        elif (data['key'] == 'ArrowDown'):
            game.moveDown()
        elif (data['key'] == 'ArrowRight'):
            game.moveRight()
        
        if len(get_empty_tiles(game.tiles)) != 0:
            random.choice(get_empty_tiles(game.tiles)).value = 2 if random.random() < game.p_four else 4
        else:
            print('hi')
            
        return jsonify(grid_data=render_board_state(game), color_mapping=color_mapping)
    
    return render_template('grid.html', grid_data=render_board_state(game), color_mapping=color_mapping)

if __name__ == '__main__':
    game = Game()
    app.run(debug=True, host='0.0.0.0')
    