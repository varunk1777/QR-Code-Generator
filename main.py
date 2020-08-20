import pyqrcode
#from pyzbar.pyzbar import decode
#from PIL import Image
#generating QR CODE
querry=input("Enter a url to make QR Code:")

qr=pyqrcode.create(querry)
qr.png('abc.png',scale=8)

#reading QR CODE

#d=decode(Image.open('E:\pycharm projects\QRCode\ abc.png'))

#print(d)