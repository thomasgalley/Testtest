from argparse import ArgumentParser
from Geolocation import geolocate
def process():
   parser = ArgumentParser(description = "Locate city")

   parser.add_argument('city')
   
   arguments= parser.parse_args()

   print geolocate(arguments.city)

if __name__ == "__main__":
    process()
