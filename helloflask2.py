from flask import Flask

import folium

app = Flask(__name__)

@app.route('/')
def index():
    lat = input("Enter the location lattidue: ")
    lon = input("Enter the longtitude:")
    start_coords = (lat, lon)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224, debug=True)

