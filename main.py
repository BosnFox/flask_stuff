from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('first.html', title='Колонизация Марса')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
