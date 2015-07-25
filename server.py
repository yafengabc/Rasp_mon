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
    cur=db.execute('select * from cpu_t order by SysTime desc LIMIT 50')
    rows=cur.fetchall()
#    print(rows)
    lbl=[]
    lbl2=[]
    dat=[]
    j=0
    for i in rows:
        lbl.append(i[0].split()[1])
        dat.append(i[1])

    lbl.reverse()
    dat.reverse()

    label=str(lbl).replace("'",'"').replace('u"','"')

    data=str(dat).replace("'",'"').replace('u"','"')
    return template("cpu_t2",label=label,data=data) 

@app.post('/post')
def revdata():
    temp=request.body.read()
    temp=temp.replace("'",'"')
    t=json.loads(temp)

    if t.get('temp'):
        print (t['temp'])
        cur=db.cursor()
        cur.execute("insert into cpu_t  values ('{0}',{1})".format(t['time'],t['temp']))
#        cur.commit()
        db.commit()
    return "Post OK"

#app.run(host='0.0.0.0',server="paste",port=8000,reloader=True,debug=True)
#app.run(host='0.0.0.0',server="gevent",port=8000,reloader=True,debug=True)
app.run(host='0.0.0.0',server="gevent",port=8000)

