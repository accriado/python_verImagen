import cv2
import urllib.request
import numpy

class Imagenes:

    def __init__(self,url):
        self.url=url

    def convertirUrl(self):

        resp = urllib.request.urlopen(self.url)
        image = numpy.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        return image

url=input("Ingrese la url del archivo imagen jpg o png: ")

im=Imagenes(url)
im.convertirUrl()