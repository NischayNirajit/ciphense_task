import folium
import csv


check_map = folium.Map(location = [20.5937, 78.9629],zoom_start = 8 )


data = None    
with open('data.csv','r') as f:
    reader = csv.reader(f.read().splitlines(), delimiter=',')
    data = [row for row in reader]
del data[0]
for pops in data:
	count+=1
    k = int(pops[1])
    if k>500000:
        getstring = i[2]
        getloc = k[31:]
        coordinates = g.split(',')
        coordinates = [float(c) for c in cood]
        city = pops[0]
        folium.Marker(coordinates, popup='<i>population: {}</i>'.format(k), tooltip='<i>{}</i>'.format(city)+'<br/>'+'click for more').add_to(check_map)



check_map.save(" my_map1.html " )