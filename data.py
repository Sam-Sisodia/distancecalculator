from geopy.geocoders import Nominatim
from geopy import distance


geocoder = Nominatim(user_agent="I know Python")

location1 = input("Enstet the loc 1 :")
location2 = input("Enstet the loc 2 :")


cordinate1 = geocoder.geocode(location1)
cordinate2 = geocoder.geocode(location2)

lat1,lon1 = (cordinate1.latitude) ,(cordinate1.longitude)

lat2,lon2 = (cordinate2.latitude) ,(cordinate2.longitude)

place1 = (lat1,lon1)

palce2 = (lat2,lon2)


print(distance.distance(place1,palce2))

