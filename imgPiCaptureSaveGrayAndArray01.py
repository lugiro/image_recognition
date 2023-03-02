import os
from PIL import Image, ImageOps
from picamera import PiCamera
import time
import f_img_coa

##
##

#os.system("sudo fswebcam imageCam.jpg 2> /dev/null")
camera = PiCamera()

camera.resolution = (600, 350)
#camera.rotation = 180
#camera.vflip = True
#camera.contrast = 10
#camera.image_effect = "watercolor"
#time.sleep(1)
camera.capture("imageCam.jpg")
print("Cam done.")

# creating a image object
img = Image.open(r"imageCam.jpg")
width, height = img.size
print width, height

cropped = img.crop((115,100,515,300))

# applying grayscale method
gray_image = ImageOps.grayscale(cropped)
gray_image.save('imageCam_grey.png')

width, height = cropped.size
print "cam cropped size x,y ", width, height

f_img_coa.calculate_objekt_array("imageCam_grey.png","camtall.txt")
