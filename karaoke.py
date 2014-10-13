#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import smallsmilhandler
import sys
import os
from xml.sax import make_parser

com = sys.argv

class KaraokeLocal():

    def __init__ (self, fich):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)

        try:
            parser.parse(open(fich))

        except IOError:
            print "Error: Document not found"

        self.tags = sHandler.get_tags()

    def __str__ (self):
        strimp = ""
        for tag in self.tags:
            name = tag[0]
            strimp += name

            atts = tag[1]
            for att in atts:
                if atts[att] != "":
                    strimp += "\t" + att + '="' + atts[att] + '"'
            strimp += "\n"

        return strimp

    def do_local (self):
        for tag in self.tags:
            atts = tag[1]
            for att in atts:
                if atts[att][0:7] == "http://":
                    os.system("wget -q " + atts[att])
                    campos = atts[att].split('/')
                    atts[att] = campos[-1]


if __name__ == "__main__":

    if len(com) == 2:

        Kar = KaraokeLocal(com[1])
        print Kar
        Kar.do_local()
        print Kar

    else:
        print "Usage: python karaoke.py file.smil"
