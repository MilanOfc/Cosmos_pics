import requests
import argparse
from downloader import download_pic


def get_spacex_pics_links(identificator='latest'):
    url_with_id = f'https://api.spacexdata.com/v5/launches/{identificator}'
    response = requests.get(url_with_id)
    response.raise_for_status()
    return response.json().get('links').get('flickr').get('original')


def fetch_spacex_launch(identificator):
    spacex_url, spacex_id = 'https://api.spacexdata.com/v5/launches', identificator
    if spacex_id is None:
        spacex_id = 'latest'
    folder = "./pictures"
    for link in get_spacex_pics_links(spacex_id):
        download_pic(link, folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('downloading photos from the SpaceX launch\n')
    parser.add_argument('-id', '--launch_id', default='6243adcaaf52800c6e919254', type=str,
                        help='launch identifier the pictures from which you want to upload')
    args = parser.parse_args()
    identificator = args.launch_id
    fetch_spacex_launch(identificator)
    print('All photos are downloaded')
