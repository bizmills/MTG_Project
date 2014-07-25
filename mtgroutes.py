from flask import Flask, request, session, render_template, g, redirect, url_for, flash
from model import db_session, Card, Collection, Collection_item, User, Set
import jinja2
import tempfile
import base64
from PIL import Image
import imagehash



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
#stores image in a temporary file and parses
def pass_img():
    saveimg = request.form.get('imgBase64')
    new_temp = tempfile.NamedTemporaryFile(delete=False)
    img = saveimg.split(',')
    clean_img = img[-1]
    print clean_img
    # this returns a decoded string, need to be able to turn it into img
    decode_img = base64.b64decode(clean_img)
    new_temp.file.write(decode_img)
    print new_temp.name
    # scanned image is now called new_temp
    
    # Process the scanned image
    img = Image.open(new_temp)
    imageG = img.convert('L')
    small = imageG.resize((9, 8), Image.ANTIALIAS) 
    hashimg = imagehash.dhash(small) # hash img
    h = str(hashimg) # change to number
    num_of_bits = 8
    hashbin = bin(int(h, 16))[2:].zfill(num_of_bits) # convert to bytestring and fill in 0s
    print hashbin
    new_temp.close()
    return render_template("scan.html")

@app.route("/update", methods=["GET"])
def display_update():
    """manually update collection"""
    return render_template("update.html")

@app.route("/update", methods=["POST"])
def update_collection():
    """can add to collection with card title, spell type, set, rarity""" 
    #TODO add ability to add collection name
    #collection_name = request.form['c_name']
    card_name = request.form['name']
    #Fields not necessary for DB update
    # setName = request.form['Set']
    # rarity = request.form['Rarity']
    # spell_type = request.form['Spell Type']

    # checking to see if card is real card from Card class and getting the card
    # ToDO handle error if card not found
    card_from_table = db_session.query(Card).filter_by(name=card_name).all()
    # if card_from_table:
    #     flash("you've successfully added a card to your collection")
    #adding row to collection items table
    col_itm_card = Collection_item(cards_id = card_from_table.id)
    db_session.add(col_itm_card)
    db_session.commit()
    db_session.refresh(col_itm_card)

    return render_template("update_results.html")

@app.route("/search", methods=["GET"])
def display_search():
    return render_template("search.html")
                          
@app.route("/search", methods=["POST"])
def search_collection():
    # query = request.form['name']
    # in_collection = db_session.query(Collection_item).filter(Collection_item.like("%" + query + "%")).all()
    # print request.form
    """can search on card title, spell type, set, rarity""" 

    return render_template("search.html")
    

if __name__ == "__main__":
    app.run(debug=True)
