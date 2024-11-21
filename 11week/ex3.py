import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save__path = 'qr_data.png'
qr_img.save(save__path)