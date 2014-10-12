#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        # Todo son string. Considerar inicializar con int (0) cuando proceda
        self.rootlayout = {'w':'', 'h':'', 'bc':''}
        self.region = {'id':'', 'top':'', 'bottom':'', 'left':'', 'right':''}
        self.img = {'src':'', 'region':'', 'begin':'', 'dur':''}
        self.audio = {'src':'', 'begin':'', 'dur':''}
        self.textstream = {'src':'', 'region':''}
        self.tags = []

    def startElement(self, name, attrs):
        
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.rootlayout['w'] = attrs.get('width',"")
            self.rootlayout['h'] = attrs.get('height',"")
            self.rootlayout['bc'] = attrs.get('background-color',"")

            self.tags.append(self.rootlayout)

        elif name == 'region':
            # No sé si funciona cuando no están todos los atributos
            self.region['id'] = attrs.get('id',"")
            self.region['top'] = attrs.get('top',"")
            self.region['bottom'] = attrs.get('bottom',"")
            self.region['left'] = attrs.get('left',"")
            self.region['right'] = attrs.get('right',"")

            self.tags.append(self.region)

        elif name == 'img':
            # No sé si funciona cuando no están todos los atributos
            self.img['src'] = attrs.get('src',"")
            self.img['region'] = attrs.get('region',"")
            self.img['begin'] = attrs.get('begin',"")
            self.img['dur'] = attrs.get('dur',"")

            self.tags.append(self.img)

        elif name == 'audio':
            # No sé si funciona cuando no están todos los atributos
            self.audio['src'] = attrs.get('src',"")
            self.audio['begin'] = attrs.get('begin',"")
            self.audio['dur'] = attrs.get('dur',"")

            self.tags.append(self.audio)

        elif name == 'textstream':
            # No sé si funciona cuando no están todos los atributos
            self.textstream['src'] = attrs.get('src',"")
            self.textstream['region'] = attrs.get('region',"")

            self.tags.append(self.textstream)

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



