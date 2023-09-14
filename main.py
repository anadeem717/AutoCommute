'''
Areesh Nadeem
Auto Commmute Planner Project
    - Calculates distance and duration of commute from home to school. 
    - Can be automated by a task scheduler on a computer. 
'''

import googlemaps
from twilio.rest import Client

# twilio account SID and Auth Token
twilioSID = 'XXXXXXXXXXXXXXXXXXXXX'
twilioAuthToken = 'XXXXXXXXXXXXXXXXXXXXXX'

# the twilio phone number which will send the msg. 
twilioPhone = '+12223334567'

# opens the file containing the maps API, reads it, then closes the file. 
# API key is read from a separate file to ensure security. 
API = open("GoogleMapsAPI.txt", "r")
APIKey = API.read().strip() 
API.close() 

# phone number that the msg will be sent to. 
userPhone = '1112223456'

# start and end destination. 
home = '1234 YourStreet, City, State'
school = '1234 Your School, City, State'

# passes through the API key to google client.
gmaps = googlemaps.Client(key=APIKey)  

mode = 'driving' # user's mode of driving, in this case it is driving. 

# gets directions from maps API and calculates the route. 
directions = gmaps.directions(home, school, mode=mode)

# if directions are successfully obtained:
if directions:
    route = directions[0]['legs'][0] 

    # distance in miles from start to end destination.
    distance = route['distance']['text']

    # how long it will take for route in hrs/min.
    duration = route['duration']['text']

    # message to be sent from twilio phone number. 
    msg = f"\nDistance from home to school is {distance} and will take approximately {duration}."

    # twilio client so program can execute the message from twilio phone number. 
    twilio_client = Client(twilioSID, twilioAuthToken)

    # sends the text message to user's phone number. 
    twilio_client.messages.create(
        body=msg,
        from_=twilioPhone,
        to=userPhone
    )
    
    print("Message sent successfully.")
else:
    print("API fail or no routes avaliable.")
