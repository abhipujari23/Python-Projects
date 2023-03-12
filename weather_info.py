import requests

def weatherAPIinfo(area):
    """
     Get information about the weather in provided area
     
     @param area - (str) area to search the weather for. e. g. Pune
     
     @return info - (dict) that contains the weather information
    """
    #inorder to work you need API key from weatherAPI.com
    #visit https://www.weatherapi.com/signup.aspx to get your API key and replace YOUR_WEATHER_API_KEY with your key
    api_key = 'YOUR_WEATHER_API_KEY'

    url = 'https://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=yes'.format(api_key, area)

    weather_update = requests.get(url)

    info = weather_update.json()
    return info

def wdirection(dir):
    """
     Convert direction code to Direction fullforms. 
     Used to convert a wind direction from E to East
     
     @param dir - Direction to convert e.g. N
     
     @return Direction full form as a string e.g. North
    """
    wind = {
        'E':"East",
        'W':"West",
        'N':"North",
        'S':"South",
        'NE':"North East",
        'NW':"North West",
        'SE':"South East",
        'SW':"South West"
            }
    return wind[dir]

'''
#Sorting information
location_name = info['location']['name']
location_region = info['location']['region']
temperature_celcius = info['current']['temp_c']
temperature_farenheit = info['current']['temp_f']
temperature_feelslike_celcius = info['current']['feelslike_c']
'''