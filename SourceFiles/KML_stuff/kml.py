import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from haversine import haversine

import geopandas as gpd
import cartopy.crs as ccrs
import contextily as ctx

import requests

import os
import json

class KML_stuff():
    def __init__(self, result_path):
        self.result_path = result_path
        #print (result_path)
        




    ######################################
    ## Calculate total flight distance
    ######################################
    def calculate_flight_distance(self, kml_file):
        #print(f"KML FILE IS: {kml_file}")
        # Load KML
        tree = ET.parse(kml_file)
        root = tree.getroot()

        # Find <LineString> element
        line_string = root.find(".//{http://www.opengis.net/kml/2.2}LineString")

        # Extract <coordinates> from element
        coordinates_text = line_string.find(".//{http://www.opengis.net/kml/2.2}coordinates").text
        coordinates_list = [coord.split(',')[:2] for coord in coordinates_text.strip().split('\n')]


        #Get Longitude/Latitude 
        latitude, longitude = float(coordinates_list[0][1]), float(coordinates_list[0][0])
        #print("LAT:", latitude)
        #print("LONG:", longitude)

        # Získanie názvu lokality
        location = self.get_location_name(latitude, longitude)
        #print("Názov lokality:", locality)

        # Calculate total distance
        total_distance = 0.0

        for i in range(len(coordinates_list) - 1):
            coord1 = coordinates_list[i]
            coord2 = coordinates_list[i + 1]
            distance = haversine((float(coord1[1]), float(coord1[0])),
                                (float(coord2[1]), float(coord2[0])))
            total_distance += distance


        self.save_flight_info(total_distance, location)

        # return total distance
        return coordinates_list, total_distance
    
    def get_location_name(self, latitude, longitude):
        url = f"https://nominatim.openstreetmap.org/reverse.php?lat={latitude}&lon={longitude}&zoom=18&format=jsonv2"
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            data = response.json()
            locality = "{} {} {} {}".format(
                data.get('address', {},).get('city_district', ''),
                data.get('address', {},).get('hamlet', ''),
                data.get('address', {},).get('town', ''),
                data.get('address', {},).get('postcode', '')
            )
            return locality
        else:
            return "Názov lokality sa nenašiel"




    #################################
    ## Generate MAP
    #################################
    def generate_map(self, kml_file): 
        MAP_output = os.path.join(self.result_path, "map.png")
        
        coordinates_list, distance = self.calculate_flight_distance(kml_file)

        gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy(
            [float(coord[1]) for coord in coordinates_list],
            [float(coord[0]) for coord in coordinates_list]
        ))

        #Take Position for background
        min_lat = min([float(coord[0]) for coord in coordinates_list])
        max_lat = max([float(coord[0]) for coord in coordinates_list])
        min_lon = min([float(coord[1]) for coord in coordinates_list])
        max_lon = max([float(coord[1]) for coord in coordinates_list])

        #Setup background
        fig = plt.figure(figsize=(25, 10))
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_extent([min_lon, max_lon, min_lat, max_lat])

        #Set background from OpenStreetMap
        ax.stock_img()
        ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

        #Setup Track
        gdf.plot(ax=ax, markersize=10, color='blue', label='Trasa')

        #Save Map as image
        plt.savefig(MAP_output, bbox_inches='tight', pad_inches=0.1, dpi = 100)



        #print("Total Flight length {:.2f} km".format(distance))
        #return distance
    




    #################################
    ## Save Flight Info
    #################################
    def save_flight_info(self, flight_distance, locality):
        flight_info = {
            "flight_distance": flight_distance,
            "location": locality
        }
        json_file_path = os.path.join(self.result_path, "flight_info.json")
        with open(json_file_path, "w") as json_file:
            json.dump(flight_info, json_file)
        print(f"Flight information saved to {json_file_path}")