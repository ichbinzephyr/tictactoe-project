from flask import Flask, render_template, request, jsonify
from tictactoe import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    square = data['square']
    letter = data['letter']
    if game.make_move(square, letter):
        return jsonify({'status': 'success', 'winner': game.current_winner})
    return jsonify({'status': 'failure'})

if __name__ == '__main__':
    app.run(debug=True)
