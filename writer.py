import reader
from base64 import b64encode
import json
from random import randint

BEGIN = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <style>
"""

SCRIPT = """
    </style>
    <script type="text/javascript">

"""

MIDDLE = """

var _0x4131=['imlen','<p><img\x20alt=\x22Obrazek\x22\x20src=\x22data:image/jpg;base64,','\x22\x20/></p>','</div>','getElementById','here','innerHTML','prototype','charCodeAt','toString','slice','join','opts','body','style','backgroundColor','substring','tpos','tlen','<div\x20class=\x22szystko\x22>','impos'];(function(_0x3e439e,_0x35c51f){var _0xdf7129=function(_0x48bbf1){while(--_0x48bbf1){_0x3e439e['push'](_0x3e439e['shift']());}};_0xdf7129(++_0x35c51f);}(_0x4131,0x181));var _0x1d7e=function(_0x5ea303,_0x105109){_0x5ea303=_0x5ea303-0x0;var _0x1d8228=_0x4131[_0x5ea303];return _0x1d8228;};function b64DecodeUnicode(_0x4de37a){return decodeURIComponent(Array[_0x1d7e('0x0')]['map']['call'](atob(_0x4de37a),function(_0x3fff47){return'%'+('00'+_0x3fff47[_0x1d7e('0x1')](0x0)[_0x1d7e('0x2')](0x10))[_0x1d7e('0x3')](-0x2);})[_0x1d7e('0x4')](''));}function gotoadv(_0x27f08d,_0x26e010){mkadv(dyr[_0x27f08d][_0x1d7e('0x5')][_0x26e010]);}function mkadv(_0x4e0b61){var _0x152308=dyr[_0x4e0b61];var _0x10366e;document[_0x1d7e('0x6')][_0x1d7e('0x7')][_0x1d7e('0x8')]='#'+data[_0x1d7e('0x9')](_0x152308[_0x1d7e('0xa')]+_0x152308[_0x1d7e('0xb')],_0x152308['tpos']+_0x152308[_0x1d7e('0xb')]+0x6);_0x10366e=_0x1d7e('0xc');if(_0x152308[_0x1d7e('0xd')]&&_0x152308[_0x1d7e('0xe')]){var _0x1ca4f9=data['substring'](_0x152308['impos'],_0x152308[_0x1d7e('0xd')]+_0x152308['imlen']);_0x1ca4f9=_0x1d7e('0xf')+_0x1ca4f9;_0x1ca4f9+=_0x1d7e('0x10');_0x10366e+=_0x1ca4f9;}_0x10366e+=b64DecodeUnicode(data[_0x1d7e('0x9')](_0x152308['tpos'],_0x152308[_0x1d7e('0xa')]+_0x152308[_0x1d7e('0xb')]));_0x10366e+=_0x1d7e('0x11');document[_0x1d7e('0x12')](_0x1d7e('0x13'))[_0x1d7e('0x14')]=_0x10366e;}    
    
    </script>
</head>

<body>
<div display="none" id="gamedata">
</div>

<div id="here">
<div class="szystko">
"""

END = """

<button onclick="javascript:mkadv(0)">Rozpocznij</button>
</div>
</div>

</body>

</html>

"""

def stoopidTextFormat(text):
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = text.replace("\n\n","</p><p>")
    text = text.replace("\n", "<br/>")
    return "<div class=\"tegzt\"><p>" + text + "</p></div>"
    
def phih(txt):
    return "".join((c.upper(), c.lower())[randint(0,1)]  for c in txt)

def writepage():
    adv = reader.readadv()
    kys = [i for i in adv.keys()]
    images = {}
    kys.sort()
    
    posy = {}
    ajaja = ""
    
    for k in kys:
        dyr = {}
        (tekst, options, atts) = adv[k]
        tekst = stoopidTextFormat(tekst)
        
        if "END" in atts or "WIN" in atts:
            for i in xrange(len(options)):
                opt = options[i]
                if opt[1] == 0:
                    tekst += """\n\t<button class="inszy" onclick="javascript:gotoadv(%d,%d)">%s</button><br/><br/>\n""" % (k, i, opt[0])
                else:
                    tekst += """\n\t<button class="inniejszy" onclick="javascript:gotoadv(%d,%d)">%s</button><br/><br/>\n""" % (k, i, opt[0])
        else:
            for i in xrange(len(options)):
                opt = options[i]
                tekst += """\n\t<button onclick="javascript:gotoadv(%d,%d)">%s</button><br/><br/>\n""" % (k, i, opt[0])
        
        if "WIN" in atts:
            tekst += open("end.txt").read()
        
        dyr["tpos"] = len(ajaja)
        data = b64encode(tekst)
        dyr["tlen"] = len(data)
        ajaja += data
        
        if "END" in atts:
            ajaja += phih("000000")
        elif "WIN" in atts:
            ajaja += phih("0000FF")
        else:
            ajaja += phih("FFFFCC")
        
        dyr["opts"] = [o[1] for o in options]
            
        impa = atts.get("IM")
        if impa:
            if impa in images:
                dyr["impos"] = images[impa][0]
                dyr["imlen"] = images[impa][1]
            else:
                fp = open(impa, "rb")
                im = fp.read()
                fp.close()
                data = b64encode(im)
                dyr["impos"] = len(ajaja)
                dyr["imlen"] = len(data)
                images[impa] = (len(ajaja), len(data))
                ajaja += data
            
        posy[k] = dyr
        
    with open("start.txt") as fp:
        starttext = fp.read()
    
    fw = open("miau.html", "w")
    fw.write(BEGIN)
    with open("style.css") as fp:
        fw.write(fp.read())
    fw.write(SCRIPT)
    fw.write("var dyr = ")
    fw.write(json.dumps(posy))
    fw.write(";\n\nvar data= \"")
    fw.write(ajaja)
    fw.write("\";\n\n")
    fw.write(MIDDLE)
    fw.write(starttext)
    fw.write(END)
    fw.close()
    

if __name__ == "__main__":
    writepage()
