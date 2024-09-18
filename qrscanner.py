import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
myqr = qrcode.make("https://www.youtube.com/watch?v=LhSv6FH9g4o")
myqr.save("myqr.png",scale = 8)
b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))