import os
import time
import f_img_coa

#Make a template

letterNum = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
             "P","Q","R","S","T","U","V","W","X","Y","Z",
#             "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
#             "p","q","r","s","t","u","v","w","x","y","z",
             "1","2","3","4","5","6","7","8","9","0",
             "#","+",":"]

num_of_elements = len(letterNum)

directory = "template/"
prefix = "template"
font = "Verdana"

for z in range(num_of_elements) :

    file_name_template = directory + prefix + font + letterNum[z] + ".txt"
    print file_name_template

    output_file = "/usr/lib/cgi-bin/pi/text0.txt"
    with open(output_file, "w") as txt_file:
        txt_file.write((letterNum[z]) + "\n")

    time.sleep(2)

    ## Capture and save image and make a text array (camtall.txt)
    os.system("python imgPiCaptureSaveGrayAndArray01.py")

    cmd = "cp camtall.txt " + file_name_template
    os.system(cmd)


