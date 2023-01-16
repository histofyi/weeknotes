from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_view():
    return 'index'

@app.route('/tags')
def tags_view():
    return 'tags'

@app.route('/tags/<string:tag_slug>')
def tag_view(tag_slug):
    return f'tag:{tag_slug}'

@app.route('/tags/<string:post_slug>')
def post_view(post_slug):
    return f'tag:{post_slug}'


@app.cli.command('build_index')
def build_index():
    print ('hello from CLI, building index')
