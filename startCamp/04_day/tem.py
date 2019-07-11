import requests
import random

response = requests.get('http://artii.herokuapp.com/fonts_list').text
font = random.choice(tuple(map(str,response.split( ))))