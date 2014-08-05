# MTGSQRL: Scan it, Update it, Search it
###### Got thousands of magic cards?
###### Tired of data entry?

MTGSQRL is a web application that captures your card's image through a web cam, and then determines which card it is by comparing it to a reference set of images and data. When processing, the app automatically identifies the area of interest in a captured image, finds edges, crops appropriately, and then calculates the Hamming distance between your card and the app's existing known set of images. 

### Technologies used:
1. Presentation layer: HTML, CSS, javaScript, AJAX, Bootstrap, Jinja
2. Application layer: Flask, Python
..* including Python Image Library (PIL)
3. Data layer: SQLite3, SQLAlchemy
 
 ### Description of Components:
 1. **model.py**
 ..* file creates the database tables
 2. To get the meta data for the card go to http://mtgjson.com/ and select a set 
 3. To build your library of references go to http://mtgimage.com/set/M15/ 
 ..* use wget to rapidly download all images in the set. I used only the full jpg (not cropped, not "high quality (hq)")
 4. **jsonparse.py**
 ..* This will seed the database with your card images and create the hashes. You will need to have your JSON object and library of reference images before seeding your database
 ..* change line 12 to reference the correct JSON object for the set you are loading
 ..* change my_images_path to reference thfile path where you've stored your reference images
 5. **mtgroutes.py**
 ..* this is the flask application file

 ### How to capture images successfully:
 **camera**
 Use an external web cam. I'm using a logitech c615

 **lighting**
 Bright natural light is best. Glare on the card will result in no matches.

 **Card placement**
Card should be placed flat on a white surface. Try to keep it aligned. 
