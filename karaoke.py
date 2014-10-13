#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import smallsmilhandler
import sys
import os
from xml.sax import make_parser

com = sys.argv

def download_items(tags):
    for tag in tags:
        atts = tag[1]
        for att in atts:
            if atts[att][0:7] == "http://":
                os.system("wget -q " + atts[att])
                campos = atts[att].split('/')
                atts[att] = campos[len(campos)-1]

def print_tags(tags):
    for tag in tags:
        name = tag[0]
        print name,

        atts = tag[1]
        for att in atts:
            if atts[att] != "":
                print "\t" + att + '="' + atts[att] + '"',
        print

if len(com) == 2:

    parser = make_parser()
    sHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)

    try:
        parser.parse(open(com[1]))

    except IOError:
        print "Error: Document not found"

    tags = sHandler.get_tags()

    download_items(tags)
    print_tags(tags)

else:
    print "Usage: python karaoke.py file.smil"
