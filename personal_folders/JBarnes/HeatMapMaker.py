import pandas as pd
from folium import Map
from folium.plugins import HeatMap

# https://techwetrust.com/how-to/how-to-make-a-geographical-heat-map-with-python/

def create_heat_map(file_name : str) -> None:

    df = pd.read_csv(file_name)
    latitudes = df["latitude"]
    longitudes = df["longitude"]
    center_location = (sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes))

    base_map = Map(location=center_location, zoom_start=13)

    hm_wide = HeatMap(
        list(zip(latitudes, longitudes)),
        min_opacity=0.2,
        radius=17, 
        blur=15, 
        max_zoom=1,
    )

    base_map.add_child(hm_wide)

    return base_map

if __name__ == "__main__":
    pass
    #example use 