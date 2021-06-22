"""
Created by Abhinav M Hari
Email: abhinav03m@gmail.com
PLEASE CHANGE THE KEY INTO YOUR ASSIGNED API KEY.
YOU CAN FIND AND GET INSTRUCTIONS TO GENERATE YOUR API KEY FROM https://openweathermap.org/
"""


import requests
import datetime

print("Weather Script")
print("Created by Abhinav M Hari\nEmail: abhinav03m@gmail.com")
print("Find the current weather of any city in the world. Just type in the city name below")
print("PRESS Q TO EXIT")
print("------------------------------------------------------------")


KEY = '924056f39b342eee5396ef1be85547c0'


while(True):
	loc = input("Enter the location: ")

	if (loc == 'Q' or loc == 'q' or loc == 'QUIT' or loc == 'quit'):
		print("Program Exited.....")
		break

	assert loc.isalpha(), "Enter only alphabets. Other Characters are not allowed"

	complete_url = 'https://api.openweathermap.org/data/2.5/weather?q={},uk&APPID=924056f39b342eee5396ef1be85547c0'.format(loc.lower())

	time = datetime.datetime.now()

	r = requests.get(complete_url) #Calling the api
	r = r.json() #Converting the results into json

	#Checking if the api returned an error
	cod = int(r['cod'])
	if cod in range(400, 600):
		msg = r['message']
		print(msg)
		print("Program Exited")
		print("------------------------------------------------------------")
		#writing the error in data.txt
		with open('data.txt', 'a') as f:
			f.write('location: {}, time: {}\n'.format(loc, time))
			f.write('message: {}\n'.format(msg))

		break
	
	#Collecting neccessary data from the api
	weather_des = r['weather'][0]['description']
	temp_in_C = (r['main']['temp'] - 273.15)
	temp_in_K = r['main']['temp']
	humidity = r['main']['humidity']
	
	print("Weather stats for {} || {}\n".format(loc.upper(), time))
	print("Weather: \t\t{}".format(weather_des))
	print("Temperature: \t\t{:.2f} deg C".format(temp_in_C))
	print("Temperature in Kelvin: \t{:.2f} deg K".format(temp_in_K))
	print("Humidity: \t\t{}".format(humidity))
	print("------------------------------------------------------------")

	#Writing the data to data.txt
	with open('data.txt', 'a') as f:
		f.writelines('location: {}, time: {}'.format(loc, time))
		f.write('description: {}\n'.format(weather_des))
		f.write('temp1: {:.2f}\n'.format(temp_in_C))
		f.write('temp2: {:.2f}\n'.format(temp_in_K))
		f.write('humidity: {:.2f}\n'.format(humidity))
		


