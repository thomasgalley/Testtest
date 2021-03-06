from argparse import ArgumentParser
from Geolocation import geolocate
from Plot import plot_city_green, plot_density_of_green

def process():
   parser = ArgumentParser(description = "Locate city")

   parser.add_argument('city')
   parser.add_argument('secondcity')
   
   
   arguments= parser.parse_args()

   print geolocate(arguments.city)
   print geolocate(arguments.secondcity)
   plot_city_green(arguments.city)
   plot_density_of_green(arguments.city, arguments.secondcity)

if __name__ == "__main__":
    process()
