#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

strinit = "null value"

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.root-layout = {'w':'', 'h':'', 'bc':''}
        self.region = []
        self.img = []
        self.audio = []
        self.textstream = []

    def startElement(self, name, attrs):
        
        if name == 'chiste':
            # De esta manera tomamos los valores de los atributos
            self.root-layout['w'] = attrs.get('width',"")
        elif name == 'pregunta':
            self.inPregunta = 1
        elif name == 'respuesta':
            self.inRespuesta = 1

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'pregunta':
            self.pregunta = ""
            self.inPregunta = 0
        if name == 'respuesta':
            self.respuesta = ""
            self.inRespuesta = 0

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inPregunta:
            self.pregunta = self.pregunta + char
            print
            print "Pregunta: " + self.pregunta
        if self.inRespuesta:
            self.respuesta += char
            print "Respuesta:        " + self.respuesta
            print

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes2.xml'))
