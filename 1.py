from PIL import Image, ImageDraw
import numpy as np

inputImage = Image.open("Lena.jpeg")
# inputImage.show()

width, height = inputImage.size
pixels = np.array(inputImage.getdata()).reshape(width, height,3)
# print(pixels[0,2])
pixels = pixels.astype(np.uint8)
red_image = Image.fromarray(pixels[:, :, 0])
# red_image.show()

im_resize = inputImage.resize((256,256)) #by default it is nearest  interpolation
# im_resize.show()

im_rotated = inputImage.rotate(45) 
# im_rotated.show()

im_flip = inputImage.transpose(Image.FLIP_TOP_BOTTOM) 
# im_flip.show()

im_gray = inputImage.convert("L")
# im_gray.show()

im_cmyk = inputImage.convert("CMYK")
# im_cmyk.show()

im_hsv = inputImage.convert("HSV")
# im_hsv.show()
hsv_val = list(im_hsv.getdata())
# print(hsv_val)

for i in range(height):
    inputImage.putpixel((i,i),(0,0,0))

# inputImage.show()

txt = "Suvan has Aura"
impDrawer = ImageDraw.Draw(inputImage)
impDrawer.text((5,30),txt)
inputImage.show()
