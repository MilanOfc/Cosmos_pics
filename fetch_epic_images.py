import requests
import datetime
import argparse
import downloader
import os
from dotenv import load_dotenv


def get_epic_links(api_key, date=None):
    api_url = f'https://api.nasa.gov/EPIC/api/natural'
    if date:
        api_url = f'{api_url}/date/{date}'
    image_base_url = 'https://epic.gsfc.nasa.gov'
    params = {'api_key': api_key}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    links = []
    for image_metadata in response.json():
        image_name = image_metadata.get('image')
        image_datetime = datetime.datetime.fromisoformat(image_metadata.get('date'))
        image_date = image_datetime.strftime('%Y/%m/%d')
        image_url = f'{image_base_url}/archive/natural/{image_date}/png/{image_name}.png'
        links.append(image_url)
    return links


def valid_date(dt_str):
    try:
        return datetime.datetime.strptime(dt_str, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a valid date: {dt_str!r}")


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser('downloading "Earth Polychromatic Imaging Camera" from the NASA website\n')
    parser.add_argument('-d', '--date', type=valid_date, default=None,
                        help='the date from which you want to upload the images. Format YYYY-MM-DD')
    args = parser.parse_args()
    date = args.date
    for epic_link in get_epic_links(nasa_token, date=date):
        downloader.download_pic(epic_link, './pictures')
    print('All photos are downloaded')
