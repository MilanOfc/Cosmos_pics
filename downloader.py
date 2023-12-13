import requests
import os
from pathlib import Path
from urllib.parse import urlparse, unquote
from os.path import splitext, basename
from dotenv import load_dotenv

def download_pic(url, path):
    if url is None:
        return
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(exist_ok=True)
    parsed_url = urlparse(url)
    name = unquote(basename(parsed_url.path))
    with open(f"{path}/{name}", 'wb') as picture:
        picture.write(response.content)


def get_file_format(url):
    parsed_url = urlparse(url)
    name = unquote(basename(parsed_url.path))
    name_format_tuple = splitext(name)
    if name_format_tuple[1]:  # вопрос про функцию в целом и название переменной
        return name_format_tuple[1]
    return name_format_tuple[0]

load_dotenv()
nasa_token = os.environ['NASA_TOKEN']