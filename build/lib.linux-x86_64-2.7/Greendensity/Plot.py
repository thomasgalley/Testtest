import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from Png import is_green, count_green_in_png
from URL import map_at
from Geolocation import geolocate
from Points import location_sequence 
from Visualise import show_green_in_png

def plot_density_of_green(city1,city2):
   
   plt.plot([
    count_green_in_png(
        map_at(*location,zoom=10,satellite=True))
          for location in location_sequence(
              geolocate(city1),
              geolocate(city2),10)])
   plt.savefig('greengraph.png')
   return

def plot_city_green(city1):
   with open('green.png','w') as green:
       green.write(show_green_in_png(map_at(*geolocate(city1),zoom=10,satellite=True)))

   return 
