mapa = folim.map(location)
velikost = 5
lat = lat-start
while lat <= lat_end:
    foluim.Polyline([(lat, lon) for lat in range(lat_start, lat_end + 1)], color="blue", weight=2.5, opacity=1).add_to(mapa)
Lon = lon_start
while lon <= lon_end:
    folium.Polyline([(lat, lon) for lon in range(lon_start, lon_end + 1)], color="blue", weight=2.5, opacity=1).add_to(mapa)
    lon += 1
sit =((0 for _ in range(velikost)))
sit[2 , 3] = x 
