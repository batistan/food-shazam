from . import app
from .models import *
import datetime as dt
import json
from flask import render_template, redirect, request, flash, g, session, url_for, send_file

app.secret_key = "xsjnfeDSWID8erawv"


# home page
# see templates directory for what this whole templates thing is about
@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    return render_template("index.html", all_stations=all_stations)

@app.route('/search', methods=["GET"])
def search():
    return render_template("search.html")

@app.route('/search_results', methods=["POST"])
def search_results():
   location = request.form['location']
   #filename = request.form['file']
   filename = './slack.jpeg'
   tags = getTags(filename)
   if tags==0:
     results=0

   else:
       # TODO: parse the return from getRestaurants
       results_json = getRestaurants(tags, location)

       parsed_json = json.loads(results_json)

       results = parsed_json['response']

   return render_template("search_results.html", results=results)

@app.route("/css/<css>")
def style_render(css):
    return render_template("css/%s"%css)

@app.route("/images/<image>")
def image_render(image):
    filename = ('templates/images/%s'%image)
    return send_file(filename,mimetype='image/jpeg')

