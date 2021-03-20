from flask import Flask, url_for
from waitress import serve

app = Flask(__name__)


@app.route('/')
def home():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет от Фишль и Оза</title>
                        <title></title>
                      </head>
                      <body>
                        <h1>Fischl: I, Fischl, Prinzessin der Verurteilung, descend upon this land by the call of fate an— Oh, you are also a traveler from another world? Very well, I grant you permission to travel with me.</h1>
                        
                        <h1>Oz: She means "Nice to meet you."</h1>
                        <img src="{url_for('static', filename='image/fishl.png')}"
                   alt="здесь должна была быть картинка, но не нашлась">
                   
                      </body>
                    </html>"""


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
    # app.run(port=8080, host='127.0.0.1')
