import os
import downloader
from dotenv import load_dotenv
from fetch_apod_images import get_apod_pics_links
from fetch_epic_images import get_epic_links
from fetch_spacex_images import download_spacex_pics_links

SPACEX_IDS = ['6243adcaaf52800c6e919254', '61e048bbbe8d8b66799018d0']

if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    folder = './pictures'
    download_spacex_pics_links()
    for link in get_apod_pics_links(api_key=nasa_token, count=10):
        downloader.download_pic(link, folder)
    for epic_link in get_epic_links(nasa_token):
        downloader.download_pic(epic_link, folder)
    print('All photos are downloaded')
