# 3 Python dictionary with keys having multiple inputs

dict1 = {}
x, y, z = 10, 20, 30
dict1[x, y, z] = x+y-z

x, y, z = 5, 10, 30
dict1[x, y, z] = x+y-z
print(dict1)


print("--- example2 ---")

# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"): "Mumbai", \
          ("28.33'34.1", "77.06'16.6"): "Delhi"}

print(places)
print('\n')
latitude = []
longitude = []
place = []
for i in places:
    latitude.append(i[0])
    longitude.append(i[1])
    #place.append(places[i])
    # OR
    place.append(places[i[0], i[1]])
print("latitude: ", latitude)
print("longitude: ", longitude)
print("place: ", place)
