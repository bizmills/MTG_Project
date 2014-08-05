# MTGSQRL: Scan it, Update it, Search it
###### Got thousands of magic cards?
###### Tired of data entry?
###### Just want to know what you have in your collection? 



MTGSQRL is a web application that captures your card's image through a web cam, and then determines which card it is by comparing it to a reference set of images and data. When processing, the app automatically identifies the area of interest in a captured image, finds edges, crops appropriately, and then calculates the Hamming distance between your card and the app's existing known set of images. 

### Technologies used:
1. Presentation layer: HTML, CSS, javaScript, AJAX, Bootstrap, Jinja
2. Application layer: Flask, Python (including Python Image Library (PIL))
3. Data layer: SQLite3, SQLAlchemy
 
### Description of Components:
1. **model.py**
This creates the database tables
2. To get the meta data for the card go to http://mtgjson.com/ and select a set 
3. To build your library of references go to http://mtgimage.com/set/M15/ 
use wget to rapidly download all images in the set. I used only the full jpg (not cropped, not "high quality (hq)")
4. **jsonparse.py**
This will seed the database with your card images and create the hashes. You will need to have your JSON object and library of reference images before seeding your database
Change line 12 to reference the correct JSON object for the set you are loading
Change my_images_path to reference thfile path where you've stored your reference images
5. **mtgroutes.py**
This is the flask application file

### How to capture images successfully:
**camera:**
Use an external web cam. I'm using a logitech c615

**lighting:**
Bright natural light is best. Glare on the card will result in no matches.

**Card placement:**
Card should be placed flat on a white surface. Try to keep it aligned. 

## Screen Shots

Home screen

![alt text](https://github.com/bizmills/MTG_Project/blob/master/app_screenshots/home.png "This is the main screen")

Scan It

![alt text](https://github.com/bizmills/MTG_Project/blob/master/app_screenshots/scan.png "note placement of cards")

Update It

![alt text](https://github.com/bizmills/MTG_Project/blob/master/app_screenshots/update.png "update collection manualy")

Search It

![alt text](https://github.com/bizmills/MTG_Project/blob/master/app_screenshots/search.png "search your collection")


## Future Features
**Create trade lists:**
 Allow users to generate lists of cards that are available for trade.

**Optimize image matching algorithm to scale:**
 current run-time with 186 cards is fairly quick, but handling 30K cards will increase processing time

**Optimize image processing:**
Enable image morphing to control tilting card. Mitigate dependency on quality lighting

**Improve collection reporting:** 
add quantity, display by attribute (spell type, rarity, etc)

**Improve searching collection:** 
allow search by attributes other than name

**Improve updating collection:** 
allow deletion of cards from collection