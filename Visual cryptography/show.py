import os
from PIL import Image
import sys
infile1 = Image.open(os.path.join('C:\\Users\\NIlo16\\Desktop\\visual_crypto-master\\ciphered.png'))
infile2 = Image.open(os.path.join('C:\\Users\\NIlo16\\Desktop\\visual_crypto-master\\secret.png'))

outfile = Image.new('1', infile1.size)
for x in range(infile1.size[0]):
    for y in range(infile1.size[1]):
        outfile.putpixel((x, y), max(infile1.getpixel((x, y)), infile2.getpixel((x, y))))
outfile.show()