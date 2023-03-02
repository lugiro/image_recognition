# image_recognition
Image recognition with Python<br>
<br>
With these moduels you can recognize text written on a 10" tablet<br>
<br>
1. Use web and send tekst to the tablet<br>
Install Apache on Raspberry Pi<br>
<br>
2. Capture image of the tablet with Pi CAmera<br>
<br>
3. Image recognition with Python<br>
Cropp the image to fit the size of the screen area on the tablet<br>
Convert image til gray scale<br>
<br>
You need:<br>
Raspberry Pi<br>
Raspberri Pi Camera v2<br>
Tablett 10"<br>
Speaker<br>
<br>
Installation of Pi Camera on Raspbery Pi:<br>
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4<br>
<br>
Installation Python modules<br>
sudo apt-get install python-picamera python3-picamera<br>
<br>
Insttalation espeak (Text To Speech)<br>
sudo apt-get install espeak<br>
<br>
Espeak command options:<br>
https://espeak.sourceforge.net/commands.html<br>
<br>
Example espeak:<br>
espeak -p99 -ven+m5 -g2 AS YOU CAN SEE AND HEAR I CAN NOW READ THIS TEXT 2>/dev/null<br>
<br>
Youtube (Text To Speech):<br>
https://youtu.be/LAvYszaxNuI<br>
