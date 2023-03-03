from PIL import Image, ImageOps
import f_img_coa
import f_img_cial
import os

## Capture image and save in text array
os.system("python imgPiCaptureSaveGrayAndArray01.py")

## Calculate total height of the image
imageC = Image.open(r"imageCam_grey.png")
widthC, heightC = imageC.size

arrayLine = [0 for i in range(heightC)]

for y in range(heightC) :
    for x in range(widthC) :
        coordinate = x, y
        pixfarge = (imageC.getpixel(coordinate));

        if pixfarge <  125:
           arrayLine[y] = 1


## Calculate height foor each line and numbers of lines
## Save line in lineArray 0 or 1 (white or black)
alnum = 0
lstartflag = 0
totnumline, linestartstop = (20, 2)
lineArray = [[0 for i in range(linestartstop)] for j in range(totnumline)]
for y in range(heightC) :
    if arrayLine[y] == 1 and lstartflag == 0:    #Calculate upper start point of the line
       lineArray[alnum][0] = y
       lstartflag = 1
       alnum = alnum + 1
    if arrayLine[y] == 0 and lstartflag == 1:    #Calculate lower stop point of the line
       lineArray[alnum-1][1] = y
       lstartflag = 0
    if y == heightC-1 and lstartflag == 1:       #Correction at the lower end of the image
       lineArray[alnum-1][1] = y+1

numline = alnum
print "Number of lines",numline

## Save cropped lines
for lnum in range(numline) :
    line_file = "line" + str(lnum) + ".png"
    print line_file
    croppedline = imageC.crop((0,lineArray[lnum][0],widthC,lineArray[lnum][1]))
    croppedline.save(line_file)


## For each line calculate number of objects/characters 
sentence = ""
for lnum in range(numline) :
    line_file = "line" + str(lnum) + ".png"
    imageg = Image.open(line_file)
    width, height = imageg.size

    arrayCol=[]
    arrayCol = [0 for i in range(width)]

    for x in range(width) :
        for y in range(height) :
            coordinate = x, y
            pixfarge = (imageg.getpixel(coordinate));

            if pixfarge <  125:
               arrayCol[x] = 1

    ## Calculate width for each objects/characters and number of objects in each line
    ## Save objects in objArray, 0 or 1 (white or black)
    aonr = 0
    ostartflag = 0
    snum = 0
    space=[]
    space = [0 for i in range(20)]
    totantobj, startstop = (20, 2)
    objArray = [[0 for i in range(startstop)] for j in range(totantobj)]
    for x in range(width) :
        if arrayCol[x] == 1 and ostartflag == 0:      #Calculate left start point for character
            objArray[aonr][0] = x
            ostartflag = 1
            aonr = aonr + 1
        if arrayCol[x] == 0 and ostartflag == 1:      #Calculate right stop point for charactern
            objArray[aonr-1][1] = x
            ostartflag = 0
        if x == width-1 and ostartflag == 1:          #Correction at right end of line image
            objArray[aonr-1][1] = x+1

        if arrayCol[x] == 0 and  arrayCol[x-1] == 1:
            numzero = 0
            if x+10 > width:                          #Calcultae space bethween characters
                space[snum] = aonr
                aonr = aonr + 1
                snum = snum + 1
            else:                                     #Special handling at right end of line image

                for t in range(10) :
                    if arrayCol[x+t] == 0:
                        numzero = numzero + 1
                if numzero == 10:
                    space[snum] = aonr
                    aonr = aonr + 1
                    snum = snum + 1

    antobj = aonr

    # For each characters compare with template and make sentence
    linesentence = ""
    snum = 0
    for lnum in range(antobj) :
        if space[snum] == lnum:
            linesentence = linesentence + "_"
            snum = snum +1
        else:
            letter_file = "letter" + str(lnum) + ".png"
            croppedobj1 = imageg.crop((objArray[lnum][0],0,objArray[lnum][1],height))
            croppedobj1.save(letter_file)

            letterArray = "letterCam" + str(lnum) +".txt"

            f_img_coa.calculate_objekt_array(letter_file,"camtall.txt")

            tegn = f_img_cial.imgCompareImageArraysLetter()

            linesentence = linesentence + tegn

    sentence = sentence + linesentence

    print "Line - calculate and compare char", antobj

print sentence

## Espeak - convert text to speech
cmd = "espeak -p99 -vno+m5 -g2 -s140 " + sentence + " 2>/dev/null"
#cmd = "espeak -p90 -ven+m5 -g2 -s140 " + sentence + " 2>/dev/null"
os.system(cmd)
