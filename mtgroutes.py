from flask import Flask, request, session, render_template, g, redirect, url_for, flash
from model import db_session, Card, Collection, Collection_item, User, Set
import jinja2
import tempfile
import base64
from PIL import Image, ImageChops
import imagehash
import sqlalchemy 
from sqlalchemy import orm
# from img_process import pass_img, grayscale, trim_img, resize, clean_str, ham_dist



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
#stores image in a temporary file  
def controller():
    imgfile = pass_img()
    gs_img = grayscale(imgfile)
    trimmed = trim_img(gs_img)
    hashbin = resize(trimmed)
    clean = clean_str()
    match = ham_dist(hashbin, clean)
    print match
    return render_template("find.html", match=match)

def pass_img():
    saveimg = request.form.get('imgBase64')
    new_temp = tempfile.NamedTemporaryFile(delete=False)
    img = saveimg.split(',')
    clean_img = img[-1]
    # this returns a decoded string
    decode_img = base64.b64decode(clean_img)
    new_temp.file.write(decode_img)
    print new_temp.name
    imgfile = new_temp.name
    new_temp.close()
    return imgfile

def grayscale(imgfile):
    # Process the scanned image
    img = Image.open(imgfile)
    imageG = img.convert('L')
    # imageG.show() #shows grayscale image
    return imageG

def trim_img(imageG):
    # Crop Image
    image_diff = Image.new(imageG.mode, imageG.size, imageG.getpixel((0,0)))
    diff = ImageChops.difference(imageG, image_diff)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return imageG.crop(bbox)

def resize(imageG):
    # Resize for comparison
    # imageG.show() # shows cropped image
    small = imageG.resize((9, 8), Image.ANTIALIAS) 
    # small.show() # shows resized image
    hashimg = imagehash.dhash(small) # hash img
    h = str(hashimg) # change to number
    num_of_bits = 64
    hashbin = bin(int(h, 16))[2:].zfill(num_of_bits) # convert to bytestring and fill in 0s
    print "this is hashbin", hashbin
    return hashbin
# this is from my ham_dist_stub
def clean_str():
    db_imgs = []    
    stored_imgs = db_session.query(Card.hashId).select_from(Card).all()
    for image in stored_imgs:
        new_string = str(image[0])
        db_imgs.append(new_string)
    return db_imgs

def ham_dist(hashbin, db_imgs):
    poss_cards = [] # TO DO append the possible cards
    for image in db_imgs:
        diffs = 0
        for ch1, ch2 in zip(image, hashbin):
            if ch1 != ch2:
                diffs += 1
        if diffs <= 10: 
            poss_cards.append(image)
    print poss_cards
    # remove the "None"s from the list
    matches = filter(lambda a: a != 'None', poss_cards)
    # get the card name associated with each hash   
    match_name = []
    n = 0
    for match in matches:
        your_card = db_session.query(Card).filter_by(hashId = str(matches[n])).all()[0].name
        match_name.append(your_card)
        n += 1
    print len(match_name)
    print match_name
    return match_name

@app.route("/find", methods=["GET"])
def display_match():
    return render_template("find.html")

@app.route("/update/<name>", methods=["GET"])
def display_update(name):
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
            flash("Update countered! Try again")
            return render_template("update.html")

@app.route("/search", methods=["GET"])
def display_search():
    return render_template("search.html")
                          
@app.route("/search", methods=["POST"])
def search_collection():
    query = request.form['query']
    in_collection = db_session.query(Collection_item).filter(Card.name.ilike("%" + query + "%")).limit(10)
    print in_collection
    """can search on card title, spell type, set, rarity""" 
    #will go to search
    return render_template("search_results.html", search_collection=in_collection)
    

if __name__ == "__main__":
    app.run(debug=True)
