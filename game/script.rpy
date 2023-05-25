# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#navigation
define n = Character(None, who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
#eimi
define ei = Character("{font=SukhumvitSet-Medium.ttf}เอมิ",color="#F0F8FF", image ="eimi", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
#takagi
define tk = Character("{font=SukhumvitSet-Medium.ttf}ทาคากิ",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
#student a
define a = Character("{font=SukhumvitSet-Medium.ttf}นักเรียน A",color="#F0F8FF",image ="enjou1" ,  who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
#student ???
define e0 = Character("{font=SukhumvitSet-Medium.ttf}???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# The game starts here.
define en = Character("{font=SukhumvitSet-Medium.ttf}เอนโจว",color="#F0F8FF", image = "enjou2",who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
transform crops:
    crop(650,-800,1920,2900)

# image side eimi:
#     zoom 0.6
#     crops
#     im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02.png")


image side enjou1:
    zoom 1.3
    im.Scale("Sprite/Other/Enjou01.png",300,300)
    yoffset 50

image side enjou2:
    zoom 1.3
    im.Scale("Sprite/Other/Enjou02.png",300,300)
    yoffset 50



image eimi_0: 
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi01/Eimi_Body.png" ,(0,1525),"Sprite/Eimi01/Eimi_0.0.png")

image eimi_2:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02.png")


image eimi_02_wakaranai:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body.png" ,(30,1525),"Sprite/Eimi01/Eimi_Wakaranai.png")

image eimi_02_0_0:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body.png"  ,(30,1525),"Sprite/Eimi01/Eimi_0_0.png")


image eimi_02_scared:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body.png" ,(30,1525),"Sprite/Eimi01/Eimi02_scared.png")    

image eimi_02_panic:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body.png" ,(30,1525),"Sprite/Eimi01/Eimi02_panic.png")    

image eimi_02_pout:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body.png" ,(30,1525),"Sprite/Eimi01/Eimi02_pout.png")

image eimi_02_shock:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body.png" ,(30,1525),"Sprite/Eimi01/Eimi02_shock.png")
    
image eimi_02_onegai:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body.png" ,(30,1525),"Sprite/Eimi01/Eimi02_onegai.png")

image eimi_02_shy_onegai:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body_shy.png" ,(30,1525),"Sprite/Eimi02/Eimi02_onegai.png")

image eimi_02_shy_stupid:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body_shy.png" ,(30,1525),"Sprite/Eimi02/Eimi02_stupid.png")
    
image eimi_02_shy_tired:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body_shy.png" ,(30,1525),"Sprite/Eimi02/Eimi02_tired.png")
    
image eimi_02_shy_meme02:
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi02/Eimi02_body_shy.png" ,(30,1525),"Sprite/Eimi02/Eimi02_meme02.png")


image eimi_30: 
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi01/Eimi_Body.png" ,(0,1525),"Sprite/Eimi01/Eimi_030_03.png")

image eimi_t: 
    zoom 0.75
    im.Composite((1920,2900), (0,1525), "Sprite/Eimi01/Eimi_Body.png" ,(0,1525),"Sprite/Eimi01/Eimi_030_03.png")

image artroom_past= im.Scale("background/artroom/art-room6.jpg",1920,1080)
image artroom_afternoon = im.Scale("background/artroom/art-room1.jpg",1920,1080)

image imagine = im.Scale("background/imagine.png",1920,1080)


image school_park_1= im.Scale("background/SchoolPark01/school-park1.png",1920,1080)
image school_park_2= im.Scale("background/SchoolPark01/school-park2.png",1920,1080)
image school_park_3= im.Scale("background/SchoolPark01/school-park3.png",1920,1080)
image school_park_4= im.Scale("background/SchoolPark01/school-park4.png",1920,1080)

image black_scene = im.Scale("background/black.jpg",1920,1080)

image Sky_Morning = im.Scale("background/SKY/Sky_Morning.png",1920,1080)
image Sky_Summer = im.Scale("background/SKY/Sky_Summer.png",1920,1080)
image sky_morning = im.Scale("background/SKY/Sky_Morning.png",1920,1080)
image sky_summer = im.Scale("background/SKY/Sky_Summer.png",1920,1080)

image art_room1 = im.Scale("background/artroom/art-room1.jpg",1920,1080)
image art_room2 = im.Scale("background/artroom/art-room2.jpg",1920,1080)
image art_room3 = im.Scale("background/artroom/art-room3.jpg",1920,1080)
image art_room4 = im.Scale("background/artroom/art-room4.jpg",1920,1080)
image art_room5 = im.Scale("background/artroom/art-room5.jpg",1920,1080)
image art_room6 = im.Scale("background/artroom/art-room6.jpg",1920,1080)


image sunset1 = im.Scale("background/SKY/Sunset1.png",1920,1080)
image sunset2 = im.Scale("background/SKY/Sunset2.png",1920,1080)
image sunset3 = im.Scale("background/SKY/Sunset3.png",1920,1080)
image sunset4 = im.Scale("background/SKY/Sunset4.png",1920,1080)


image Sunset1 = im.Scale("background/SKY/Sunset1.png",1920,1080)
image Sunset2 = im.Scale("background/SKY/Sunset2.png",1920,1080)
image Sunset3 = im.Scale("background/SKY/Sunset3.png",1920,1080)
image Sunset4 = im.Scale("background/SKY/Sunset4.png",1920,1080)

image Canvas = im.Scale("Cutscene/Canvas00.png",1920,1080)

image route1 = im.Scale("background/route/route1.jpg",1920,1080)
image route2 = im.Scale("background/route/route2.jpg",1920,1080)
image route3 = im.Scale("background/route/route3.jpg",1920,1080)
image route4 = im.Scale("background/route/route4.jpg",1920,1080)
image route5 = im.Scale("background/route/route5.jpg",1920,1080)

image dot1 = im.Scale("Sprite/Effect/dot1.png",800,1000)
image dot2 = im.Scale("Sprite/Effect/dot2.png",800,1000)
image dot3 = im.Scale("Sprite/Effect/dot3.png",800,1000)

image laught1 = im.Scale("Sprite/Effect/laught.png",800,1000) 
image laught2 = im.Scale("Sprite/Effect/laught2.png",800,1000) 

image coffee01 = im.Scale("CG/CG01/coffee01.png",1920,1080)
image coffee02 = im.Scale("CG/CG01/coffee02.png",1920,1080)
image coffee03 = im.Scale("CG/CG01/coffee03.png",1920,1080)
image coffee04 = im.Scale("CG/CG01/coffee04.png",1920,1080)
image coffee05 = im.Scale("CG/CG01/coffee05.png",1920,1080)
image coffee06 = im.Scale("CG/CG01/coffee06.png",1920,1080)

image school_gym_a = im.Scale("background/gym/school_gym_a.jpg",1920,1080)
image school_gym_b = im.Scale("background/gym/school_gym_b.jpg",1920,1080)
image school_gym_c = im.Scale("background/gym/school_gym_c.jpg",1920,1080)

image School_Hallway1_sunset = im.Scale("background/school_Hallway/School_Hallway1_sunset.png",1920,1080)
image School_Hallway1_1 = im.Scale("background/school_Hallway/School_Hallway1_1.png",1920,1080)
image Roof = im.Scale("background/Roof2/Roof.jpg",1920,1080)

image GoldenTime01 = im.Scale("CG/CG02/GoldenTime01.png",1920,1080)
image GoldenTime02 = im.Scale("CG/CG02/GoldenTime02.png",1920,1080)


image clickToContinue:
    "diamond-large-off.png"

image canvas_death:
    "CG/Canvas_Death/item02.png"

image angry:
    "Sprite/Effect/angry.png"

image aware:
    "Sprite/Effect/aware.png"

image border:
    "Sprite/Effect/border.png"

image dark:
    "Sprite/Effect/dark.png"
image down:
    "Sprite/Effect/down.png"

image excited:
    "Sprite/Effect/excited1.png"
    pause 0.5
    "Sprite/Effect/excited2.png"
    pause 0.5
    repeat

image happy:
    "Sprite/Effect/happy.png"
image heart:
    "Sprite/Effect/heart.png"
image huh:
    "Sprite/Effect/huh.png"
image moyamoya:
    "Sprite/Effect/moyamoya.png"
image pout:
    "Sprite/Effect/pout.png"
image question:
    "Sprite/Effect/question.png"

image shine:
    "Sprite/Effect/shine.png"
image surprise:
    "Sprite/Effect/surprise.png"
image sweat:
    "Sprite/Effect/sweat.png"
image wakaru:
    "Sprite/Effect/wakaru.png"

image spotlight:
    "Sprite/Effect/spotlight.png"

image dot:
    "Sprite/Effect/dot1.png"
    pause 0.5
    "Sprite/Effect/dot2.png"
    pause 0.5
    "Sprite/Effect/dot3.png"
    pause 0.5
    "Sprite/Effect/dot1.png"
    repeat

image laught:
    "Sprite/Effect/laught.png"
    pause 0.5
    "Sprite/Effect/laught2.png"
    pause 0.5
    repeat

image panic:
    "Sprite/Effect/panic1.png"
    pause 0.5
    "Sprite/Effect/panic2.png"
    pause 0.5
    repeat


image main_scene_1 = im.Scale("Animation/anime01.png",1920,1080)
image main_scene_2 = im.Scale("Animation/anime02.png",1920,1080)
image main_scene_3 = im.Scale("Animation/anime03.png",1920,1080)
image main_scene_4 = im.Scale("Animation/anime04.png",1920,1080)
image main_scene_5 = im.Scale("Animation/anime05.png",1920,1080)
image main_scene_6 = im.Scale("Animation/anime06.png",1920,1080)
label splashscreen:
    scene black with Dissolve(1.0)
    scene main_scene_1 with Dissolve(0.5)
    scene main_scene_2 with Dissolve(0.5)
    scene main_scene_3 with Dissolve(0.5)
    scene main_scene_4 with Dissolve(0.5)
    scene main_scene_5 with Dissolve(0.5)
    scene main_scene_6 with Dissolve(0.5)
    return
image thankyouImg = im.Scale("thx.png",1920,1080)
image endCredit= im.Scale("credit.png",1920,1080)
image _thankyouImg = im.Scale("thx.png",1920,1080)
image _endCredit= im.Scale("credit.png",1920,1080)



image BadPic2 =  im.Scale("CG/Eimi_bird/BadPic2.png",1920,1080)

image cutscene_1_0 =  im.Scale("Cutscene/unit01/unit01_00.png",1920,1080)
image cutscene_1_1 =  im.Scale("Cutscene/unit01/unit01_01.png",1920,1080)
image cutscene_1_2 =  im.Scale("Cutscene/unit01/unit01_02.png",1920,1080)
image _cutscene_1_2 =  im.Scale("Cutscene/unit01/unit01_02.png",1920,1080)

image cutscene_2_0 =  im.Scale("Cutscene/unit02/unit2_00.png",1920,1080)
image cutscene_2_1 =  im.Scale("Cutscene/unit02/unit2_01.png",1920,1080)
image cutscene_2_2 =  im.Scale("Cutscene/unit02/unit2_02.png",1920,1080)
image _cutscene_2_2 =  im.Scale("Cutscene/unit02/unit2_02.png",1920,1080)

image cutscene_3_0 =  im.Scale("Cutscene/unit03/unit03_00.png",1920,1080)
image cutscene_3_1 =  im.Scale("Cutscene/unit03/unit03_01.png",1920,1080)
image cutscene_3_2 =  im.Scale("Cutscene/unit03/unit03_02.png",1920,1080)
image _cutscene_3_2 =  im.Scale("Cutscene/unit03/unit03_02.png",1920,1080)

image badend_0 = im.Scale("Cutscene/badend/badend02.png",1920,1080)
image _badend_0 = im.Scale("Cutscene/badend/badend02.png",1920,1080)

screen pausenow():
    key "dismiss" action NullAction()
label cutscene_1:

    scene black with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    scene cutscene_1_0 with Dissolve(1.0)
    play sound "audio/SoundEffect/sumahokessai.mp3" volume 1.0
    $renpy.pause(0.01, hard=True)
    scene cutscene_1_1 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    scene cutscene_1_2 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    scene _cutscene_1_2 with Dissolve(2.0)
    hide artroom_afternoon
    jump q2_1
    
label cutscene_2:
    $renpy.pause(0.01, hard=True)
    scene black with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    show cutscene_2_0 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    play sound "audio/SoundEffect/sumahokessai.mp3" volume 1.0
    $renpy.pause(0.01, hard=True)
    show cutscene_2_1 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    show cutscene_2_2 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    show _cutscene_2_2 with Dissolve(2.0)

    jump q3_1

label cutscene_3:
    $renpy.pause(0.01, hard=True)
    $ quick_menu = False
    $renpy.pause(0.01, hard=True)
    scene black with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    show cutscene_3_0 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    play sound "audio/SoundEffect/sumahokessai.mp3" volume 1.0
    $renpy.pause(0.01, hard=True)
    show cutscene_3_1 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    show cutscene_3_2 with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    show _cutscene_3_2 with Dissolve(2.0)
    $renpy.pause(0.01, hard=True)
    jump endcreditScreen
    return

label endcreditScreen:
    pause 0.01
    scene black with Dissolve(1.0)
    scene endCredit with Dissolve(2.0)
    pause 0.01
    scene _endCredit with Dissolve(2.0)
    pause 2
    scene thankyouImg with Dissolve(2.0)
    pause 0.01
    scene _thankyouImg with Dissolve(2.0)
    pause 2
    jump splashscreen
    return

label badend:
    $renpy.pause(0.01, hard=True)
    $ quick_menu = False
    $renpy.pause(0.01, hard=True)
    scene black with Dissolve(1.0)
    $renpy.pause(0.01, hard=True)
    scene badend_0 with Dissolve(2.0)
    $renpy.pause(0.01, hard=True)
    scene _badend_0 with Dissolve(3.0)
    $renpy.pause(0.01, hard=True)
    jump splashscreen
    return




    
label transition_screen:
    scene Canvas with Dissolve(2.0)
    $renpy.pause(2.0,hard = True)
    jump q002


style ascend:
    outlines [ (absolute(1), "#00ff00", absolute(0), absolute(0)) ]

label start:
    scene dark with Dissolve(2.0)
    $ point = 0
    scene Canvas with Dissolve(2.0)
    play music "audio/bgm/nagai_no_yoru.mp3" volume 0.5 
    show text "{size=40}หากเราไม่พยายามและไม่เชื่อในสิ่งที่ตัวเองทำก็เท่ากับแพ้ตั้งแต่แรก" with Dissolve(1.0)
    $ renpy.pause(2)
    hide text with Dissolve(1.0)
    show text  "{size=40}ไม่ว่าจะเกิดอะไรขึ้นก็ตาม...จงอย่าทรยศต่อความฝันของตัวเอง..." with Dissolve(1.0)
    $ renpy.pause(2)
    hide text with Dissolve(1.0)



    scene artroom_past with Dissolve(1.0)
    hide Canvas

    jump q4_1

    tk "นายน่ะ เลิกเถอะ..."
    a "รุ่นพี่ว่ายังไงนะครับ?"
    n "ผมไม่เข้าใจว่าทำไมผมต้องพูดซ้ำด้วย"

    n "นอกจากจะไม่มีความสามารถแล้วยังหูไม่ดีอีก ต้องให้ผมเสียเวลาแค่ไหนกันถึงจะให้คนพวกนี้เข้าใจสภาพความจริงได้"
    tk "นายฝืนวาดไปเรื่อยๆแบบนี้นายก็ไม่เก่งขึ้น นายกำลังเสียเวลาอยู่"
    a "รุ่นพี่จะบอกว่าที่ผมทำทั้งหมดมันไม่มีความหมายเหรอครับ"
    n "ผมไม่ได้ตอบเขาด้วยคำพูด เพียงแค่พยักหน้าเท่านั้น"
    n "แค่นั้นก็เป็นคำตอบที่มากพอจะให้บรรยากาศในห้องชมรมหมองลงแล้ว"
    tk "นายไม่เคยฟังที่ฉันสอนเลย มัวแต่ทำผิดพลาดเรื่องเดิมๆ"
    a "ก็ผมน่ะ อยากจะ...!"
    tk "อยากจะทำงานที่เป็นแบบของตัวเอง ใช่ไหมล่ะ?"
    a "......!!"
    n "ผมพูดขัดบท คนฟังเลยเถียงกลับไม่ได้เพราะผมอ่านออกว่าเขาต้องการอะไรตั้งแต่แรก"
    n "น่าเสียดายที่สิ่งที่เขาต้องการจะไม่สามารถทำให้อะไรดีๆงอกเงยออกมาได้แม้แต่อย่างเดียว"
    tk "ความต้องการของนายเป็นสิ่งที่ดี แต่ถ้านายไม่มีทักษะที่แข็งพอ...ผลงานที่เป็นตัวของตัวเองแล้วออกมาดีก็เป็นแค่ลมปากที่ไม่มีน้ำหนักเท่านั้น..."
    a "จะพูดเกินไปแล้วนะครับ!"
    n "ผมก็เห็นด้วยว่าผมพูดแรงเกินไป แต่สำหรับผมแล้ว การพูดความจริงที่รุนแรงนั้นดีกว่าคำโกหกที่มอบได้แค่ความรู้สึกดีชั่วคราว"
    n "ถ้าอยากเก่งขึ้นก็ต้องทนให้ได้กับคำดูถูก มันเป็นเรื่องปกติในวงการนี้"
    a "ถ้ารุ่นพี่ยังไม่ไว้หน้าใครแบบนี้ไปเรื่อยๆสักวันจะไม่มีใครฟังรุ่นพี่นะครับ..."
    tk "......"
    n "ผมเงียบลงชั่วขณะ ในใจแอบคิดว่าแท้จริงแล้วคำพูดที่ผมเคยพูดให้คนอื่นฟังมีความหมายรึเปล่า"
    n "ทุกคำสั่งสอน ทุกคำวิจารณ์ ทุกการแลกเปลี่ยนในงานสร้างสรรค์ บางทีก็ส่งไปไม่ถึงคนดูงานศิลปะหรือคนที่ทำงานด้วยกัน"
    n "แท้จริงแล้วคนเรารับรู้คำพูดของอีกฝ่ายจริงๆหรือเลือกฟังเฉพาะสิ่งที่ตัวเองอยากจะฟังกันแน่"
    n "จริงๆแล้ว อาจจะเป็นผมเองก็ได้ที่บ้าไปเองคนเดียว"
    tk "ฉันจะจำคำเตือนนั้นไว้แล้วกัน"
    n "ไม่มีคำตอบดังมาจากคนอื่นในห้องชมรมอีก"
    n "สิ่งเดียวที่ผมจำได้คือดวงตาของคนอื่นๆที่มองผมด้วยความผิดหวัง"
    n "...ไม่ก็ความหวาดกลัว"
    stop music
    n "..."
    jump q002

    return

label q002:

    scene dark with Dissolve(0.2)
    scene artroom_afternoon with Dissolve(2.0)   
    hide dark
    tk "หืม?"
    n "ผมลืมตาตื่นขึ้นท่ามกลางห้องชมรมที่ไม่เหลือใครนอกจากผม ช่วงเวลาที่มีคนมากมายอยู่ในชมรมนี้มันกี่เดือนก่อนกันนะ? ผมเริ่มจะจำไม่ได้แล้ว"
    n "ผมขยี้ตาเพื่อปลุกให้ตัวเองตื่นขึ้นก่อนจะผุดลุกขึ้นช้าๆ"
    tk "ฝันเรื่องเก่าๆอีกแล้ว...อย่างงั้นเหรอ...?"
    n "ผมพึมพำกับตัวเองคนเดียว"

    scene school_park_1 with Dissolve(1.0)
    play music "audio/bgm/hijimeta_no_date.mp3" volume 0.5
    hide artroom_afternoon  with Dissolve(1.0)
    n "เดินออกมาจากห้องชมรมแล้ว ผมก็ทำตามกำหนดการที่วางแผนมาตั้งแต่แรก"
    n "กระดาษวาดรูป พร้อม!"
    n "พู่กันและจานสี พร้อม!"
    n "กาแฟที่เอาไว้เพิ่มพลังตอนทำงาน พร้อม!"
    n "บรรยากาศปลอดโปร่งที่เหมาะสมสำหรับการวาดรูป พร้อม!"
    n "...ผมใกล้จะเรียนจบม.6 แล้ว เลยมีแผนที่จะฝากผลงานไว้ทิ้งไว้ในฐานะสมาชิกชมรมศิลปะ"
    n "มันก็เป็นหน้าที่ของผมที่จะต้องให้ชมรมมีผลงานสักอย่างก่อนที่ผมจะเรียนจบ"
    n "ภาพที่วาดมาหลายต่อหลายวันใกล้จะสำเร็จ"
    n "ว่าแล้วก็ลงมือเล..."
    scene sky_morning with Dissolve(1.0)
    show excited with Dissolve(1.0)
    stop music
    play music "audio/bgm/dotabata_happening.mp3" volume 0.5
    play sound "audio/SoundEffect/KFJZC74-crash-with-debris.mp3" volume 1.0
    n "{size=50}ตูมมมมมมมมมมมมมมมมมมมมมมม!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    hide excited
    e0 "กรี๊ดดดด!!!!!!!"
    tk "อ้ากกกกกก!!!!!!!!!!"
    n "เสียงผู้หญิงคนหนึ่งกรีดร้องดังขึ้นข้างๆผม"
    n "ผมอยากจะบอกเลยว่าคนอยากกรี๊ดคือผมต่างหาก อยากจะกรี๊ดให้คอแตกไปข้างเลย"
    n "ยังปลุกใจตัวเองคนเดียวไม่เสร็จก็มีสาวน้อยคนหนึ่งวิ่งด้วยความเร็วราวกับรถแข่งเอฟวันเข้ามาหาผม"
    n "อุปกรณ์วาดภาพ กระดาษบนขาตั้งวาดรูปและกาแฟบนโต๊ะน้อยๆของผมระเนระนาดไปหมด"
    n "ทั้งๆที่สาวน้อยคนนั้นตัวเล็กกว่าผม แต่ด้วยความเร็วและพละกำลังที่มากเกินขนาดตัวทำให้ผมกลิ้งโคโล่ไปกับพื้นสองสามเมตร\nเป็นเพื่อนอุปกรณ์วาดรูปของผม"
    n "วาดรูปอยู่ดีๆทำไมเรามานอนมองท้องฟ้ากันนะ ชีวิตผมมันเกิดบ้าอะไรขึ้น?"
    scene school_park_1 with Dissolve(1.0)
    show Eimi_Eimi_cry_meme2
    show sweat with Dissolve(1.0)
    e0 "ขอโทษค่ะ! ฉันวิ่งไม่ดูทา..." with dissolve
    hide sweat
    tk "ว้ากกกกกกกกส์ส์ส์ส์!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    hide  Eimi_Eimi_cry_meme2 
    show  Eimi_Eimi_o 
    show surprise with Dissolve(1.0)
    e0 "อุหวา! มันเกิดอะไรขึ้นเหรอค้า!?" with dissolve
    hide surprise
    n "ผมไม่อยากจะเชื่อภาพที่ตัวเองเห็น"
    "ถึงแม้จะเพิ่งล้มกลิ้งกับพื้นแต่ผมใช้กำลังที่ยังเหลืออยู่คลานไปหาภาพวาดของผม"
    tk "ไม่นะ! งานส่งประกวดของฉัน!"
    hide Eimi_Eimi_o 
    show Eimi_Eimi_0_0
    show down with Dissolve(1.0)
    e0 "ห๊ะ? งานส่งประกวดเหรอคะ!?" with dissolve
    hide down
    n "...ภาพวาดของผมเต็มไปด้วยกาแฟทาบทับเต็มไปหมด"
    "รูปวาดของผมจมกาแฟตายไปแล้ว!"
    tk "ทั้งๆที่ฉันใช้เวลาวาดผลงานชิ้นเอกชิ้นนี้เกือบสัปดาห์หนึ่งแท้ๆ"
    hide Eimi_Eimi_0_0
    show Eimi_Eimi_panic 
    show panic with Dissolve(1.0)
    e0 "1 สัปดาห์!" with dissolve
    hide panic
    tk "แล้วงานประกวดก็จะต้องส่งสัปดาห์หน้าแล้วด้วย..."
    e0 "งั้นก็ใกล้มากแล้วสิคะ"
    tk "ใกล้มากจนการทำงานใหม่ส่งแทบจะเป็นไปไม่ได้เลย โอวววว..."
    e0 "ทะ...ทำใจไว้ดีๆก่อนนะคะ"
    hide Eimi_Eimi_panic 
    show Eimi_Eimi_cry_meme2  
    n "วิญญาณน้อยๆของผมแทบจะหลุดลอยออกจากปาก" with dissolve
    n "ความสิ้นหวังทะลักทลายเข้ามาในจิตใจผมอย่างหยุดไม่ได้"
    n "งานที่ผมทุ่มเทฝีมือทั้งหมด ใช้เวลากับมันอย่างยาวนานและมั่นใจว่ามันต้องออกมาดีมากแน่ๆเพราะผมใช้ทั้งฝีมือ \nแรงบันดาลใจและจิตวิญญาณทั้งหมดเพื่อคลอดผลงานนี้ออกมา"
    n "หยาดเหงื่อแรงงานของผมพังเป็นชิ้นๆเพราะสาวน้อยคนหนึ่งและกาแฟอีกแก้วหนึ่ง"
    n "นี่มันเรื่องตลกอะไรกันฟะ!?"
    tk "เธอน่ะ...ชื่ออะไร?...ชั้นปีอะไร?"
    hide Eimi_Eimi_cry_meme2 
    show eimi_2  
    ei "อิทสึกิ เอมิค่ะ อยู่ม.4 ...เพิ่งย้ายเข้ามาเรียนโรงเรียนนี้ปีนี้ค่ะ" with dissolve
    tk "เพิ่งย้ายเข้ามาก็สร้างความบรรลัยเลยนะ แสบจริงๆ"
    hide eimi_2 
    show Eimi02_Eimi02_smile 
    show question with Dissolve(1.0)
    ei "คะ?" with dissolve
    hide question
    tk "ชดใช้..."
    hide Eimi02_Eimi02_smile

    show Eimi02_Eimi02_0
    ei "หา?????" with dissolve
    n "ผมสูดหายใจเข้าลึกๆก่อนที่จะส่งเสียงตะโกนแบบที่ผมมั่นใจว่าไม่เคยตะโกนดังขนาดนี้มาก่อนในชีวิต"
    tk "ยัยบ้า! ชดใช้มาเดี๋ยวนี้เลยนะเฟ้ยยยยยยยยย!!!!!!!!!!!!!!"
    hide Eimi02_Eimi02_0
    show Eimi_Eimi_panic
    show panic with Dissolve(1.0)
    ei "หวา!!! รุ่นพี่ค้า--!!" with dissolve
    hide panic
    n "ผมพุ่งเข้าไปหารุ่นน้องตัวแสบพร้อมกับกำพู่กันในมือแน่น"
    play sound "audio/SoundEffect/zakuxtu.mp3" volume 1.0
    n "รู้ตัวอีกทีความเดือดดาลก็ทำให้ผมเอาแท่งพู่กันยาวไล่แทงคนทำลายผลงานผมจนเธอต้อง\nวิ่งหนีผมวนไปวนมารอบกองงานศิลปะผม"
    n ""
    n "ไม่สิ...ต้องเรียกว่าสุสานของงานศิลปะผมดีกว่า งานของผมถูกกาแฟลบหายไปหมดแล้ว T_T”"
    hide Eimi_Eimi_panic
    show Eimi_Eimi_hurt_meme
    ei "กรี๊ดด! รุ่นพี่! อย่าเพิ่งฆ่าหนู!" with dissolve
    tk "คนเรามันไม่ตายเพราะแท่งพู่กันเสียบหรอกโว้ย!"
    hide Eimi_Eimi_hurt_meme
    show Eimi_Eimi_cry_meme3
    ei "เมตตาหนูด้วยค่า เมตตาหนูด้วยค่า!" with dissolve
    tk "ความผิดนี้น่ะ คว้านท้องสักล้านครั้งยังไม่พอเลยยัยบ้านี่!!!"
    hide Eimi_Eimi_cry_meme3
    show Eimi_Eimi_hurt_meme
    ei "คว้านท้องครั้งเดียวก็ตายแล้วค่า จะล้านครั้งทำไมกันค้า-- " with dissolve
    tk "ไม่รู้ล่ะๆๆๆๆๆ ชดใช้มาๆๆๆๆ!!"
    ei "ไว้ชีวิตเค้าด้วย ม่ายยยยย!!!!!!!!!!!!!!!"
    scene sky_morning with Dissolve(1.0)
    n "นี่คือการพบกันครั้งแรกของผมกับเอมิ"
    n "ว่ากันตามตรงแล้วเป็นการพบกันครั้งแรกที่ตราตรึงในความทรงจำผมไปจนวันตายแน่นอน"
    stop music
    jump q003
    return


    




















#     show cat1 at left
    

#     # These display lines of dialogue.

#     c "น้องแมวที่บ้านผมมันไม่เล่นกับผมแล้ว"
#     c "ไปหยิบแมวหน้าบ้านมาดีไหม"

#     hide cat1

#     menu : 
#         "หยิบดิ รอไร" : 
#             $ point +=1
#         "แล้วแมวที่เมิงหล่ะ" : 
#             $ point +=0
#     # This ends the game.
#     if point > 0:
#         n "คุณได้รับแมวหนึ่งตัว"
#         jump after
#     else :
#         n "คุณไม่เหลืออะไรอีกต่อไป"
 
#     return

# label after:
#     scene bg room
#     show cat1

#     c "จะไปหยิบมาอีกตัวมั้ย"