from . import app
from .models import *
import datetime as dt
import json
import os
from flask import Flask, render_template, redirect, request, flash, g, session, url_for, send_file
from werkzeug.utils import secure_filename

#app = Flask(__name__)
#app.config['template_folder'] = '../bootstrap-4.0.0-alpha.6-dist/node_modules/bootstrap/node_modules/startbootstrap-creative/'
app.secret_key = "xsjnfeDSWID8erawv"
#upload_folder = '/tmp/idcrave'
allowed_extensions = set(['png', 'jpg', 'jpeg', 'gif'])
#app.config['UPLOAD_FOLDER'] = upload_folder

# home page
# see templates directory for what this whole templates thing is about
@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/search_results', methods=["POST"])
def search_results():
   #location = request.form['location']
   #filename = request.form['file']
   #filename = './slack.jpeg'

   print(str(request.files))
   ifile = request.files['image']
   tags = getTags(ifile)
   if tags==0:
     results=0

   else:
       # TODO: parse the return from getRestaurants
       results_json = getRestaurants(tags, 'New York, NY')

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

