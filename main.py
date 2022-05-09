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


@app.route('/list_prof/<list>')
def listing(liste):
    try:
        assert liste in ['ul', 'ol']
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
                    <h2>Cписок работ</h2>
                    <ul>
                    <{liste}>Вилкой чистить</{liste}>
                    <{liste}>Рисовать четвёртый сезон Вакфу</{liste}>
                    <{liste}>Молиться Космосу ради еды</{liste}>
                    <{liste}>Записывать летсплеи по ENA</{liste}>
                    </ul>
                  </body>
                </html>"""
    except AssertionError:
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
                    <div class="alert alert-danger">Некорректный ввод типа списка</div>
                  </body>
                </html>"""

@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('auto_answer.html', title='Колонизация Марса', n_dict = {
        'name': 'Name',
        'surname': 'SûrName',
        'education': 'Nope',
        'profession': 'Nope',
        'sex': 'O T H E R',
        'ready': 'True'
    })

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
