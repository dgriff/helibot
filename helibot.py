from PIL import ImageGrab
from PIL import Image
import time
import win32api
import win32con

def click_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def click_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def find_img(haystack, needle):
    # take large image and small image and return coordinates of first occurance of small image in large
    haystackfast = haystack.load() # optimization
    needlefast = needle.load() # optimization
    for x in xrange(0, haystack.size[0] - needle.size[0] + 1):
        for y in xrange(0, haystack.size[1] - needle.size[1] + 1):
            if compare(haystack, haystackfast, needle, needlefast, x, y):
                return (x,y)
    return (-1, -1)

def compare(haystack, haystackfast, needle, needlefast, x, y):
    for ix in xrange(needle.size[0]):
        for iy in xrange(needle.size[1]):
            if needlefast[ix, iy] != haystackfast[x + ix, y +iy]:
                return False
    return True

def _test_find_img():
    xii = time.clock()
    assert find_img(Image.open("test1_img.png"), Image.open("test1_green.png")) == (8,6)
    assert find_img(Image.open("test1_img.png"), Image.open("test1_x.png")) == (1,5)
    assert find_img(Image.open("test2_img.png"), Image.open("test2_sig.png")) == (628, 315)
    print "test completed in %.3f seconds" % float(time.clock() - xii)

def _testgrab():
    time.sleep(2)
    xii = time.clock()
    win32api.SetCursorPos((0,0))
    x,y = find_img(ImageGrab.grab(), Image.open("helisig.png"))
    win32api.SetCursorPos((x - 274, y - 193))
    print time.clock() - xii
    
def main():
    #_test_find_img()
    _testgrab()

if __name__ == "__main__":
    main()