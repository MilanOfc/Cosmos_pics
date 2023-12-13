import requests
import datetime
import argparse
import downloader
import sys


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
        downloader.download_pic(epic_link, './pictures')


def datetime_valid(dt_str):
    try:
        datetime.datetime.fromisoformat(dt_str)
    except ValueError:
        return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', help='the date from which you want to upload the images. '
                                             'Format YYYY-MM-DD')
    args = parser.parse_args()
    date = args.date
    if datetime_valid(date):
        print('Wrong date format, try --help for more information')
        sys.exit()
    download_epic_pics(downloader.nasa_token, date)
