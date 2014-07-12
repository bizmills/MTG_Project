from flask import Flask, request, session, render_template, g, redirect, url_for, flash
# import model import db_session
import jinja2


app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    """Home Page: with path to scan or search""" 
    return render_template("index.html")

@app.route("/scan")
def scan_card():
    """Image is scanned and matched"""
    #Lots of code goes here
    return render_template("scan.html")

@app.route("/update", methods=["GET"])
def display_update():
    """manually update collection"""
    return render_template("update.html")

@app.route("/update", methods=["POST"])
def update_collection():
    """can search on card title, spell type, set, rarity""" 

    return render_template("update_results.html")

@app.route("/search", methods=["GET"])
def display_search():
    return render_template("search.html")
                          
@app.route("/search", methods=["POST"])
def search_collection():
    # query = request.form['name']
    # cards = db_session.query(Collection)
    """can search on card title, spell type, set, rarity""" 

    return render_template("search_results.html")
    

if __name__ == "__main__":
    app.run(debug=True)
