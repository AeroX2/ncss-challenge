#!/usr/bin/python3
import csv
from math import acos,cos,sin,radians

def sphere_distance(la1, lo1, la2, lo2):
	return acos((sin(la1) * sin(la2)) + (cos(la1) * cos(la2) * cos(abs(lo1 - lo2)))) * 6371

latitude = input("Enter your latitiude: ").split(" ")
longitude = input("Enter your longitude: ").split(" ")
hour = int(input("Enter the hour: "))

toilet_file = open("public-toilets.csv")
toilets = csv.DictReader(toilet_file)
avaliable_toilets = []
for line in toilets:
	if (line["IsOpen"] == "DaylightHours" and hour >= 6 and hour <= 20) or (line["IsOpen"] == "AllHours"):
		avaliable_toilets.append(line)

decimal_latitude = radians((float(latitude[0]) + (float(latitude[1]) / 60) + (float(latitude[2]) / 3600)) * (-1 if latitude[3] == "S" else 1))
decimal_longitude = radians((float(longitude[0]) + (float(longitude[1]) / 60) + (float(longitude[2]) / 3600)) * (-1 if longitude[3] == "W" else 1))

toilet_distances = []
for toilet in avaliable_toilets:
	toilet_latitude = radians(float(toilet["Latitude"]))
	toilet_longitude = radians(float(toilet["Longitude"]))
	distance = sphere_distance(decimal_latitude, decimal_longitude, toilet_latitude, toilet_longitude)
	toilet_distances.append([distance, ", ".join([toilet["Name"],toilet["Town"],toilet["State"]])])

min_distance = toilet_distances[0][0]
current_toilet = toilet_distances[0][1]
for toilet in toilet_distances:
	if toilet[0] < min_distance:
		min_distance = toilet[0]
		current_toilet = toilet[1]

print("Closest toilet: " + current_toilet)
print("Distance: " + str(round(min_distance)) + "km")
