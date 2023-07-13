from os import path
from pathlib import Path

from flask import Flask, render_template, send_from_directory
from flask_frozen import Freezer


template_folder = path.abspath('./wiki/site')
static_folder = path.abspath('./wiki/site')

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


@app.route('/404.html')
def site_error():
    return render_template('404.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/sitemap.xml.gz')
def sitemap():
    return render_template('404.html')


@app.route('/sitemap.xml')
def sitemapgz():
    return render_template('sitemap.xml')


# @app.route('/<page>/')
# def pages(page):
#     return render_template(str(Path(page)) + '/index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500


# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    app.run(port=8080)
