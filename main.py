from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('first.html', title='Колонизация Марса')


@app.route('/training/<prof>')
def training(prof):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <title>Колонизация Марса</title>
                  </head>
                  <body>
                     <h2>Здравствуй, {prof}!</h2>
                     <h3>Для тебя были приготовлены {'инженерные симуляторы'
    if 'строител' in prof or 'инже' in prof else 'научные симуляторы'}</h3>
                    <div class="alert alert-success">https://www.youtube.com/watch?v=dQw4w9WgXcQ</div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
