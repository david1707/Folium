
import folium

# Create map object
m = folium.Map(location=[38.540205,-0.140560], zoom_start=14)

tooltip = 'Click here for more info'


# Landforms
folium.Marker([38.534019,-0.118618], 
                popup="<strong>Llevant's Beach</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='leaf')).add_to(m)

folium.Marker([38.535840,-0.144041], 
                popup="<strong>Ponent's Beach</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='leaf')).add_to(m)
                
folium.Marker([38.534314,-0.131248], 
                popup="<strong>Old Benidorm City</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='leaf')).add_to(m)


# Parks
folium.Marker([38.542508,-0.130322], 
                popup="<strong>L'Aigüera Park</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='blue', icon='cloud')).add_to(m)

folium.Marker([38.5401882,-0.0940192], 
                popup="<strong>Aqualandia / Mundomar</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='blue', icon='cloud')).add_to(m)

folium.Marker([38.560471,-0.161876], 
                popup="<strong>Terra Mítica Park</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='blue', icon='cloud')).add_to(m)

folium.Marker([38.568873,-0.141899], 
                popup="<strong>Terra Natura</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='blue', icon='cloud')).add_to(m)


# Interesting places
folium.Marker([38.544540,-0.102411], 
                popup="<strong>Benidorm Palace</strong>",
                tooltip=tooltip,
                icon=folium.Icon(color='orange', icon='ok-sign')).add_to(m)

folium.Marker([38.547145,-0.137880], 
                popup="<strong>Benidorm Stadium</strong>",
                tooltip=tooltip,    
                icon=folium.Icon(color='orange', icon='ok-sign')).add_to(m)


m.save('map.html')


