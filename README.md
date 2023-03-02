# image_recognition
Image recognition with Python

With these moduels you can recognize text written on a 10" tablet

1. Use web and send tekst to the tablet
Install Apache on Raspberry Pi

2. Capture image of the tablet with Pi CAmera

3. Image recognition with Python
Cropp the image to fit the size of the screen area on the tablet
Convert image til gray scale

You need:
Raspberry Pi
Raspberri Pi Camera v2
Tablett 10"
Speaker

Installation of Pi Camera on Raspbery Pi:
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4

Installation Python modules
sudo apt-get install python-picamera python3-picamera

Insttalation espeak (Text To Speech)
sudo apt-get install espeak

Espeak command options:
https://espeak.sourceforge.net/commands.html

Example espeak:
espeak -p99 -ven+m5 -g2 AS YOU CAN SEE AND HEAR I CAN NOW READ THIS TEXT 2>/dev/null

Youtube (Text To Speech):
https://youtu.be/LAvYszaxNuI
