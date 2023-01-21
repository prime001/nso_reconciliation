from flask import Flask, send_file, render_template
from flask import request
import json

service = {'some': 'Data'}

app = Flask(__name__)

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