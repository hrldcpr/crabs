import itertools

from flask import Flask, request, render_template
app = Flask(__name__)

PX = 8

BITMAPS = {}
with open('small_pixel.ttf.txt') as f:
    for i in range(128):
        bitmap = []
        for line in itertools.islice(f, PX):
            line = line[:-1] # remove newline
            row = tuple(c != ' ' for c in line)
            bitmap.append(row)
        BITMAPS[chr(i)] = tuple(bitmap)

@app.route('/')
def index():
    text = request.args.get('s', 'test')
    words = []
    for word in text.split():
        bitmap = [[] for _ in range(PX)]
        for c in word:
            c_bitmap = BITMAPS.get(c)
            if c_bitmap:
                for row, c_row in zip(bitmap, c_bitmap):
                    row += c_row
        words.append(bitmap)
    return render_template('index.html', words=words)

if __name__ == '__main__':
    app.run(debug=True)
