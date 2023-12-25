import pyqrcode
import png
from pyqrcode import QRCode

while True:
    s = input()
    if "www" in s:
        url = pyqrcode.create(s)
        # url.svg(f"{s}qr.svg", scale=8)
        url.png(f"{s}qr.png", scale=6)
        print("QR code generated successfully")
    else:
        break
