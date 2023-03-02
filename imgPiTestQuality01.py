import os
import time

#Input to web - start.pl - Samsung tablet - 192.168.1.75/cgi-bin/start.no

letterNum = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
             "P","Q","R","S","T","U","V","W","X","Y","Z",
#             "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
#             "p","q","r","s","t","u","v","w","x","y","z",
             "1","2","3","4","5","6","7","8","9","0",
             "#","+",":"]

num_of_elements = len(letterNum)

for z in range(num_of_elements) :

    output_file = "/usr/lib/cgi-bin/pi/text0.txt"
    with open(output_file, "w") as txt_file:
        txt_file.write((letterNum[z]) + "\n")

    #print letterNum[z]
    time.sleep(2)
    os.system("python imgPiCompareImageArraysLetter01.py")

    print "Input: ",letterNum[z]
