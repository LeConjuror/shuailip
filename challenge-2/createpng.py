import base64
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.PngImagePlugin import PngInfo
import numpy as np

flag = "picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}"

encoded_base64 = base64.b64encode(flag.encode())

encoded_base64_str = encoded_base64.decode('ascii')

encoded_bin = ''.join(format(ord(char), '08b') for char in encoded_base64_str)

binary_string = ''.join('1' if bit == '1' else '0' for bit in encoded_bin)

img = Image.new('RGBA', (128, 128), 'red')
pixels = np.array(img)

for x in range(128):
    index = 0
    for y in range(128):
        # Extract four bits
        bits = binary_string[index:index+4]
        index += 4
        
        # Modify the RGBA values
        r, g, b, a = pixels[x, y]
        r = (r & 0xFE) | int(bits[0])
        g = (g & 0xFE) | int(bits[1])
        b = (b & 0xFE) | int(bits[2])
        a = (a & 0xFE) | int(bits[3])
        pixels[x, y] = [r, g, b, a]

# Convert the numpy array back to an image
img = Image.fromarray(pixels)

poem = """Crimson heart, vibrant and bold,
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke."""

meta = PngInfo()
meta.add_text('Poem', poem)
img.save('red.png', pnginfo=meta)