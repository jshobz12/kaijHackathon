from datetime import datetime
import requests
import pymysql

from .consts import *


def insert_posts(results):
    with pymysql.connect(DB_ADDRESS, DB_USER, database=DB) as con:
        for post in results:
            userid_query = f'SELECT id FROM profileInformation WHERE handle = {post["user"]["username"]};'
            con.execute(userid_query)
            userid = next(con.fetchone(), None)
            if userid is None:  # skip people not in our system
                continue
            datetime = datetime.fromtimestamp(int(post['created_time'])) \
                .strftime('%Y-%m-%d %H:%M:%S')
            insert_query = f"""INSERT INTO entries (userId,dateAndTime,insta,instaPostId,points)
                VALUES({userid}, {datetime}, {post['link']}, {post[id]}, NULL"""
            con.execute(insert_query)
        con.commit()


def get_page_tagged(tags):
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
            if is_id_in_db(postid):  # everything past here is old news
                break
            if postid in seen_posts:  # was seen with another tag
                continue
            seen_posts.add(postid)
            results.append(post)
    insert_posts(results)


def is_id_in_db(postid):
    query = f'SELECT id FROM entries WHERE postId = {postid};'
    with pymysql.connect(DB_ADDRESS, DB_USER, database=DB) as con:
        con.execute(query)
        return len(con.fetchall())


def _log_request_error(request):
    try:
        jsonerror = request.json()
    except ValueError:
        jsonerror = ''
    print("error fetching tags: "
          f"{request.status_code} {request.reason}: {jsonerror}")
