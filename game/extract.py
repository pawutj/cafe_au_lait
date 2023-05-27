#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

import re
with open("badend1.rpy", encoding="utf-8") as file:
    content = file.read()
    lines  = content.split("\n")
    count = 0
    for i in lines:
        t= i
        if(len(i) <=1):
            continue
        # if(i.split(" ")[1]== "ei"):
        #     print(i)
        if("hide" in i):
            continue
        if("play" in i):
            continue
        if("show" in i):
            continue
        if("stop" in i):
            continue
        if("scene" in i):
            continue
        if("with" in i):
            pattern = r'\s+with dissolve$'
            t = re.sub(pattern, '', i)
        if("ei" in t):
            x = "{0:0=2d}".format(count)
            print(t + " bad1_1_"+x+".mp3")
            count = count+1
        else:
            print(t)
            