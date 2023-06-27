from os import path
from pathlib import Path

from flask import Flask, render_template, send_from_directory
from flask_frozen import Freezer


template_folder = path.abspath('./documentation/site')
static_folder = path.abspath('./documentation/site')

app = Flask(__name__,
            static_url_path='',
            static_folder=static_folder,
            template_folder=template_folder,
            )


app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)


@app.cli.command()
def freeze():
    freezer.freeze()


@app.cli.command()
def serve():
    freezer.run()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<page>/')
def serve_page(page):
    return render_template(str(Path(page)) + '/index.html')


# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    app.run(port=8080)
