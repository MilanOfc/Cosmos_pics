import requests
import argparse
from downloader import download_pic


def get_spacex_pics_links(url, id='latest'):
    url_with_id = f'{url}/{id}'
    response = requests.get(url_with_id)
    response.raise_for_status()
    return response.json().get('links').get('flickr').get('original')


def fetch_spacex_launch(id):
    spacex_url, spacex_id = 'https://api.spacexdata.com/v5/launches', id
    if spacex_id is None:
        spacex_id = 'latest'
    folder = "./pictures"
    for link in get_spacex_pics_links(spacex_url, spacex_id):
        download_pic(link, folder)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--launch_id', help='launch identifier the pictures from which you want to upload')
    args = parser.parse_args()
    id = args.launch_id
    fetch_spacex_launch(id)
    print('All photos are downloaded')