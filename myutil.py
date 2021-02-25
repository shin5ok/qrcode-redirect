
import qrcode
import os
import sys
import requests
import uuid

APIURL="https://api-ssl.bitly.com/v3/shorten"
APIKEY=os.environ.get('BITLY_APIKEY')

def gen(url):
    img = qrcode.make(url)
    imgpath = f"static/{str(uuid.uuid4())}.png"
    img.save(imgpath)
    genurl = get_bitly_shortenurl(url)
    return {'orgurl':url, 'newurl':genurl,'imgpath':imgpath}

def get_bitly_shortenurl(url):
    params=dict(
        access_token=APIKEY,
        longurl=url
    )
    response = requests.get(APIURL, params)
    return response.json()['data']['url']

