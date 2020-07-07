from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open('listarank.jpeg')

time = 1
date = 2020 

w, h = img.size
drawing = ImageDraw.Draw(img)
font = ImageFont.truetype("Roboto-Regular.ttf", 16)
text = f"© Pakard {time}{date} "
text_w, text_h = drawing.textsize(text, font)
pos = ((w - text_w) - 250), ((h - text_h) - 5)
c_text = Image.new('RGB', (text_w, (text_h)), color = "#FFFFFF")
drawing = ImageDraw.Draw(c_text)
drawing.text((0,0), text, fill='#000000', font = font)

img.paste(c_text, pos)
img.save('listarankpt.jpeg')
img.show('listarankpt.jpeg')