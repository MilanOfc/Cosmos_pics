import requests
import datetime
from helper import download_pic


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
