import requests
from tqdm import tqdm
import re

def download_file_from_google_drive(id,destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
 
    save_response_content(response, destination)
    
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None
def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in tqdm(response.iter_content(CHUNK_SIZE),desc=destination,ascii='#'):
            if chunk:
                f.write(chunk)

print("Downloading Super-Slomo Model(358Mb)")
download_file_from_google_drive('196YojhefdbwynJ1w1YWbHR47yBtd5Nju', 'checkpoint/model-200000.data-00000-of-00001')
download_file_from_google_drive('1fyhSwY_vV77sH4Ymuyq0nIb7JrFEncen', 'checkpoint/model-200000.meta')
download_file_from_google_drive('1jDvXtcu5bvO5GxpKprjdphmYsDtoSACt', 'checkpoint/model-200000.index')
