from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    grid_data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    return render_template('grid.html', grid_data=grid_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')