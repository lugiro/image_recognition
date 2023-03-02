import os
import f_img_coa

#Tar bild med cam
os.system("python imgPiCaptureSaveGrayAndArray01.py")
#os.system("python image_main03.py")    #Omformer cambilde til array 30x40

#Omformer cambilde til array 30x40
#img_coa.calculate_objekt_array("imageCam_grey.png","camtall.txt")

array_name = [[ ['0' for x in range(30)] for y in range(40)] for l in range(70)]

letterNum = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
             "P","Q","R","S","T","U","V","W","X","Y","Z",
#             "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
#             "p","q","r","s","t","u","v","w","x","y","z",
             "1","2","3","4","5","6","7","8","9","0",
             "#","+",":"]

#letterNum = ["A","B","C","D","E","F","G","H","I","J"]
num_of_elements = len(letterNum)
print num_of_elements
directory = "template/"
prefix = "template"
font = "Verdana"

for z in range(num_of_elements) :
    file_name_template = directory + prefix + font + letterNum[z] + ".txt"
    # Read array original file lines
    file_array = open(file_name_template, 'r')
    Lines = file_array.readlines()

#array_name = [[ ['0' for col in range(10)] for col in range(30)] for row in range(40)]
#print array_name

#for z in range(10) :
    # Convert text file lines to list
    array_orig = []
    for line in Lines:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        array_orig.append(line_list)
    array_name[z] = array_orig

#print array_name[1]
#print array_name[1][0]

# Read array cam file lines
file_array = open('camtall.txt', 'r')
Lines = file_array.readlines()

# Convert text file lines to list
array_cam = []
for line in Lines:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    array_cam.append(line_list)

#print array_cam

forrige_eqgodhet = 0

for z in range(num_of_elements) :
# Convert text file lines to list
#Sammenligen array for image og cam
    antfellespix = 0
    totteller = 0
    for y in range(40) :
        for x in range(30) :
#        print x, y, arrXim[anr], arrYim[anr]
#        print array_cam[y][x]
            if array_name[z][y][x] == "1":
                #print array_name[z][y][x]
                if array_name[z][y][x] == array_cam[y][x]:
                    antfellespix = antfellespix + 1
                    #print antfellespix 
                totteller = totteller + 1

            if array_name[z][y][x] == "0":
                #print array_name[z][y][x]
                if array_name[z][y][x] == array_cam[y][x]:
                    antfellespix = antfellespix + 1
                    #print antfellespix 
                totteller = totteller + 1

    eqgodhet = int((float(antfellespix) / totteller)*100)
    print antfellespix
    #print totteller
    print eqgodhet, letterNum[z]
    if eqgodhet > forrige_eqgodhet:
        forrige_eqgodhet = eqgodhet
        tegn = letterNum[z]

print "Bokstav er:", tegn
