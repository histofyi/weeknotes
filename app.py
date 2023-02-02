from flask import Flask, request
import json
import toml
import datetime

from handlers.views import weeknotes_index_handler, weeknotes_post_handler, weeknotes_tags_handler, weeknotes_tag_handler, weeknotes_year_handler, weeknotes_month_handler
from handlers.cli import build_index_handler

from functions.decorators import templated


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

    app.config.from_file('config.toml', toml.load)

    # removing whitespace from templated returns    
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.data = {}

    return app


app = create_app()





def load_from_index(index):
    for key in index:
        app.data[key] = index[key]
    pass


@app.before_first_request
def load_data():
    """
    This is a function which loads the generated datasets which are used by the site.

    By loading them in here, we can reduce S3 calls and speed the app up significantly.
    """
    with open('content/index.json') as index_file:
        index = json.load(index_file)

    load_from_index(index)
    pass


# Web handlers

@app.route('/weeknotes/')
@app.route('/weeknotes')
@templated('index')
def index_view():
    return weeknotes_index_handler()


@app.route('/weeknotes/tags/')
@app.route('/weeknotes/tags')
def tags_view():
    return weeknotes_tags_handler()


@app.route('/weeknotes/tags/<string:tag_slug>/')
@app.route('/weeknotes/tags/<string:tag_slug>')
@templated('facet')
def tag_view(tag_slug):
    return weeknotes_tag_handler(tag_slug)


@app.route('/weeknotes/years/<string:year>/')
@app.route('/weeknotes/years/<string:year>')
@templated('facet')
def year_view(year):
    return weeknotes_year_handler(year)


@app.route('/weeknotes/years/<string:year>/months/<string:month>/')
@app.route('/weeknotes/years/<string:year>/months/<string:month>/')
@templated('facet')
def month_view(year, month):
    return weeknotes_month_handler(year, month)


@app.route('/weeknotes/posts/<string:post_slug>/')
@app.route('/weeknotes/posts/<string:post_slug>')
@templated('post')
def post_view(post_slug):
    return weeknotes_post_handler(post_slug)


@app.route('/tmp/build_index')
def build_index_view():
    if '127.0.0.1' in request.host:
        print ('BUILDING INDEX VIA URL')
        index = build_index_handler()
        load_from_index(index)
        return index
    else:
        return {'error':'Indexing by URL is only supported locally'}


#CLI handlers

@app.cli.command('build_index')
def build_index_command():
    print ('BUILDING INDEX VIA CLI')
    return build_index_handler()    


# Template filters

@app.template_filter()
def deslugify(text):
    """
    This function takes a slug of a text string and turns it back into a text string (assuming only spaces were in the original string)
    """
    return text.replace('_',' ')


@app.template_filter()
def humanize_fulldate(date):
    ordinal_char = '$'
    datestring = date.strftime(f'%B %d{ordinal_char} %Y')
    day_of_month = str(date.strftime('%d'))
    if day_of_month in ['1','11','21','31']:
        ordinal = 'st'
    elif day_of_month in ['2','22']:
        ordinal = 'nd'
    elif day_of_month in ['3','23']:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    datestring = datestring.replace(ordinal_char, ordinal)
    return datestring


@app.template_filter()
def truncate_list_posts(html):
    paragraphs = html.split('</p>')
    truncated_html = '</p>'.join(paragraphs[:1])
    truncated_html += '</p>'
    return truncated_html
