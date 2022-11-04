import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def text2png(code, lang):
    code = code.replace("\t", "    ")
    background = (255, 255, 255)

    fontsize = 14
    font_path = Path.cwd() / 'models/wysiwim/vis_st/FreeMonoBold.ttf'
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', fontsize)

    width, height = ImageDraw.Draw(Image.new('RGBA', (1,1), background)).textsize(code, font)
    image = Image.new('RGBA', (int(width * 1.1), int(height * 1.1)), background)
    draw = ImageDraw.Draw(image)
    draw.text((10, 2), code, fill='black', font=font)
    return image

def from_to_file_st(code, out_path, lang, img_name):
    image = text2png(code, lang)
    image.save(str(out_path / img_name), dpi=(600, 600))

if __name__ == "__main__":
    from_to_file_st("<path>/example.java", "<path>/example_simple_text.png")