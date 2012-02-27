#http://stackoverflow.com/questions/3800458/
#quickly-getting-the-color-of-some-pixels-on-the-screen-in-python-on-windows-7


from PIL import ImageGrab
import time

xii = time.clock()
img = ImageGrab.grab(bbox).load()
#img = ImageGrab.grab().load()
for i in range(100):
    a = img[0,i]

print time.clock() - xii

# load the signature image

# load the image you're checking

# compare the two images

# find the offset where the signature image starts

# # start botting routine

# if it doesnt find anything, try again until force quit

