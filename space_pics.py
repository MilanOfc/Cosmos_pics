import requests
import datetime
import os
from pathlib import Path
from urllib.parse import urlparse, unquote
from os.path import splitext, basename
from dotenv import load_dotenv

SPACEX_IDS = ['6243adcaaf52800c6e919254', '61e048bbbe8d8b66799018d0']


def download_pic(url, path):
    if url is None:
        return
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(exist_ok=True)
    parsed_url = urlparse(url)
    name = unquote(basename(parsed_url.path))
    with open(f"{path}/{name}", 'wb') as picture:
        picture.write(response.content)


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


def get_file_format(url):
    parsed_url = urlparse(url)
    name = unquote(basename(parsed_url.path))
    name_format_tuple = splitext(name)
    if name_format_tuple[1]:  # вопрос про функцию в целом и название переменной
        return name_format_tuple[1]
    return name_format_tuple[0]


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


def get_epic_links(api_key, date=None):
    api_url = f'https://api.nasa.gov/EPIC/api/natural'
    if date:
        api_url = f'{api_url}/date/{date}'
    image_url_base = 'https://epic.gsfc.nasa.gov'
    params = {'api_key': api_key}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    links = []
    for image_metadata in response.json():
        image_name = image_metadata.get('image')
        image_datetime = datetime.datetime.fromisoformat(image_metadata.get('date'))
        image_date = image_datetime.strftime('%Y/%m/%d')
        image_url = f'{image_url_base}/archive/natural/{image_date}/png/{image_name}.png'
        links.append(image_url)
    return links


def download_epic_pics(api_key, date=None):
    for epic_link in get_epic_links(api_key, date=date):
        download_pic(epic_link, './epic')


if __name__ == "__main__":

    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    for id in SPACEX_IDS:
        fetch_spacex_launch(id)
    download_apod_pics(30, nasa_token)
    download_epic_pics(nasa_token, date='2023-01-10')
