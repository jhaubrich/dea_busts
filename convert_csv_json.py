import csv
import json
from geopy import geocoders


def dict_from_csv(filename):
    o = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            addr, latLng = geocode(row[0])
            o.append({'latLng':latLng, 'address':addr, 'date':row[1]})
    return o

def geocode(addr):
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(addr)
    return place, (lat, lng)


def main():
    busts = dict_from_csv('okc_dea_busts.csv')
    with open('okc_dea_busts.json', 'w') as f:
        f.write(json.dumps(busts))
if __name__ == '__main__':
    main()