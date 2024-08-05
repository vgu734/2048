from flask import Flask, request, jsonify, render_template
from services.game import Game, Tile
from services.utils import render_board_state, get_empty_tiles

import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    global game
    
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
            random.choice(get_empty_tiles(game.tiles)).value = 2 if random.random() < .8 else 4
        else:
            print('hi')
            
        return jsonify(grid_data=render_board_state(game))
    
    return render_template('grid.html', grid_data=render_board_state(game))

if __name__ == '__main__':
    game = Game()
    app.run(debug=True, host='0.0.0.0')