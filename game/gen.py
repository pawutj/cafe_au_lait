from os import listdir
from os.path import isfile, join
mypath = "./images/Sprite/Eimi01"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

for c in onlyfiles:
    print("image" + " " + "Eimi_"+c.split('.')[0])
    print("    "+"zoom 0.75")
    print('    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/'+c+"\"")