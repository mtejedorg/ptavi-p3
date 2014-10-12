#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import smallsmilhandler

com = sys.argv

if len(com) == 2:

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    try:
        parser.parse(open(com[1]))

    tags = sHandler.get_tags()
    
    print tags

    except IOError:
        print "Error: Document not found"
 
else:
    print "Usage: python karaoke.py file.smil"
