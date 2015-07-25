fi=open('/proc/meminfo')
li=[]
for i in fi.readlines():
    j=i.split()
    j.remove('kB')
    li.append(j)

dic=dict(li)
memuse=100*\
        (float(dic['MemTotal:'])-float(dic['MemFree:'])\
        -float(dic['Buffers:'])-float(dic['Cached:'])\
        -float(dic['Slab:']))\
        /float(dic['MemTotal:'])
print(memuse)

