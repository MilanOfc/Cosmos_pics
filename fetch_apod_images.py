import sys

import requests
import downloader
import argparse


def get_apod_pics_links(count, api_key):
    nasa_url = 'https://api.nasa.gov/planetary/apod/'
    params = {'api_key': api_key, 'count': count}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    links = []
    for picture_json in response.json():
        links.append(picture_json.get('hdurl'))
    return links


def download_apod_pics(api_key, count=10):
    for link in get_apod_pics_links(count, api_key):
        downloader.download_pic(link, './pictures')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='amount of pictures you want to download, 10 by default')
    args = parser.parse_args()
    count = args.count
    if count:
        try:
            count = int(count)
        except ValueError:
            print('Wrong format, you have to use integer number')
            sys.exit()
        download_apod_pics(downloader.nasa_token, count)
    else:
        download_apod_pics(downloader.nasa_token)
    print('All photos are downloaded')