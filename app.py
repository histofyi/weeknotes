from flask import Flask
import json

from handlers.views import weeknotes_index_handler, weeknotes_post_handler, weeknotes_tags_handler, weeknotes_tag_handler, weeknotes_year_handler, weeknotes_month_handler
from handlers.cli import build_index_handler


def create_app():
    """
    Creates an instance of the Flask app, and associated configuration and blueprints registration for specific routes. 

    Configuration includes

    - Relevant secrets stored in the config.toml file
    - Storing in configuration a set of credentials for AWS (decided upon by the environment of the application e.g. development, live)
    
    Returns:
            A configured instance of the Flask app

    """
    app = Flask(__name__)

    # removing whitespace from templated returns    
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.data = {}

    return app


app = create_app()


@app.before_first_request
def load_data():
    """
    This is a function which loads the generated datasets which are used by the site.

    By loading them in here, we can reduce S3 calls and speed the app up significantly.
    """
    with open('content/index.json') as index_file:
        index = json.load(index_file)

    for key in index:
        app.data[key] = index[key]
    pass



@app.route('/weeknotes/')
@app.route('/weeknotes')
def index_view():
    return weeknotes_index_handler()


@app.route('/weeknotes/tags/')
@app.route('/weeknotes/tags')
def tags_view():
    return weeknotes_tags_handler()


@app.route('/weeknotes/tags/<string:tag_slug>/')
@app.route('/weeknotes/tags/<string:tag_slug>')
def tag_view(tag_slug):
    return weeknotes_tag_handler(tag_slug)


@app.route('/weeknotes/years/<string:year>/')
@app.route('/weeknotes/years/<string:year>')
def year_view(year):
    return weeknotes_year_handler(year)


@app.route('/weeknotes/years/<string:year>/months/<string:month>/')
@app.route('/weeknotes/years/<string:year>/months/<string:month>/')
def month_view(year, month):
    return weeknotes_month_handler(year, month)


@app.route('/weeknotes/posts/<string:post_slug>/')
@app.route('/weeknotes/posts/<string:post_slug>')
def post_view(post_slug):
    return weeknotes_post_handler(post_slug)


@app.route('/tmp/build_index')
def build_index_view():
    return build_index_handler()    


@app.cli.command('build_index')
def build_index_command():
    print ('BUILDING INDEX')
    return build_index_handler()    