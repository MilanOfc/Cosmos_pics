import requests
import downloader
import argparse
import os
from dotenv import load_dotenv


def get_apod_pics_links(count, api_key):
    nasa_url = 'https://api.nasa.gov/planetary/apod/'
    params = {'api_key': api_key, 'count': count}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    links = [picture_metadata.get('hdurl') for picture_metadata in response.json() if picture_metadata.get('hdurl')]
    return links


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser('downloading "A Picture Of the Day" from the NASA website\n')
    parser.add_argument('-c', '--count', default=10, type=int,
                        help='amount of pictures you want to download, 10 by default')
    args = parser.parse_args()
    count = args.count
    for link in get_apod_pics_links(count, nasa_token):
        downloader.download_pic(link, './pictures')
    print('All photos are downloaded')
