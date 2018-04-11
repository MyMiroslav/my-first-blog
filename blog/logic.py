# !/usr/bin/env python3
import json
from urllib.request import urlopen
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

def make_request(method, **params):
    url = 'https://api.telegra.ph/' + method
    params = {k: v if isinstance(v, str) else json.dumps(v) for k, v in params.items()}
    r = json.loads(urlopen(url + '?' + urlencode(params)).read())
    if not r['ok']:
        raise ValueError(str(r))
    return r['result']

def get_access_token(short_name):
    return make_request('createAccount', short_name=short_name)['access_token']

def create_page(**params):
    return make_request('createPage', **params)

def Publish(short_name,title_page,cont,image_url,source_of_page):
    token = get_access_token(short_name)
    title = title_page
    page = create_page(access_token=token, title=title, content=cont)
    print(page['url'])


def UploadImageTo(Path,name_file):
    with open(Path+name_file, 'rb') as f:
        print(requests.post('http://telegra.ph/upload', files={'file': ('file', f, 'image/jpeg')}  # image/gif, image/jpeg, image/jpg, image/png, video/mp4
            ).json()
        )

def GetPageContentOfTelegraph(url_article):
            ReturnDict = {}
            cont = requests.get(url_article).content
            soup = BeautifulSoup(cont)
            ReturnDict["h1"] = soup.findAll("h1")[0].string
            ReturnDict["img"] = soup.findAll("img")[0]['src']
            ReturnDict["p"] = soup.findAll("p")[0].string
            return (ReturnDict)