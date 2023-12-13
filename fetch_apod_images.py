import requests
from helper import download_pic


def get_apod_pics_links(count, api_key):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': count}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    links = []
    for picture_json in response.json():
        links.append(picture_json.get('hdurl'))
    return links


def download_apod_pics(count, api_key):
    for link in get_apod_pics_links(count, api_key):
        download_pic(link, './apod')
