import requests
import urllib2
import pprint
from geopy import geocoders
import json
g = geocoders.GoogleV3()
pp = pprint.PrettyPrinter(indent=4)
address = raw_input('Enter the address: ')
place, (lat, lng) = g.geocode(address)
print "%s: %.5f, %.5f" % (place, lat, lng)
url = "https://maps.googleapis.com/maps/api/place/search/json?location=%s,%s&radius=10&sensor=false&key=AIzaSyBYRMJfTpRcV-KEPuyzidZDXhvptBse6us" %(lat,lng)
'''Request'''
response = requests.get(url)
data = json.loads(response.text)
for test in data['results']:
        list=test['name']
        print(list)
        urll = "http://api.nytimes.com/svc/search/v1/article?query=bob&api-key=f        7eeff97d545f21eef9fe0ecdf99b655:17:68190350"
        response1 = requests.get(urll)
        print(response1)
        data1 = json.loads(response1.text)
pp.pprint(data1)
