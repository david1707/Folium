
import folium

# Create map object
m = folium.Map(location=[38.540205,-0.140560], zoom_start=14)

tooltip = 'Click here for more info'

# Landforms
folium.Marker([38.534019,-0.118618], 
                popup="<strong>Llevant's Beach</strong>",
                tooltip=tooltip).add_to(m)

folium.Marker([38.535840,-0.144041], 
                popup="<strong>Ponent's Beach</strong>",
                tooltip=tooltip).add_to(m)
                
folium.Marker([38.534314,-0.131248], 
                popup="<strong>Old Benidorm City</strong>",
                tooltip=tooltip).add_to(m)

# Parks
folium.Marker([38.542508,-0.130322], 
                popup="<strong>L'Aigüera Park</strong>",
                tooltip=tooltip).add_to(m)

folium.Marker([38.5401882,-0.0940192], 
                popup="<strong>Aqualandia / Mundomar</strong>",
                tooltip=tooltip).add_to(m)



m.save('map.html')

38.5431882,-0.1089192