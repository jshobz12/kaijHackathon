import os

TAGS = ['healthylivingtlvchallenge', ]


ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

DB_PARAMS = dict(host='localhost',
                     user='arielhuntley',
                     db='instadb',
                     charset='utf8',)

DB_PARAMS = dict(**DB_PARAMS, user='root', password='!Newyork17')