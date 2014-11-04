# test whether geolocate function returns correct coordinates by comparing to known values
from nose.tools import assert_almost_equal
from Geolocation import geolocate
def test_actual_locations():
    actualParis = [48.8567,2.3508]
    for i in range (0,1):
        assert_almost_equal(geolocate("Paris")[i],actualParis[i], 2)
