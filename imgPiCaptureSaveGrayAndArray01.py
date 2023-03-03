import os
from PIL import Image, ImageOps
from picamera import PiCamera
import time
import f_img_coa

camera = PiCamera()

camera.resolution = (600, 350)
#camera.rotation = 180
#camera.vflip = True
#camera.contrast = 10
#camera.image_effect = "watercolor"
#time.sleep(1)
camera.capture("imageCam.jpg")

# creating a image object
img = Image.open(r"imageCam.jpg")
width, height = img.size

## IMPORTANT Cropped area must containe white background
## White color is greater than 125 on grey colour scale
cropped = img.crop((120,100,510,300))

# applying greyscale method
gray_image = ImageOps.grayscale(cropped)
gray_image.save('imageCam_grey.png')

width, height = cropped.size

print "Cropped gray image done"

## Convert image file (.png) to text array file (camtall.txt)
f_img_coa.calculate_objekt_array("imageCam_grey.png","camtall.txt")

print "Camtall done"
