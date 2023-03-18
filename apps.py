import requests
from CONSTS import URL
# from PIL import Image


def get_cat() -> None:
    response = requests.get(URL)
    # im = Image.open(requests.get(response.json()[0]['url'], stream=True).raw)
    # im.save('image.jpg')
    return response.json()[0]['url']