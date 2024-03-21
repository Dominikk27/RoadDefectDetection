import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from haversine import haversine

import geopandas as gpd
import cartopy.crs as ccrs
import contextily as ctx
import xyzservices.providers as xyz

import os

class KML_stuff():
    def __init__(self):
        self.result_path = ""

    #########################################
    ##   VÝPOČET PRELETENEJ VZDIAELNOSTI   ##
    #########################################

    def calculate_flight_distance(self, kml_file):
        print(f"KML FILE IS: {kml_file}")
        # Load KML
        tree = ET.parse(kml_file)
        root = tree.getroot()

        # Find <LineString> element
        line_string = root.find(".//{http://www.opengis.net/kml/2.2}LineString")

        # Extract <coordinates> from element
        coordinates_text = line_string.find(".//{http://www.opengis.net/kml/2.2}coordinates").text
        coordinates_list = [coord.split(',')[:2] for coord in coordinates_text.strip().split('\n')]

        # Calculate total distance
        total_distance = 0.0

        for i in range(len(coordinates_list) - 1):
            coord1 = coordinates_list[i]
            coord2 = coordinates_list[i + 1]
            distance = haversine((float(coord1[1]), float(coord1[0])),
                                (float(coord2[1]), float(coord2[0])))
            total_distance += distance

        # return total distance
        return coordinates_list, total_distance


    def generate_map(self, output_directory, kml_file): 
        MAP_output = os.path.join(output_directory, "map.png")
        
        coordinates_list, distance = self.calculate_flight_distance(kml_file)

        gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy(
            [float(coord[1]) for coord in coordinates_list],
            [float(coord[0]) for coord in coordinates_list]
        ))

        # Vyber priblíženú oblasť
        min_lat = min([float(coord[0]) for coord in coordinates_list])
        max_lat = max([float(coord[0]) for coord in coordinates_list])
        min_lon = min([float(coord[1]) for coord in coordinates_list])
        max_lon = max([float(coord[1]) for coord in coordinates_list])

        # Konfiguruj mapu s pozadím a zobraz priblíženú oblasť
        fig = plt.figure(figsize=(25, 10))
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_extent([min_lon, max_lon, min_lat, max_lat])

        # Pridaj background map (napr. "OpenStreetMap")
        ax.stock_img()
        ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

        # Zvýrazni trasu
        gdf.plot(ax=ax, markersize=10, color='blue', label='Trasa')

        # Ulož mapu
        plt.savefig(MAP_output, bbox_inches='tight', pad_inches=0.1, dpi = 100)

        #print("Celková preletená vzdialenosť: {:.2f} km".format(distance))
        return distance