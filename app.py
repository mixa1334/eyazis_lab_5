from flask_cors import cross_origin
from flask import Flask, render_template, request
import logic

app = Flask(__name__)

@app.route('/')
@app.route('/info')
@cross_origin()
def info():
    return render_template('info.html')


@app.route('/speech', methods=['POST', 'GET'])
@cross_origin()
def speech():
    if request.method == 'POST':
        text = request.form['text']
        voice = request.form['voice']
        rate = request.form['rate']
        volume = request.form['volume']
        logic.text_to_speech(text, voice, rate, volume)
        return render_template('speech.html')
    else:
        return render_template('speech.html')