import requests
import urllib2
import urllib
import pprint
from geopy import geocoders
import json
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    g = geocoders.GoogleV3()
    pp = pprint.PrettyPrinter(indent=4)
    #address = raw_input('Enter the address: ')
    place, (lat, lng) = g.geocode(address)
    print "%s: %.5f, %.5f" % (place, lat, lng)
    url = "https://maps.googleapis.com/maps/api/place/search/json?location=%s,%s&radius=10&sensor=false&key=AIzaSyBYRMJfTpRcV-KEPuyzidZDXhvptBse6us" %(lat,lng)
    #Request
    response = requests.get(url)
    data = json.loads(response.text)
    file = open('alchemy.txt', 'w+')
    for test in data['results']:
            list=test['name']
            list = "%22" + str(list) +"%22"
            urll = "http://api.nytimes.com/svc/search/v1/article?format=json&query=%s&api-key=f7eeff97d545f21eef9fe0ecdf99b655:17:68190350"%         (list)
            response1 = requests.get(urll)
            data1 = json.loads(response1.text)
            for urtest in data1['results']:

                    listurl=str(urtest['url'])
                    response = urllib.urlopen(listurl)
                    for urlline in response.read():
                         file.write(urlline)
if __name__ == "__main__":
    app.run()
