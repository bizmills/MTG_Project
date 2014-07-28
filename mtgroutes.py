from flask import Flask, request, session, render_template, g, redirect, url_for, flash
from model import db_session, Card, Collection, Collection_item, User, Set
import jinja2
import tempfile
import base64
from PIL import Image
import imagehash
import sqlalchemy 
from sqlalchemy import orm



app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    """Home Page: with path to scan or search""" 
    return render_template("index.html")

@app.route("/scan")
def scan_card():
    """Image is scanned"""
    return render_template("scan.html")


@app.route("/tempimg", methods=["POST"])
#stores image in a temporary file and parses
def pass_img():
    saveimg = request.form.get('imgBase64')
    new_temp = tempfile.NamedTemporaryFile(delete=False)
    img = saveimg.split(',')
    clean_img = img[-1]
    # this returns a decoded string, need to be able to turn it into img
    decode_img = base64.b64decode(clean_img)
    new_temp.file.write(decode_img)
    print new_temp.name
    imgfile = new_temp.name
    new_temp.close()
    # scanned image is now called clean_img
    
    # # Process the scanned image
    img = Image.open(imgfile)
    imageG = img.convert('L')
    small = imageG.resize((9, 8), Image.ANTIALIAS) 
    hashimg = imagehash.dhash(small) # hash img
    h = str(hashimg) # change to number
    num_of_bits = 8
    hashbin = bin(int(h, 16))[2:].zfill(num_of_bits) # convert to bytestring and fill in 0s
    print hashbin
    # clean_img.close()
    return render_template("scan.html")

@app.route("/find", methods=["GET"])


@app.route("/update", methods=["GET"])
def display_update():
    """manually update collection"""
    return render_template("update.html")

@app.route("/update", methods=["POST"])
def update_collection():
    """can add to collection with card title""" 
    while True:
        try: 
            card_name = request.form['name']

            # checking to see if card is real card from Card class and getting the card
            card_from_table = db_session.query(Card).filter_by(name=card_name).one()
            col_itm_card = Collection_item(cards_id = card_from_table.id)
            db_session.add(col_itm_card)
            db_session.commit()
            db_session.refresh(col_itm_card)
            flash("you've successfully added a card to your collection")
            return render_template("update.html")
        
        except sqlalchemy.orm.exc.NoResultFound:
            flash("Search countered! Try again.")
            return render_template("update.html")

@app.route("/search", methods=["GET"])
def display_search():
    return render_template("search.html")
                          
@app.route("/search", methods=["POST"])
def search_collection():
    query = request.form['query']
    in_collection = db_session.query(Collection_item).filter(Card.name.ilike("%" + query + "%")).all()
    # print request.form
    print in_collection
    # print db_session
    """can search on card title, spell type, set, rarity""" 
    #will go to search
    return render_template("search_results.html", collection=in_collection)
    

if __name__ == "__main__":
    app.run(debug=True)
