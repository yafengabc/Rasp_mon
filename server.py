#!/usr/bin/env python2
#encode=utf8
import gevent.monkey
gevent.monkey.patch_all()

from bottle import route,run,template,Bottle
import sqlite3
app=Bottle(__name__)
db=sqlite3.connect('test.db')

@app.route('/')
def ind():
    return 'OK'
def index():
    cur=db.execute('select * from pimark')
    rows=cur.fetchall()
    li=[]
    for i in rows:
        for j in i:
            li.append(j)
        
    return  template("first",rows=rows) 

@app.post('/post')
def revdata():

    
    return "Post OK"

app.run(host='0.0.0.0',server="gevent",port=8000,reloader=True,debug=True)

