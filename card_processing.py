import os
import glob
import time
from PIL import Image as pil_image
from SimpleCV import Image as cv_image
print __doc__

#Settings
my_images_path = "JOU_imgs" #put your image path here if you want to override current directory
extension = "*.png"


#Program
if not my_images_path:
        path = os.getcwd() #get the current directory
else:
        path = my_images_path

imgs = list() #load up an image list
directory = os.path.join(path, extension)
files = glob.glob(directory)

print "FILES", files
for file in files:
    import pdb; pdb.set_trace()
    new_img = cv_image(file)
    gray = new_img.grayscale()
    pixel8 = gray.resize(8, 8)
    pixel8.show()
    time.sleep(3) #wait for 1 second