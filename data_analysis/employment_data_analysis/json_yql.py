import urllib2
import json


def find_place_to_eat(type_of_food, zip_code ):
    URL = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20local.search%20where%20zip%3D'"+str(zip_code)+"'%20and%20query%3D'"+type_of_food+"'&format=json&diagnostics=true&callback="
    result_yql = urllib2.urlopen(URL)

    url_to_json = json.load(result_yql)
    print url_to_json
    data = url_to_json['query']['results']

    for item in data['Result']:
        print "Address: ", item['Address']
        print "Name: ", item['Title']
        print "Distance: ", item['Distance']
        print "Ratings: ", item['Phone']
        print "Website: ", item['Url']

#find_place_to_eat('pizza', 32901)
#find_place_to_eat('shakes', 32901)
find_place_to_eat('bars', 32901)


