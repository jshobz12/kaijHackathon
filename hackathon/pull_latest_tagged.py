from datetime import datetime
import requests
import pymysql

from consts import *

assert ACCESS_TOKEN

def insert_posts(results):
    con = pymysql.connect(**DB_PARAMS)
    with con.cursor() as cur:
        for post in results:
            userid_query = 'SELECT id FROM profileInformation WHERE handle = ' \
                           f'"{post["user"]["username"]}";'
            cur.execute(userid_query)
            userid = cur.fetchone()
            if userid is None:  # skip people not in our system
                continue
            userid = userid[0]
            dt = datetime.fromtimestamp(int(post['created_time'])) \
                .strftime('%Y-%m-%d %H:%M:%S')
            insert_query = f"""INSERT INTO entries 
                (userId,dateAndTime,postURL,imgURL,instaPostId,points)
                VALUES({userid}, "{dt}", "{post['link']}", 
                "{post["images"]["standard_resolution"]["url"]}", 
                "{post["id"]}", NULL)"""
            cur.execute(insert_query)
    con.commit()


def get_page_tagged(tags, token):
    """Searches for new posts with any from the list of tags"""
    results = []
    seen_posts = set()
    for tagname in tags:
        r = requests.get('https://api.instagram.com/v1/tags/'
                         f'{tagname}/media/recent?access_token={token}')
        if not r.ok:
            _log_request_error(r)
            continue
        posts = r.json()['data']
        for post in posts:
            postid = post['id']
            if is_id_in_db(postid):  # everything past this point is already in db
                break
            if postid in seen_posts:  # was seen with another tag
                continue
            seen_posts.add(postid)
            results.append(post)
    insert_posts(results)


def is_id_in_db(postid):
    query = f'SELECT id FROM entries WHERE instaPostId = "{postid}";'
    with pymysql.connect(**DB_PARAMS) as con:
        con.execute(query)
        return len(con.fetchall())


def _log_request_error(request):
    try:
        jsonerror = request.json()
    except ValueError:
        jsonerror = ''
    print("error fetching tags: "
          f"{request.status_code} {request.reason}: {jsonerror}")


if __name__ == '__main__':
    get_page_tagged(TAGS, ACCESS_TOKEN)