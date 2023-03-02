from PIL import Image, ImageOps
import f_img_coa
import f_img_cial
import os

os.system("python imgPiCaptureSaveGrayAndArray01.py")

###Identifisere total hoyde for hele teksten
imageC = Image.open(r"imageCam_grey.png")
widthC, heightC = imageC.size

arrayLine = [0 for i in range(heightC)]

for y in range(heightC) :
    for x in range(widthC) :
        coordinate = x, y
        pixfarge = (imageC.getpixel(coordinate));

        if pixfarge <  125:
           arrayLine[y] = 1

#print arrayLine


###Identifisere hoyde for hver linje, beregner antall linjer
###Lagrer hver linje i lineArray, med 0 eller 1, (hvit eller sort)
alnum = 0
lstartflag = 0
totnumline, linestartstop = (20, 2)
lineArray = [[0 for i in range(linestartstop)] for j in range(totnumline)]
for y in range(heightC) :
    if arrayLine[y] == 1 and lstartflag == 0:   #Beregner startpkt for linje
       lineArray[alnum][0] = y
       lstartflag = 1
       alnum = alnum + 1
    if arrayLine[y] == 0 and lstartflag == 1:   #Beregner stoppkt for linje
       lineArray[alnum-1][1] = y
       lstartflag = 0
    if y == heightC-1 and lstartflag == 1:       #Korreksjon ved enden av image
       lineArray[alnum-1][1] = y+1

numline = alnum
print numline

for lnum in range(numline) :
    line_file = "line" + str(lnum) + ".png"
    print line_file
    croppedline = imageC.crop((0,lineArray[lnum][0],widthC,lineArray[lnum][1]))
    croppedline.save(line_file)


sentence = ""
for lnum in range(numline) :
    line_file = "line" + str(lnum) + ".png"
    ####################################
    ###Beregne total bredde for linje
    #antH = 0

    #imageg = Image.open(r"imageCam_grey.png")
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

    #print arrayCol


    ###Identifisere bredde for hvert objekt/bokstav og antall objekt 
    ###Lagrer hvert object i objArray, med 0 eller 1, (hvit eller sort)
    aonr = 0
    ostartflag = 0
    snum = 0
    space=[]
    space = [0 for i in range(20)]
    totantobj, startstop = (20, 2)
    objArray = [[0 for i in range(startstop)] for j in range(totantobj)]
    for x in range(width) :
        if arrayCol[x] == 1 and ostartflag == 0:   #Beregner startpkt for tegn
            objArray[aonr][0] = x
            ostartflag = 1
            aonr = aonr + 1
            #print x
        if arrayCol[x] == 0 and ostartflag == 1:   #Beregner stoppkt for tegn
            objArray[aonr-1][1] = x
            ostartflag = 0
            #print x
        if x == width-1 and ostartflag == 1:       #Korreksjon ved enden av image
            objArray[aonr-1][1] = x+1

        if arrayCol[x] == 0 and  arrayCol[x-1] == 1:  #Beregner mellomrom mellom tegn
#           print "test",x 
            numzero = 0
            if x+10 > width:                        #Spesialbehandling ved image slutt
                space[snum] = aonr
                aonr = aonr + 1
                snum = snum + 1 
            else:
                for t in range(10) :
                    if arrayCol[x+t] == 0:
                        numzero = numzero + 1
                if numzero == 10:
                    space[snum] = aonr
                    aonr = aonr + 1
                    snum = snum + 1
#                    print "space", aonr, snum

    antobj = aonr
    print antobj

    #print snum
    #print space[0], space[1]
    #print width
    #print objArray

    linesentence = ""
    snum = 0
    for lnum in range(antobj) :
        if space[snum] == lnum:
            linesentence = linesentence + "_"
#            print "spacefile",space[snum],snum,aonr
            snum = snum +1
        else:
            letter_file = "letter" + str(lnum) + ".png"
#           print letter_file
            croppedobj1 = imageg.crop((objArray[lnum][0],0,objArray[lnum][1],height))
            croppedobj1.save(letter_file)

            letterArray = "letterCam" + str(lnum) +".txt"
            f_img_coa.calculate_objekt_array(letter_file,"camtall.txt")

            tegn = f_img_cial.imgCompareImageArraysLetter()
            #print tegn

            linesentence = linesentence + tegn
#        print linesentence

    sentence = sentence + linesentence

print sentence

#cmd = "espeak -p99 -vno+m5 -g2 -s140 " + sentence + " 2>/dev/null"
cmd = "espeak -p90 -ven+m5 -g2 -s140 " + sentence + " 2>/dev/null"
os.system(cmd)
