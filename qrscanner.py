import qrcode

myqr = qrcode.make("https://www.youtube.com/watch?v=LhSv6FH9g4o")
myqr.save("myqr.png")
