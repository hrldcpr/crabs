import sys

from PIL import Image, ImageFont, ImageDraw

PX = 8

TTF_PATH = sys.argv[1]
font = ImageFont.truetype(TTF_PATH, PX)

im = Image.new('RGB', (PX, 128 * PX))
draw = ImageDraw.Draw(im)

def get_bitmap(i):
    bitmap = []
    for y in range(i * PX, (i + 1) * PX):
        row = []
        for x in range(PX):
            p = im.getpixel((x, y))
            if p == (0, 0, 0):
                row.append(False)
            elif p == (255, 255, 255):
                row.append(True)
            else:
                return # characters with grey are weird
        bitmap.append(row)
    return bitmap

with open(TTF_PATH + '.txt', 'w') as f:
    for i in range(128):
        draw.text((0, i * PX), chr(i), font=font, fill="white")
        bitmap = get_bitmap(i)
        if bitmap:
            f.write(''.join(''.join('#' if b else ' ' for b in row) + '\n'
                            for row in bitmap))
        else:
            f.write((' '*PX + '\n') * PX)

im.save(TTF_PATH + '.png')
