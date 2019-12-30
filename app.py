from flask import flask, render_template, request
from flask_cors import CORS

app = flask(_name_)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method = 'GET':
        pass

    if request.method = 'POST':
        name = request.form.get('name')
        content = request.form.get('post')
        create_post(name, content)

        post = get_posts()

    return render_template('index.html', posts=posts)