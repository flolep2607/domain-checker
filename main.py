import requests
base_name="crunchyroll"
text_to_find="crunchyroll.com"
tdl=open("tdl.txt").readlines()
tdl=[i.lower().strip() for i in tdl]
print(len(tdl))

formater=f"http://{base_name}.%(ext)s"
i=1
for ext in tdl:
    try:
        rep=requests.get(formater%locals())
        if text_to_find in rep.text:
            print(formater%locals(),"________________")
    except:
        pass
    print(i,formater%locals(),"________________",end="\r")
    i+=1
