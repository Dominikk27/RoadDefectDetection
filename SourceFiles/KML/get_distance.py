import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from haversine import haversine
import geopandas as gpd
import cartopy.crs as ccrs
import contextily as ctx

#########################################
##   VÝPOČET PRELETENEJ VZDIAELNOSTI   ##
#########################################

def calculate_flight_distance(kml_file):
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
    return total_distance

