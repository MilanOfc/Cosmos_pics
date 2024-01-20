import os
import argparse
from dotenv import load_dotenv
from fetch_apod_images import download_apod_pics
from fetch_epic_images import download_epic_pics
from fetch_spacex_images import fetch_spacex_launch

SPACEX_IDS = ['6243adcaaf52800c6e919254', '61e048bbbe8d8b66799018d0']

if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser('downloading photos from the SpaceX launch, NASA APOD and NASA EPIC\n')
    args = parser.parse_args()
    for flight_id in SPACEX_IDS:
        fetch_spacex_launch(flight_id)
    download_apod_pics(nasa_token, count=30)
    download_epic_pics(nasa_token, date='2023-01-10')
    print('All photos are downloaded')
