#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import smallsmilhandler
import sys
from xml.sax import make_parser

com = sys.argv

if len(com) == 2:

    parser = make_parser()
    sHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)

    try:
        parser.parse(open(com[1]))

    except IOError:
        print "Error: Document not found"

    def print_tags
        tags = sHandler.get_tags()
        print tags

else:
    print "Usage: python karaoke.py file.smil"
