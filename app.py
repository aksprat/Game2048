from flask import Flask, render_template_string, request, jsonify
from game import Game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    game.move(direction)
    return jsonify(game.board)

if __name__ == '__main__':
    game = Game()
    app.run(debug=True, host='0.0.0.0')
