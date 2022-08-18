from PIL import Image
import qrcode

# brand name
brand = "Accesorii ambarcatiuni"

# website url
url = "https://accesoriiambarcatiuni.ro/"

# save logo (make sure it you give the correct path)
logo_link = "cropped-1516968907550-400x400.jpg"
logo = Image.open(logo_link)

# basewidth (Can be any size, preferably between 100-150)
basewidth = 100


# adjusting image size
widthPercent = (basewidth/float(logo.size[0]))
heightSize = int((float(logo.size[0])*float(widthPercent)))
logo = logo.resize((basewidth, heightSize), Image.ANTIALIAS)
code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# add url to the qr code & generate it
code.add_data(url)
code.make()

# adding the color to the code (color of code = fill_color & background color = back_color)
qrImg = code.make_image(fill_color="black", back_color="white").convert('RGB')

# adjust size of the code
pos = ((qrImg.size[0] - logo.size[0]) // 2,
       (qrImg.size[1] - logo.size[1]) // 2)
qrImg.paste(logo, pos)

# save the png
qrImg.save(brand + '.png')