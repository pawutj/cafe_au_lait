#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

def printHide(c):
    if(c == ""):
        return
    print("hide " + c +"\n")
    

import pandas as pd

data = pd.read_csv('test.csv',encoding="utf-8")

data = data.fillna("")

data['summary'] = data['who'] + ' "' + data['talk'] + '"'
data

p = []
temp_charector = ""
temp_charector_emotion=""
temp_screen = ""
for i,c in data.iterrows():

    if(c['bg']):
        print("show "+c['bg'] + "\n")
        printHide(temp_screen)
        temp_screen = c['bg']

    if(c['bgm'] and c['bgm'] != 'stop music'):
        print('play music "audio/bgm/'+c['bgm']+'.mp3" volume 0.5')
    
    if(c['bgm'] == 'stop music'):
        print("stop music \n")

    if(c['charector']):
        if(c['charector'] == 'hide'):
            printHide(temp_charector_emotion)
            temp_charector = ""
        else :
            printHide(temp_charector_emotion)
            temp_charector = c['charector']
            temp_charector_emotion = temp_charector +"_"+c['emotion']
            print("show " +temp_charector_emotion +"\n" )
        
    else:
        if( c['emotion']):
            printHide(temp_charector_emotion)
            temp_charector_emotion = temp_charector + "_"+c['emotion']
            print("show " + temp_charector_emotion +"\n" )

    
    print(c['summary'].strip())

