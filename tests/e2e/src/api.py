from tests.e2e.src.utils import baseUrl, vqd

import requests

def _url():
    return baseUrl

def getDogsImages(search: str):
    headers = {"Content-type": "application/json", "referer": "https://duckduckgo.com/"}
    params = {"q": search, "format": "json", "vqd":vqd}
    response = requests.get(_url() + "/i.js", params=params, headers=headers)
    return response

def getDogeCoinLinks(search: str):
    headers = {"Content-type": "application/json"}
    params = {"q": search, "format": "json", "vqd":vqd}
    response = requests.get(_url(), params=params, headers=headers)
    return response