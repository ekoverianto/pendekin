from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    url = request.form['url']
    result = pyshorteners.Shortener().tinyurl.short(url)
    return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)