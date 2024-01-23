import requests
import argparse
from downloader import download_pic


def download_spacex_pics_links(identificator='latest', folder='./pictures'):
    url_with_id = f'https://api.spacexdata.com/v5/launches/{identificator}'
    response = requests.get(url_with_id)
    response.raise_for_status()
    links = response.json().get('links').get('flickr').get('original')
    for link in links:
        download_pic(link, folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('downloading photos from the SpaceX launch\n')
    parser.add_argument('-id', '--launch_id', default='6243adcaaf52800c6e919254', type=str,
                        help='launch identifier the pictures from which you want to upload')
    args = parser.parse_args()
    identificator = args.launch_id
    download_spacex_pics_links(identificator)
    print('All photos are downloaded')
