__author__ = "Erik Anderson"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Anderson"
__email__ = "primex001@gmail.com"
__status__ = "Development"

from flask import Flask, send_file, render_template
from flask import request
import json
import sqlite3

service = {'some': 'Data'}

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('nso_rec.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def welcome(name='test'):
    # Nothing Like Home!
    return render_template('index.html', name=name)

@app.route("/reconciliation")
def reconciliation():
    return render_template('reconciliation.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/edit")
def edit():
    return render_template('edit.html', service=service)

@app.route("/evaluate")
def evaluate():
    return render_template('evaluate.html')

@app.route("/report")
def report():
    return render_template('report.html')

@app.route("/help")
def help():
    return render_template('help.html')

# Post GET
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# @app.route('/hello/')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# @app.route("/config_gen/", methods=["GET", "POST"])
# def config_gen():
#     if request.method == "POST":
#         data = request.form
#         zipped = config_gen2.passinput(data)
#         return send_file(zipped, as_attachment=True)
#     else:
#         return render_template("config_gen.html")

# @app.route('/database')
# def database():
#     conn = get_db_connection()
#     posts = conn.execute('SELECT * FROM posts').fetchall()
#     conn.close()
#     return render_template('index.html', posts=posts)

# Edit example:
# @app.route('/<int:id>/edit', methods=('GET', 'POST'))
# def edit(id):
#     post = get_post(id)

#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']

#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('UPDATE posts SET title = ?, content = ?'
#                          ' WHERE id = ?',
#                          (title, content, id))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))

#     return render_template('edit.html', post=post)

# Flask Send E-mail
# from flask_mail import Message

# @app.route("/")
# def index():

#     msg = Message("Hello",
#                   sender="from@example.com",
#                   recipients=["to@example.com"])
# mail.send(msg)
