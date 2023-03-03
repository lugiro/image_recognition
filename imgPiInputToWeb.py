#Input to web - start.pl -  tablet - IP-adr/cgi-bin/pi/start.no

while True:
    letter = raw_input("Enter letter: ")

    output_file = "/usr/lib/cgi-bin/pi/text0.txt"
    with open(output_file, "w") as txt_file:
        txt_file.write((letter) + "\n")


