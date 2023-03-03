# image_recognition
### Image recognition with Python<br>
<br>
With these modules you can recognize text written on a 10" tablet.<br>Use web and send text to the tablet.<br>
Install Apache on Raspberry Pi<br>
Capture image of the tablet with Pi CAmera<br>
Image recognition with Python<br>
<br>
###Main file:<br>

**imgPiFindLinesAndLetters01.py**<br>
- Capture image with Pi Camera<br>
- Cropp image to area according to screen on tablet<br>
- Save grey file: imageCam_grey.png<br>
- Convert imageCam_grey.png to camtall.txt 30x40 text matrix on file<br>
- Calculate lines<br>
- Calculate characters on each line<br>
- Put together characters to a sentence<br>
- Sentence sent to espeak (text to speech)<br>

<br>
**Equipment:**<br>
- Raspberry Pi<br>
- Raspberri Pi Camera v2<br>
- Tablett 10"<br>
- Speaker<br>
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
