import re
with open("script1_4.rpy", encoding="utf-8") as file:
    content = file.read()
    lines  = content.split("\n")
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
        if("with" in i):
            pattern = r'\s+with dissolve$'
            t = re.sub(pattern, '', i)
        print(t)
            