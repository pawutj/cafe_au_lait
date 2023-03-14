#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8


import pandas as pd

data = pd.read_csv('test.csv',encoding="utf-8")

data = data.fillna("")

data['summary'] = data['who'] + ' "' + data['talk'] + '"'
data

p = []
temp_charector = ""
temp_charector_emotion=""

for i,c in data.iterrows():
    if(c['charector']):
        print("hide " +temp_charector_emotion +"\n")
        temp_charector = c['charector']
        temp_charector_emotion = temp_charector +"_"+c['emotion']
        print("show " +c['emotion'] +"\n" )
        
    else:
        if( c['emotion']):
            print("hide " +temp_charector_emotion +"\n")
            temp_charector_emotion = temp_charector + "_"+c['emotion']
            print("show " + temp_charector_emotion +"\n" )

    
    print(c['summary'].strip())

