from gps_class import GPSVis

vis = GPSVis(
    data_path=4,                                    # <--- data file with GSM positions (change only this row)
    locations="data-locations.csv",                 # restaurants and residences
    map_path="dat-map.png",                        # Map downloaded from OSM (https://www.openstreetmap.org/export)
    points=(44.4838, 25.9844, 44.3970, 26.1578)     # Two coordinates of the map (upper left, lower right)
)

vis.create_image(color=(0, 0, 255), width=5)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

# print()
