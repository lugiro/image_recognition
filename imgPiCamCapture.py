from PIL import Image, ImageOps
from picamera import PiCamera

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
print width, height

cropped = img.crop((115,100,515,300))

# applying grayscale method
gray_image = ImageOps.grayscale(cropped)
gray_image.save('imageCam_grey.png')

print("Cam done.")
