# encoding: utf-8
import json
zhash={"xiaoming":{"class":"1","score":"85"},"lucy":{"class":"2","score":"62"},"lili":{"class":"1","score":"90"},"ladygaga":{"class":"2","score":"74"},"爱新觉罗":{"class":"1","score":"68"},"厄页木东日天":{"class":"2","score":"78"}}

a=0
b=0
i=0
c=0
d=0
e=0
f=0
suma =0
sumb =0

listc=[]
listd=[]
liste=[]
for k in zhash:
    if zhash[k]["class"]=="1":
        i=i+1
        a =a+int(zhash[k]["score"])
        #print a
    if zhash[k]["class"]=="2":
        b =b+int(zhash[k]["score"])
        #print b
suma=(a/i)
sumb=(b/i)


for k in zhash:
    if zhash[k]["score"]>="85":
        f=k
        liste.append(f)
    if zhash[k]["score"]<="85":
        c=(k)
        if zhash[k]["score"]>="70":
            d=k
            listd.append(d)
            #print d
    if zhash[k]["score"]<="60":
        e=k
        listc.append(e)

lista={"一班":suma,"二班":sumb}
dictd={"A":liste,"B":listd,"C":listc}
all={"result2":lista,"result1":dictd}
print json.dumps(all,encoding='UTF-8',ensure_ascii=False)

