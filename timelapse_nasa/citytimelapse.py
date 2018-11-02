import requests
import json
from PIL import Image
from io import BytesIO
import os
import glob
import moviepy.editor as mpy

api_key = "DEMO_KEY"

def nasagetimages(lat, lon, dim: 0.025, date, api_key, image_name):
	"""
	This function calls the NASA api and requests for a satellite image of the coordinates
	given, it will then download this image into a directory called "img" if this directory
	is not already created there will be an error. 
	:param: 
		lat -> float: the lattitude of the city you want to find images for
		lon -> float: the longitude of the city you want to find images for
		dim -> float: the dimensions of the image, by default it is a square
		api_key -> string: the api key that you will need to get from 
							https://api.nasa.gov/api.html#earth
		image_name -> str

	:return: 0 if the status code is not 200, and returns None if an image has been
	written to the img/ directory.
	"""
    payload = {
        "lat": lat,
        "lon": lon,
        "dim": dim,
        "date": date,
        "api_key":api_key
    }
    url = "https://api.nasa.gov/planetary/earth/imagery/"
    r = requests.get(url, params=payload)
    if r.status_code == 200:
       image_url = r.json()["url"]
       r = requests.get(image_url)
       i = Image.open(BytesIO(r.content))
       i.save(os.getcwd() + "/img/" + image_name + ".png", quality=100)
    else:
        print("{}: your request is not ok...".format(r.status_code))
        return 0


for month in range(1, 13):  # need to get images for 1 year
   day = "2016-{0:02d}-01".format(month)  # format file name so that it is easy to read

   nasagetimages(lat=40.730610, lon=-73.935242,  \
       dim=0.025, date=day, api_key=api_key, image_name=day)  # lat and lon of NYC

gif_name = 'timelapse'  
os.chdir(os.getcwd() + "/img")  # change directory of the img/
file_list = glob.glob(r'*.png')
list.sort(file_list, key=lambda x: int(x.split('-')[1]))  # sort files by their month
fps = 6

clip = mpy.ImageSequenceClip(file_list, fps=fps)  # create a sequence of images
clip.write_gif('{}.gif'.format(gif_name), fps=fps)  # writing that sequence to a gif

