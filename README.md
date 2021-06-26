
#Clickventure creator

Bunch of ugly python scripts for creating simple "choose-your-own-adventure" browser games.

Inspired by the excellent clickventures on clickhole.com 

The resulting game is a single html document with embedded graphics and javascript code.
It is not very elegant nor sophisticated, but can be shared easily and requires no server side
code.


## Requirements

python2 is required for running scripts. Can be easily ported to python3 I guess..

web.py package is needed if you want to use demo feature (sample.py)

Image package is needed if you want to use picprocess scirpt (optional).

Modern, javascript-enabled browser is needed for "running" the games.

## Usage

1. Steal some silly looking stock photos from the internet and put them in picsOriginal folder.

picprocess.py - the script will resize all pictures in picOriginal folder to somewhat simillar size
and copy the result to pics folder

This is not necessary, but can be helpful to speed up development.


2. Create game script.

Game script goes to one or more files named with following template: ppp*.txt

See attached ppp_DEMO.txt as an example.

You also need files start.txt (introductory text for your game) and end.txt - an extra text for the winner.

All game script files should be encoded in UTF8 format.



3. Validate your game script.

Run reader.py script. It will check if there are no obvious errors, such as paths that lead nowhere.
It will also warn you if you create short-circut (circular path).


4. Start your game in demo mode.

Run sample.py script. It will start simple web server that you can use to test your game "live".
You can edit your game script while playing and "forward" and "back" buttons will work "normally" in the brower
which makes it easier to experiment and debug.

This step can be skipped, however and you can go straight into


5. Generate "production" game.

Run writer.py script. It will package your game as a single html file (together with images and everything).
Depending on number and size of images, this file can get quite big, so be careful.

Now you can share your game by sending html file to your friends and family or putting it on web server.
There is no server side logic necessary.



## Principle of operation.

The entire game is stored in html document (client side). Therefore it is entirely possible for players to cheat and look up what
is the correct path in html code. That being said, a bit of obfuscation was added to make it not so easy without at least a little bit
of work and knowledge how code works.

Both images and text data are encoded as base64 and decoded on runtime by javascript code.

The script gets transformed to one big javascript dictionary.


