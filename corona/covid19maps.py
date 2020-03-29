# -*- coding: utf-8 -*-
"""covid19maps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16rfUtltavUe0yzPnKcTTLtR1PH4bRgqQ
"""

#install the library google places
#!pip install python-google-places

#import the required library
from googleplaces import GooglePlaces, types, lang 
import requests 
import json

#use api keys for makking the rquest
#API_KEY='AIzaSyCQ-YokzoFHZQ-iTxnCjQ3Ipx2w3cfn3w4'
API_KEY = 'AIzaSyBXxEqeeifFE9Kzybugg25z_a7lRO9dE-8'
#initiate the api keys
google_places = GooglePlaces(API_KEY)

#call the function nearby for required location
query_result = google_places.nearby_search( lat_lng ={'lat': 28.4089, 'lng': 77.3178},radius = 5000,types =[types.TYPE_HOSPITAL,types.TYPE_ATM,types.TYPE_BAKERY,types.TYPE_BANK,types.TYPE_POLICE,types.TYPE_DEPARTMENT_STORE])

#if request is correct the print them
if query_result.has_attributions: 
    print (query_result.html_attributions)

#itrate the search result
#print the types of places and get detail of them
for place in query_result.places: 
    print(type(place)) 
    place.get_details() 
    print (place.name) 
    print("Latitude", place.geo_location['lat']) 
    print("Longitude", place.geo_location['lng']) 
    print()

