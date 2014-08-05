from flask import Flask, request, session, render_template, g, redirect, url_for, flash
from model import db_session, Card, Collection, Collection_item, User, Set
import jinja2
import tempfile
import base64
from PIL import Image, ImageChops
import imagehash
import sqlalchemy 
from sqlalchemy import orm

def grayscale():
    # Process the scanned image
    img = Image.open("test_scan/test_inferno_fist.png")
    img.show() #shows start image
    imageG = img.convert('L')
    imageG.show() #shows grayscale image
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
    imageG.show() # shows cropped image
    small = imageG.resize((9, 8), Image.ANTIALIAS) 
    small.show() # shows resized image
    hashimg = imagehash.dhash(small) # hash img
    h = str(hashimg) # change to number
    num_of_bits = 64
    hashbin = bin(int(h, 16))[2:].zfill(num_of_bits) # convert to bytestring and fill in 0s
    print "this is hashbin", hashbin
    return hashbin

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

def main():
    gs_img = grayscale()
    trimmed = trim_img(gs_img)
    hashbin = resize(trimmed)
    clean = clean_str()
    match = ham_dist(hashbin, clean)
    print match

if __name__ == "__main__":
    main()