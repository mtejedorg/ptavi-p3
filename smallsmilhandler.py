#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.tags = []

    def startElement(self, name, attrs):
        
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            rootlayout = {}
            rootlayout['width'] = attrs.get('width',"")
            rootlayout['height'] = attrs.get('height',"")
            rootlayout['background-color'] = attrs.get('background-color',"")

            self.tags.append(["root-layout", rootlayout])

        elif name == 'region':

            region = {}
            region['id'] = attrs.get('id',"")
            region['top'] = attrs.get('top',"")
            region['bottom'] = attrs.get('bottom',"")
            region['left'] = attrs.get('left',"")
            region['right'] = attrs.get('right',"")

            self.tags.append(["region", region])

        elif name == 'img':

            img = {}
            img['src'] = attrs.get('src',"")
            img['region'] = attrs.get('region',"")
            img['begin'] = attrs.get('begin',"")
            img['dur'] = attrs.get('dur',"")

            self.tags.append(["img", img])

        elif name == 'audio':

            audio = {}
            audio['src'] = attrs.get('src',"")
            audio['begin'] = attrs.get('begin',"")
            audio['dur'] = attrs.get('dur',"")

            self.tags.append(["audio", audio])

        elif name == 'textstream':

            textstream = {}
            textstream['src'] = attrs.get('src',"")
            textstream['region'] = attrs.get('region',"")

            self.tags.append(["textstream", textstream])

    def get_tags(self):
        return self.tags

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))

    print sHandler.get_tags()



