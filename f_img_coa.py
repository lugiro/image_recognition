def calculate_objekt_array(image_input,image_output):

    from PIL import Image, ImageOps

    #Open image file from Paintbrush or from cam
    image0 = Image.open(image_input,"r")
    #Convert colour image to grayscale
    image1 = ImageOps.grayscale(image0)

    #Array varables
    xmin  = 1000
    xmax  = -1
    ymin  = 1000
    ymax  = -1
    anum  = 0
    pixels=0

    #Max number of pixels
    max_range = 15000

    #Width and height for image
    width, height = image1.size

    #Define array size
    #Arrays are used to define object size in x and y direction
    #Content in arrays set to 0
    arrayXimage =[]
    arrayXimage = [0 for i in range(max_range)]
    arrayYimage =[]
    arrayYimage = [0 for i in range(max_range)]

    #Find grayclour for each pixel (0-255), 0=black
    for y in range(height) :
        for x in range(width) :
            coordinate = x, y
            pix_colour = (image1.getpixel(coordinate));

            #If gray clour less than 80 set pixel colour to black
            #In array black colour is 1
            if pix_colour < 125:
                #Count number of black pixels
                pixels = pixels + 1
                #Calculate size of object i x,y direction
                arrayXimage[anum] = x
                arrayYimage[anum] = y 
                anum = anum + 1
                #Calculate  xmin,ymin og xmax og ymax for the object
                if x < xmin:
                    xmin = x
                if x > xmax:
                    xmax = x
                if y < ymin:
                    ymin = y
                if y > ymax:
                    ymax = y

    #recalculate xmin,ymin og xmax og ymax to
    #new array values starting in arraypoint 0,0
    #xamin,yamin og xamax og yamax
    xamin = 0
    xamax = xmax - xmin + 1 
    yamin = 0
    yamax = ymax - ymin + 1

    #Move x,y values to start point 0,0
    for anum in range(pixels) :
        arrayXimage[anum] = arrayXimage[anum] - xmin
        arrayYimage[anum] = arrayYimage[anum] - ymin

    #Define object array according to object size yamax, xamax
    rows, cols = (yamax, xamax)
    objektArray = [[0 for i in range(cols)] for j in range(rows)]

    #Store black pixels in objectArray
    anum = 0 
    for y in range(yamax) :
        for x in range(xamax) :
            if arrayYimage[anum] == y and arrayXimage[anum] == x:
                objektArray[y][x] = 1
                anum = anum + 1


    #Write data (for test and error handling)
    #for y in range(yamax) :
    #    print objektArray[y]

#    print pixels
    #print xmin, xmax
    #print ymin, ymax
#    print xamin, xamax
#    print yamin, yamax

    #Copy from objectArray to new image (overwrite)
    #Change image size for objectArray
    image1 = image1.resize((xamax,yamax))
    #Store pixel value (black) in new image
    for y in range(yamax):
        for x in range(xamax) :
            if objektArray[y][x] == 1:
                image1.putpixel( (x, y), 0 )
            else:
                image1.putpixel( (x, y), 255 )

    #Resize image to x,y 30x40
    image1 = image1.resize((30,40))

    #Define a new objektarray 
    rows, cols = (40, 30)
    objekt2Array = [[0 for i in range(cols)] for j in range(rows)]

    #Find gray clour for each pixel (0-255) 0=black
    for y in range(rows) :
        for x in range(cols) :
            coordinate = x, y
            pix_colour = (image1.getpixel(coordinate));

            #If gray colour is less than 80 define pixel as black
            #In array black clour is set to 1
            if pix_colour < 125:
                objekt2Array[y][x] = 1

    #Convert array to text string and store each line in text file separated with space
    with open(image_output, "w") as txt_file:
        for y in range(rows):
            output = " ".join(str(i) for i in objekt2Array[y])
            txt_file.write((output) + "\n")

