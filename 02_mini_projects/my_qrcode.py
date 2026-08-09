import qrcode

data = "https://github.com/Manisasank"

qr = qrcode.make(data)
qr.save("my_qrcode.png")
print("QR code generated and saved as my_qrcode.png")