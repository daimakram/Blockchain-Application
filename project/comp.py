from flask import Flask, request
from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
import requests
from lib import verify


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_chain():
    if request.method == 'POST':
        # data = [{"name" : "car", "company" : "audi", "date" : "5/2/22"}, {"name" : "car tires", "company" : "honda", "date" : "10/2/22"}]
        data = verify()
        print("here")
        details = request.form
        pid = details.get('pid') # course_id
        print(pid)
        print("leaving")
        print(data)
        return render_template("display.html", data = data)

    return render_template("random.html")

app.run(debug=True, port=5000)
