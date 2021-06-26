
from glob import glob
from os.path import isfile

def append(dyr, number, tekst, opcje, cechy):
    if None == number:
        raise Exception("No KEY!")
    if number in dyr:
        raise Exception("Duplicate key " + str(number))
    if None == tekst or 0 == len(tekst):
        raise Exception("No tekst for number " + str(number))
    if 0 == len(opcje):
        raise Exception("No options for number " + str(number))
    if "IM" not in cechy:
        print "WARN no image for number " + str(number)
    for (t,link) in opcje:
        if link == number:
            print "WARN short circut in node " + str(number)
    dyr[number] = (tekst, opcje, cechy)
    
def checkadv(dyr):
    keys = dyr.keys()
    for t,opts,att in dyr.itervalues():
        for o,i in opts:
            if i not in keys:
                raise Exception("option points to non-existing key " + str(i))
        

def read(fp, dyr):
    lines = fp.readlines()
    idx = 0
    
    number = None
    tekst = None
    opcje = None
    attribs = None
    
    for line in lines:
        idx += 1
        line = line.rstrip()
        
        if len(line.strip()):
            if line.isdigit():
                if None != number:
                    append(dyr, number, tekst, opcje, attribs)
                number = int(line)
                tekst = ""
                opcje = []
                attribs = {}
            elif line.startswith("    "):
                ciap = line.split()[0]
                if not ciap.isdigit():
                    raise Exception(str(idx) + ": option with no link!")
                option = line[line.index(ciap) + len(ciap) :]
                opcje.append((option, int(ciap)))
            elif line.startswith("ENDENDEND"):
                attribs["END"] = True
            elif line.startswith("WINWINWIN"):
                attribs["WIN"] = True
            elif line.startswith("IMIMIM"):
                impa = line[line.index("IMIMIM") + 6:].strip()
                if not isfile(impa):
                    raise Exception("No such file: " + impa)
                attribs["IM"] = impa
            else:
                tekst += line + "\n"
    
    if None != number:
        append(dyr, number, tekst, opcje, attribs)
                


def readadv():
    dyr = {}
    for fname in glob("ppp*.txt"):
        try:
            fp = open(fname)
            try:
                read(fp, dyr)
            finally:
                fp.close()
        except IOError, ioe:
            print "omg IOerror " +fname
    checkadv(dyr)
    return dyr
    
if __name__ == "__main__":
    print readadv()
