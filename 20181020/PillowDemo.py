from PIL import Image

im = Image.open('f:\\GitHub\\test.jpg')
w,h=im.size
print('Origin image size:%sx%s' %(w,h))
im.thumbnail((w//2,h//2))