import qrcode
data=input("Enter URL:").strip()
filename=input("Enter file name:").strip()

if not filename.endswith(".png"):
    filename += ".png"
    
qr=qrcode.QRCode(box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill_color="black",back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")