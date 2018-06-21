from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql
from consts import *

connection = pymysql.connect(**DB_PARAMS,
                             cursorclass=pymysql.cursors.DictCursor)


@get("/scores")
def category() :
    try :
        with connection.cursor() as cursor:
            sql = """select username, handle, cast(sum(e.points) as SIGNED) as totalpts
                    from profileInformation p
                    join entries e on e.userid = p.id
                    group by p.id
                    order by totalpts desc
                    limit 20;"""
            cursor.execute(sql)
            get_score = cursor.fetchall()
            result = {
                "STATUS" : "SUCCESS",
                "MSG" : "success",
                "scores" : get_score,
                "CODE" : 200
            }
    except :
        result={
            "STATUS" : "ERROR",
            "MSG" : "internal error",
            "CODE" : 500
        }
    return json.dumps(result)


@get("/")
def index():
    return template("leaderboard.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')

@get('/plugins/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='plugins')

@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')

@get('/plugins/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='plugins')

@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='0.0.0.0', port=7000)
