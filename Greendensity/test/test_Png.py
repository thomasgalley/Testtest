
from nose.tools import assert_equal
from Png import count_green_in_png
import requests

#In the following test we verify that the count_green_in_png returns the correct number of green pixels for a known completly green image png file
#The file is hosted on uncyclopedia and is of dimension 504*360 (=181440) pixels, all of which are green

def test_green_pixel_count():
    assert_equal (count_green_in_png(requests.get("http://img1.wikia.nocookie.net/__cb20060327020342/uncyclopedia/images/7/72/Green.png")), 181440)
