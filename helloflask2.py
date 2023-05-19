from flask import Flask

import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (36.128, -115.165)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    
    fashion_mall = (36.127, -115.171)
    las = (36.085, -115.151)  
    black_mnt = (36.020, -114.988) 

    # Add markers to the map
     # popup --> label for the Marker; click on the pins on the map!
    folium.Marker(fashion_mall, popup = 'Fashion Snow Mall', icon=folium.Icon(color='red', icon='glyphicon glyphicon-globe', prefix='fa')).add_to(folium_map)
    folium.Marker(las, popup = 'Las Vegas Airport', icon=folium.Icon(color='blue', icon='glyphicon glyphicon-plane')).add_to(my_map)
   folium.Marker(black_mnt, popup = 'Black Mountain', icon=folium.Icon(color='green', icon='glyphicon glyphicon-tree-conifer')).add_to(my_map)
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224, debug=True)

