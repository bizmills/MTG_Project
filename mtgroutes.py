from flask import Flask, request, session, render_template, g, redirect, url_for, flash
from model import db_session
import jinja2
import tempfile



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
    #scan image
    #morph scanned image to fix image angles
    #grascale the image
    #scale image down to 8X8
    #dhash image
    #x or operation to determine match points
    #bit population count to determine how different two images are
    return render_template("scan.html")

@app.route("/tempimg", methods=["POST"])
def pass_img():
    print "inside pass_img"
    saveimg = request.form.get('imgBase64')
    print "save image"
    new_temp = tempfile.NamedTemporaryFile(delete=False)
    print new_temp.name
    return render_template("scan.html")

@app.route("/update", methods=["GET"])
def display_update():
    """manually update collection"""
    return render_template("update.html")

@app.route("/update", methods=["POST"])
def update_collection():
    """can add to collection with card title, spell type, set, rarity""" 
    #collection_name = request.form['c_name']
    card_name = request.form['name']
    setName = request.form['Set']
    rarity = request.form['Rarity']
    spell_type = request.form['Spell Type']
    existing = db_session.query(Card).filter_by(name=name).first()
    if existing:
        flash("you've successfully added a card to your collection")
    c = Collection_item(cards_id = cards.id)
    db_session.add(c)
    db_session.commit()
    db_session.refresh(c)

    return render_template("update_results.html")

@app.route("/search", methods=["GET"])
def display_search():
    return render_template("search.html")
                          
@app.route("/search", methods=["POST"])
def search_collection():
    # query = request.form['name']
    # cards = db_session.query(Collection)
    print request.form
    """can search on card title, spell type, set, rarity""" 

    return render_template("search.html")
    

if __name__ == "__main__":
    app.run(debug=True)
