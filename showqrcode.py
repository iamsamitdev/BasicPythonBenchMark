import qrcode

qr = qrcode.QRCode()
qr.add_data('https://www.itgenius.co.th')
qr.make()
img = qr.make_image()
img.save('qrcode_test.png')
