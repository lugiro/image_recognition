# image_recognition
### Image recognition with Python  

With these modules you can recognize text written on a 10" tablet  
See picture of test rig: irTestRig01.jpg  

### Main file:    

**imgPiFindLinesAndLetters01.py**
- Capture image with Pi Camera
- Cropp image to area according to screen on tablet
- Save grey file: imageCam_grey.png
- Convert imageCam_grey.png to camtall.txt 30x40 text matrix on file
- Calculate lines
- Calculate characters on each line
- Put together characters to a sentence
- Sentence sent to espeak (text to speech). 
  
**Equipment:**
- Raspberry Pi
- Raspberri Pi Camera v2
- Tablett 10"
- Speaker

Installation of Pi Camera on Raspbery Pi:  
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4  
  
Installation Python modules  
sudo apt-get install python-picamera python3-picamera  
  
Installation espeak (Text To Speech)  
sudo apt-get install espeak  
  
Espeak command options:  
https://espeak.sourceforge.net/commands.html  
  
Example espeak:  
espeak -p99 -ven+m5 -g2 AS YOU CAN SEE AND HEAR I CAN NOW READ THIS TEXT 2>/dev/null  
  
Youtube (Text To Speech):  
https://youtu.be/LAvYszaxNuI  

**Use tablet to write text**  
Use web and send text to the tablet  
Install Apache on Raspberry Pi  
Capture image of the tablet screen with Pi Camera  

