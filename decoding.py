from pyzbar.pyzbar import decode
from PIL import Image

d=decode(Image.open('abc.png'))

print(d)