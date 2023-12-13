import requests
from helper import download_pic


def get_spacex_pics_links(url, id='latest'):
    url_with_id = f'{url}/{id}'
    response = requests.get(url_with_id)
    response.raise_for_status()
    return response.json().get('links').get('flickr').get('original')


def fetch_spacex_launch(id='latest'):
    spacex_url, spacex_id = 'https://api.spacexdata.com/v5/launches', id
    folder = "./spaceX"
    for link in get_spacex_pics_links(spacex_url, spacex_id):
        download_pic(link, folder)
