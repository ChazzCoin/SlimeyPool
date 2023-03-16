# import modules
import base64

import qrcode
from qrcode import main
from PIL import Image
from F import OS

# taking image which user wants
# in the QR code center
cwd = OS.get_cwd()


def get_logo(file_name_and_path:str):
       return Image.open(file_name_and_path)

def prepare_logo(file_name_and_path:str):
       # taking base width
       basewidth = 100
       # adjust image size
       logo = get_logo(file_name_and_path)
       wpercent = (basewidth / float(logo.size[0]))
       hsize = int((float(logo.size[1]) * float(wpercent)))
       return logo.resize((basewidth, hsize), Image.ANTIALIAS)

# # taking url or text
# data = 'Selim is gay as shit! '

def make_qr_code(data) -> main.QRCode:
       # adding URL or text to QRcode
       QRcode = main.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
       QRcode.add_data(data)
       # generating QR code
       QRcode.make()
       return QRcode

def generate_and_save_qr_image(qrcode:main.QRCode, export_path:str, file_name_and_path:str, color:str):
       # taking color name from user
       QRcolor = color
       # adding color to QR code
       QRimg = qrcode.make_image(fill_color=QRcolor, back_color="purple").convert('RGB')
       logo = prepare_logo(file_name_and_path)
       # set size of QR code
       pos = ( (QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2 )
       # QRimg.paste(logo, pos)
       # save the QR code generated
       QRimg.save(export_path)
       print('QR code generated!')

# cwd = OS.get_cwd()
img = None
with open(f"{cwd}/utb_qr.jpg", "rb") as f:
    img = f.read()
    # UU = data12.encode("base64")
    # UUU = base64.b64decode(UU)
    # pass

encoded_string= base64.b64encode(img)
d = encoded_string.decode('utf-8')
print(d)

qr = make_qr_code(encoded_string)
generate_and_save_qr_image(qr, f"{cwd}/utb_qr1.jpg", f"{cwd}/utb.jpg", "black")