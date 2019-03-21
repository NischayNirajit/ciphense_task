import folium
import csv


check_map = folium.Map(location = [20.5937, 78.9629],zoom_start = 5 )


data = None    
with open('data.csv','r') as f:
    reader = csv.reader(f.read().splitlines(), delimiter=',')
    data = [row for row in reader]
del data[0]
count = 0
for pops in data:
    k = int(pops[1])
    if k>500000:
        count = count+1
        getstring = pops[2]
        getloc = getstring[31:]
        coordinates = getloc.split(',')
        coordinates = [float(i) for i in coordinates]
        city = pops[0]
        folium.Marker(coordinates, popup='<i>population : {}</i>'.format(k), tooltip='<i>{}</i>'.format(city)+'<br/>'+'click for more').add_to(check_map)


print(count)
check_map.save("Indian Population map.html" )