from PIL import Image
import numpy as np
import base64
import os

# Load the image
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'red.png')
img = Image.open(img_path)
pixels = np.array(img)
metadata = img.info
print(f'Metadata: {metadata}')

# Initialize the variable to store the extracted binary data
extracted_bin = []

# Extract the LSB of each color component of each pixel
for x in range(128):
    r, g, b, a = pixels[0, x]
    extracted_bin.append(r & 0x01)
    extracted_bin.append(g & 0x01)
    extracted_bin.append(b & 0x01)
    extracted_bin.append(a & 0x01)

# Convert the list of bits back to a binary string
binary_string = ''.join(str(bit) for bit in extracted_bin)
ascii_string = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
flag = base64.b64decode(ascii_string).decode()
print(f'Flag: {flag}')