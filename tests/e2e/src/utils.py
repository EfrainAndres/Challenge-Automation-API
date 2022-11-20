import requests

baseUrl = "http://api.duckduckgo.com"
vqd = "3-28626076117804744091260013398931412268-315264775669019803022439510800524395403"

def duckDuckGoUrl(path: str) -> str:
    return baseUrl