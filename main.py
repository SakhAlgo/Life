from flask import Flask, render_template
import game_of_life as gl

app = Flask(__name__)

@app.route('/')
def index():
    gl.GameOfLife(20,20)
    return render_template('index.html')

@app.route('/live')
def live():
    game = gl.GameOfLife(20,20)
    game.form_new_generation()
    # print(game.world)
    return render_template('live.html', game=game)



if __name__ == '__main__':
    app.run(debug=True)