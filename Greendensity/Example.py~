from Geolocation import geolocate 
from URL import map_at, Url
from Png import count_green_in_png,is_green
from Visualise import show_green_in_png
from Plot import plot_city_green,plot_density_of_green


london_location=geolocate("London")

print london_location  

print Url(london_location) 

print count_green_in_png(map_at(*london_location))

plot_density_of_green("London","Birmingham")
plot_city_green("London")



