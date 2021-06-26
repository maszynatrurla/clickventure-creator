import Image
from glob import glob
import os.path

SIZE = (480, 480)

for fname in glob("picsOriginal/*"):
    try:
        im = Image.open(fname)
        im.thumbnail(SIZE, Image.ANTIALIAS)
        newname = os.path.join("pics", os.path.basename(fname))
        newname = os.path.splitext(newname)[0] + ".jpg"
        im.save(newname)
    except IOError, ioe:
        print "Skipping " + fname + " due to IOError (" + str(ioe) + ")"

