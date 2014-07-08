import os
import glob
import time
from SimpleCV import *

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

for file in files:
        new_img = Image(file)
        new_img.show()
        time.sleep(2) #wait for 1 second
