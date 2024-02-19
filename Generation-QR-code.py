#QR CODE GENERATOR
import pyqrcode
import png
from pyqrcode import QRCode

#String represent the QR Code
site="https://www.instagram.com/ahmadfurqan7/"
#whatever u want :)

#Generate QR code
url_qr=pyqrcode.create(site)

#Create and Save the svg file naming
url_qr.svg("qr-instagram.svg",scale=8)

#Create and Save the png file naming
url_qr.png("qr-instagram.png",scale=6)

#Done :)
