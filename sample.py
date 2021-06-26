import web
import reader
from base64 import b64encode
        
urls = (
    '/(.*)', 'Adventures'
)
app = web.application(urls, globals())

def getstyle():
    with open("style.css") as fp:
        return "\n<style>\n" + fp.read() + "</style>\n"

def startPage():
    #text = """<?xml version="1.0" encoding="UTF-8"?>\n"""
    text = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n"""
    text += """<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n"""
    text += getstyle() + "</head>"
    text += "<body><div class=\"szystko\">\n"
    text += open("start.txt").read()
    text += """\n\n<form><button type="submit" formaction="0" formmethod="get">Rozpocznij</button></form>\n"""
    text += "</div>"
    text += "</body></html>\n"
    return text
    
def stoopidTextFormat(text):
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = text.replace("\n\n","</p><p>")
    text = text.replace("\n", "<br/>")
    return "<div class=\"tegzt\"><p>" + text + "</p></div>"
    
def imageText(impa):
    text = "<p><img alt=\"Obrazek\" src=\"data:image/jpg;base64,"
    fp = open(impa, "rb")
    im = fp.read()
    fp.close()
    text += b64encode(im)
    text += "\"/></p>"
    return text

def advPage(num):
    adv = reader.readadv()
    if num not in adv:
        return ":("
    (tekst, options, atts) = adv[num]
    
    text = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n"""
    text += """<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n"""
    text += getstyle() + "</head>"
    if "END" in atts:
        text += "<body style=\"background-color:#000000\"><div class=\"szystko\">"
    elif "WIN" in atts:
        text += "<body style=\"background-color:#0000FF\"><div class=\"szystko\">"
    else:
        text += "<body style=\"background-color:#FFFFCC\"><div class=\"szystko\">\n"
    impa = atts.get("IM")
    if None != impa:
        text += imageText(impa)
    text += stoopidTextFormat(tekst)
    text += "\n\n<form>"
    
    if "END" in atts or "WIN" in atts:
        for opt in options:
            if opt[1] == 0:
                text += """\n\t<button class="inszy" type="submit" formaction="%d" formmethod="get">%s</button><br/><br/>\n""" % (opt[1], opt[0])
            else:
                text += """\n\t<button class="inniejszy" type="submit" formaction="%d" formmethod="get">%s</button><br/><br/>\n""" % (opt[1], opt[0])
    else:
        for opt in options:
            text += """\n\t<button type="submit" formaction="%d" formmethod="get">%s</button><br/><br/>\n""" % (opt[1], opt[0])
            
    if "WIN" in atts:
        text += "</form>\n"
        text += open("end.txt").read()
        text += "</div></body></html>\n"
    else:
        text += "</form></div></body></html>\n"
    return text

class Adventures:
    
    def GET(self, number):
        if not number:
            return startPage()
        elif number.isdigit():
            return advPage(int(number))
        else:
            return startPage()

if __name__ == "__main__":
    app.run()
