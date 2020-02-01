
from PIL import Image


# Open the image and create it's instance
img = Image.open("sample.jpg")

# Gives the dimensions or the size of the image
print (img.size)

# Gives the width of the image
print (img.width)

# Gives the width of the image
print (img.height)


# Gives the format of image like JPEG, PNG ...
print (img.format)

# Gives the mode of image like RGB, binary, GreyScale ...
print (img.mode)

# Displays the Image
img.show()


# Rotate the image with the given angle
# Create separate instance for rotated image
# ROTATE_90, ROTATE_180, ROTATE_270
img_rotate = img.transpose(Image.ROTATE_180)
 
# Displays the rotated image
img_rotate.show()  

img_rotate.save("sample1.jpg")


# Resizing the image
small_im = img.resize((300, 150), resample=Image.BICUBIC)
small_im.save('small_sample1.jpg')


# Creating Thumbnail
img = Image.open("sample.jpg")
img.thumbnail((150, 100))
print(img.width, img.height)
img.save('thumb_sample1.jpg')


# Cropping
img = Image.open("sample.jpg")
                    # startx, starty,width,height
crop_im = img.crop(box=(340, 20, 560, 164))
crop_im.save('crop_sample1.jpg')


# Adding a Border

img = Image.open("sample.jpg")
border_im = Image.new('RGB', (img.width+20, img.height+20), 'yellow')
border_im.paste(img, (10, 10))
border_im.save("border_sample.jpg")


# Flip the image
# Create separate instance for flipped image
# FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM
img_flip = img.transpose(Image.FLIP_TOP_BOTTOM)

# Displays the rotated image
img_flip.show()  
img_flip.save("sample2.jpg")



# Make Black and White image
img_bw = Image.open("sample.jpg")
img_bw.convert(mode='L').save('sample3.jpg')
img_bw = Image.open("sample3.jpg")
img_bw.show()


# Blur the Images
from PIL import Image, ImageFilter
img_blur = Image.open("sample.jpg")

# 15 is the radius, default is 2 so it doesn’t show too much
img_blur.filter(ImageFilter.GaussianBlur(15)).save('sample4.jpg')
img_blur = Image.open("sample4.jpg")
img_blur.show()




