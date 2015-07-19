#!/usr/bin/env python2
#encode=utf8
import gevent.monkey
gevent.monkey.patch_all()

from bottle import route,run,template,Bottle,request
import json
import sqlite3
app=Bottle(__name__)
db=sqlite3.connect('test.db')

@app.route('/')
def index():
    cur=db.execute('select * from cpu_t')
    rows=cur.fetchall()
    print(rows)
    li=[]
    for i in rows:
        for j in i:
            li.append(j)
    print(li)
    return "" #template("first",rows=rows) 

@app.post('/post')
def revdata():
    temp=request.body.read()
    temp=temp.replace("'",'"')
    t=json.loads(temp)
    if t.get('temp'):
        print (t['temp'])
        cur=db.cursor()
        cur.execute("insert into cpu_t (cpu_t) values ({0})".format(str(100.0)))
#        cur.commit()
        db.commit()
    return "Post OK"

app.run(host='0.0.0.0',server="gevent",port=8000,reloader=True,debug=True)

