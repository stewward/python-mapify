#This program shows top 25 tourist attractions in the world map
import folium
import pandas

#Seperate csv files for different continents of the world
Africa_data = pandas.read_csv("Africa.csv")
africa_lat = list(Africa_data["LAT"])
africa_lon = list(Africa_data["LON"])
africa_name = list(Africa_data["NAME"])
africa_cont = list(Africa_data["CONT"])

Asia_data = pandas.read_csv("Asia.csv")
asia_lat = list(Asia_data["LAT"])
asia_lon = list(Asia_data["LON"])
asia_name = list(Asia_data["NAME"])
asia_cont = list(Asia_data["CONT"])

Europe_data = pandas.read_csv("Europe.csv")
europe_lat = list(Europe_data["LAT"])
europe_lon = list(Europe_data["LON"])
europe_name = list(Europe_data["NAME"])
europe_cont = list(Europe_data["CONT"])

North_America_data = pandas.read_csv("North America.csv")
north_america_lat = list(North_America_data["LAT"])
north_america_lon = list(North_America_data["LON"])
north_america_name = list(North_America_data["NAME"])
north_america_cont = list(North_America_data["CONT"])

Oceania_data = pandas.read_csv("Oceania.csv")
oceania_lat = list(Oceania_data["LAT"])
oceania_lon = list(Oceania_data["LON"])
oceania_name = list(Oceania_data["NAME"])
oceania_cont = list(Oceania_data["CONT"])

South_America_data = pandas.read_csv("South America.csv")
south_america_lat = list(South_America_data["LAT"])
south_america_lon = list(South_America_data["LON"])
south_america_name = list(South_America_data["NAME"])
south_america_cont = list(South_America_data["CONT"])

#Makes links to the places 
html = """
<b> Place: \b <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""

#This functions allows the icon to change the colour accordingly 
def cont_color_maker(contine):
    if contine == "North America":
        return 'green'
    elif contine == "Asia ":
        return 'pink'
    elif contine == "Africa":
        return 'cadetblue'
    elif contine == "South America":
        return 'beige'
    elif contine == "Europe":
        return 'darkpurple'
    elif contine == "Oceania":
        return 'lightgray'


#Map layout
map = folium.Map(location=[40.730610, -73.935242], tiles='Stamen Toner',
                zoom_start=2, control_scale=True, prefer_canvas=True)

#Creates feature groups according to each continent they're in 
fg_one = folium.FeatureGroup(name = "North America")
fg_two = folium.FeatureGroup(name = "South America")
fg_three = folium.FeatureGroup(name = "Asia")
fg_four = folium.FeatureGroup(name = "Africa")
fg_five = folium.FeatureGroup(name = "Europe")
fg_six = folium.FeatureGroup(name = "Oceania")

for lt, ln, nm, ct in zip(north_america_lat, north_america_lon, north_america_name, north_america_cont):
    iframe = folium.IFrame(html=html % (nm, nm), width=190, height=100)
    fg_one.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon=folium.Icon(color = cont_color_maker(ct))))

for lt, ln, nm, ct in zip(south_america_lat, south_america_lon, south_america_name, south_america_cont):
    iframe = folium.IFrame(html=html % (nm, nm), width=250, height=100)
    fg_two.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon=folium.Icon(color = cont_color_maker(ct))))

for lt, ln, nm, ct in zip(asia_lat, asia_lon, asia_name, asia_cont):
    iframe = folium.IFrame(html=html % (nm, nm), width=150, height=100)
    fg_three.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon=folium.Icon(color = cont_color_maker(ct))))

for lt, ln, nm, ct in zip(africa_lat, africa_lon, africa_name, africa_cont):
    iframe = folium.IFrame(html=html % (nm, nm), width=250, height=100)
    fg_four.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon=folium.Icon(color = cont_color_maker(ct))))

for lt, ln, nm, ct in zip(europe_lat, europe_lon, europe_name, europe_cont):
    iframe = folium.IFrame(html=html % (nm, nm), width=150, height=100)
    fg_five.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon=folium.Icon(color = cont_color_maker(ct))))

for lt, ln, nm, ct in zip(oceania_lat, oceania_lon, oceania_name, oceania_cont):
    iframe = folium.IFrame(html=html % (nm, nm), width=120, height=90)
    fg_six.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon=folium.Icon(color = cont_color_maker(ct))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('global_pop_data.json', 'r', encoding='utf-8-sig').read()))

map.add_child(fgp)
map.add_child(fg_one)
map.add_child(fg_two)
map.add_child(fg_three)
map.add_child(fg_four)
map.add_child(fg_five)
map.add_child(fg_six)
map.add_child(folium.LayerControl())
map.save("mapify4.html")