import googlemaps
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

gmaps = googlemaps.Client(key=config['keys']['google_key'])

def getDistance(start, dest):
    distance = gmaps.distance_matrix(origins=start, destinations=dest)
    if distance['status'] == "OK":
        return distance['rows'][0]['elements'][0]['distance']['text']
    else:
        print("Failed to get distance")