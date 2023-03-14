# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#navigation
define n = Character(None, who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
#eimi
define ei = Character("{font=THSarabunNew Bold.ttf}{size=+10}Eimi",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
#takagi
define tk = Character("{font=THSarabunNew Bold.ttf}{size=+10}Takagi",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
#student a
define a = Character("{font=THSarabunNew Bold.ttf}{size=+10}Student A",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
#student ???
define e0 = Character("{font=THSarabunNew Bold.ttf}{size=+10}???",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
# The game starts here.

image eimi_0_cry_meme2:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_cry_meme2.png")

image eimi_0_cry_meme1:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_cry_meme1.png")


image eimi_0_0_0:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_0_0.png")


image eimi_0_panic:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_panic.png")

image eimi_0_wakaranai:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_Wakaranai.png")

image eimi_0_hurt_meme:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_hurt_meme.png")

image eimi_0_cry_meme3:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_cry_meme3.png")

image eimi_0: 
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_0.0.png")

image eimi_2:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi02/Eimi02.png")


image eimi_02_wakaranai:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi02/Eimi02_body.png" ,(30,1500),"Sprite/Eimi01/Eimi_Wakaranai.png")

image eimi_02_0_0:
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi02/Eimi02_body.png"  ,(30,1500),"Sprite/Eimi01/Eimi_0_0.png")


image eimi_30: 
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_030_03.png")

image eimi_t: 
    zoom 0.75
    im.Composite((1920,2900), (0,1500), "Sprite/Eimi01/Eimi_Body.png" ,(0,1500),"Sprite/Eimi01/Eimi_030_03.png")

image artroom_past= im.Scale("background/artroom/art-room2.jpg",1920,1080)
image artroom_afternoon = im.Scale("background/artroom/art-room1.jpg",1920,1080)

image school_park_1= im.Scale("background/school-park/school-park1.jpg",1920,1080)
image school_park_2= im.Scale("background/school-park/school-park2.jpg",1920,1080)
image school_park_3= im.Scale("background/school-park/school-park3.jpg",1920,1080)
image school_park_4= im.Scale("background/school-park/school-park4.jpg",1920,1080)


image sky_morning = im.Scale("background/SKY/Sky_Morning.png",1920,1080)



label start:

    $ point = 0
    scene black
    play music "audio/bgm/nagai_no_yoru.mp3" volume 0.5
    show text "หากเราไม่พยายามและไม่เชื่อในสิ่งที่ตัวเองทำก็เท่ากับแพ้ตั้งแต่แรก" with Dissolve(1.0)
    $ renpy.pause(2)
    hide text with Dissolve(1.0)
    show text  "ไม่ว่าจะเกิดอะไรขึ้นก็ตาม...จงอย่าทรยศต่อความฝันของตัวเอง..." with Dissolve(1.0)
    $ renpy.pause(2)
    hide text with Dissolve(1.0)
    scene artroom_past with Dissolve(1.0)
    tk "นายน่ะ เลิกเถอะ..."
    a "รุ่นพี่ว่ายังไงนะครับ?"
    n "ผมไม่เข้าใจว่าทำไมผมต้องพูดซ้ำด้วย"
    a "นอกจากจะไม่มีความสามารถแล้วยังหูไม่ดีอีก ต้องให้ผมเสียเวลาแค่ไหนกันถึงจะให้คนพวกนี้เข้าใจสภาพความจริงได้"
    tk "นายฝืนวาดไปเรื่อยๆแบบนี้นายก็ไม่เก่งขึ้น นายกำลังเสียเวลาอยู่"
    a "รุ่นพี่จะบอกว่าที่ผมทำทั้งหมดมันไม่มีความหมายเหรอครับ"
    n "ผมไม่ได้ตอบเขาด้วยคำพูด เพียงแค่พยักหน้าเท่านั้น"
    n "แค่นั้นก็เป็นคำตอบที่มากพอจะให้บรรยากาศในห้องชมรมหมองลงแล้ว"
    tk "นายไม่เคยฟังที่ฉันสอนเลย มัวแต่ทำผิดพลาดเรื่องเดิมๆ"
    a "ก็ผมน่ะ อยากจะ...!"
    tk "อยากจะทำงานที่เป็นแบบของตัวเอง ใช่ไหมล่ะ?"
    a "........!!"
    n "ผมพูดขัดบท คนฟังเลยเถียงกลับไม่ได้เพราะผมอ่านออกว่าเขาต้องการอะไรตั้งแต่แรก"
    n "น่าเสียดายที่สิ่งที่เขาต้องการจะไม่สามารถทำให้อะไรดีๆงอกเงยออกมาได้แม้แต่อย่างเดียว"
    tk "ความต้องการของนายเป็นสิ่งที่ดี แต่ถ้านายไม่มีทักษะที่แข็งพอ...ผลงานที่เป็นตัวของตัวเองแล้วออกมาดีก็เป็นแค่ลมปากที่ไม่มีน้ำหนักเท่านั้น..."
    a "จะพูดเกินไปแล้วนะครับ!"
    n "ผมก็เห็นด้วยว่าผมพูดแรงเกินไป แต่สำหรับผมแล้ว การพูดความจริงที่รุนแรงนั้นดีกว่าคำโกหกที่มอบได้แค่ความรู้สึกดีชั่วคราว"
    n "ถ้าอยากเก่งขึ้นก็ต้องทนให้ได้กับคำดูถูก มันเป็นเรื่องปกติในวงการนี้"
    a "ถ้ารุ่นพี่ยังไม่ไว้หน้าใครแบบนี้ไปเรื่อยๆสักวันจะไม่มีใครฟังรุ่นพี่นะครับ..."
    tk "..............."
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
    scene artroom_afternoon with Dissolve(1.0)   

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
    n "{size=50}ตูมมมมมมมมมมมมมมมมมมมมมมม!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    e0 "กรี๊ดดดด!!!!!!!"
    tk "อ้ากกกกกก!!!!!!!!!!"
    n "เสียงผู้หญิงคนหนึ่งกรีดร้องดังขึ้นข้างๆผม"
    n "ผมอยากจะบอกเลยว่าคนอยากกรี๊ดคือผมต่างหาก อยากจะกรี๊ดให้คอแตกไปข้างเลย"
    n "ยังปลุกใจตัวเองคนเดียวไม่เสร็จก็มีสาวน้อยคนหนึ่งวิ่งด้วยความเร็วราวกับรถแข่งเอฟวันเข้ามาหาผม"
    n "อุปกรณ์วาดภาพ กระดาษบนขาตั้งวาดรูปและกาแฟบนโต๊ะน้อยๆของผมระเนระนาดไปหมด"
    n "ทั้งๆที่สาวน้อยคนนั้นตัวเล็กกว่าผม แต่ด้วยความเร็วและพละกำลังที่มากเกินขนาดตัวทำให้ผมกลิ้งโคโล่ไปกับพื้นสองสามเมตรเป็นเพื่อนอุปกรณ์วาดรูปของผม"
    n "วาดรูปอยู่ดีๆทำไมเรามานอนมองท้องฟ้ากันนะ ชีวิตผมมันเกิดบ้าอะไรขึ้น?"
    scene school_park_1 with Dissolve(1.0)
    show eimi_0_cry_meme2 
    e0 "ขอโทษค่ะ! ฉันวิ่งไม่ดูทา..." with dissolve
    tk "ว้ากกกกกกกกส์ส์ส์ส์!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    hide eimi_0_cry_meme2 
    show eimi_0_cry_meme1 
    e0 "อุหวา! มันเกิดอะไรขึ้นเหรอค้า!?" with dissolve
    n "ผมไม่อยากจะเชื่อภาพที่ตัวเองเห็น"
    "ถึงแม้จะเพิ่งล้มกลิ้งกับพื้นแต่ผมใช้กำลังที่ยังเหลืออยู่คลานไปหาภาพวาดของผม"
    tk "ไม่นะ! งานส่งประกวดของฉัน!"
    hide eimi_0_cry_meme1 
    show eimi_0_0_0
    e0 "ห๊ะ? งานส่งประกวดเหรอคะ!?" with dissolve
    n "...ภาพวาดของผมเต็มไปด้วยกาแฟทาบทับเต็มไปหมด"
    "รูปวาดของผมจมกาแฟตายไปแล้ว!"
    tk "ทั้งๆที่ฉันใช้เวลาวาดมาสเตอร์พีซชิ้นนี้เกือบสัปดาห์หนึ่งแท้ๆ"
    hide eimi_0_0_0 
    show eimi_0_panic 
    e0 "สัปดาห์หนึ่ง!" with dissolve
    tk "แล้วงานประกวดก็จะต้องส่งสัปดาห์หน้าแล้วด้วย..."
    e0 "งั้นก็ใกล้มากแล้วสิคะ"
    tk "ใกล้มากจนการทำงานใหม่ส่งแทบจะเป็นไปไม่ได้เลย โอวววว..."
    e0 "ทะ...ทำใจไว้ดีๆก่อนนะคะ"
    hide eimi_0_panic 
    show eimi_0_cry_meme2  
    n "วิญญาณน้อยๆของผมแทบจะหลุดลอยออกจากปาก" with dissolve
    n "ความสิ้นหวังทะลักทลายเข้ามาในจิตใจผมอย่างหยุดไม่ได้"
    n "งานที่ผมทุ่มเทฝีมือทั้งหมด ใช้เวลากับมันอย่างยาวนานและมั่นใจว่ามันต้องออกมาดีมากแน่ๆเพราะผมใช้ทั้งฝีมือ แรงบันดาลใจและจิตวิญญาณทั้งหมดเพื่อคลอดผลงานนี้ออกมา"
    n "หยาดเหงื่อแรงงานของผมพังเป็นชิ้นๆเพราะสาวน้อยคนหนึ่งและกาแฟอีกแก้วหนึ่ง"
    n "นี่มันเรื่องตลกอะไรกันฟะ!?"
    tk "เธอน่ะ...ชื่ออะไร?...ชั้นปีอะไร?"
    hide eimi_0_cry_meme2 
    show eimi_2  
    ei "อิทสึกิ เอมิค่ะ อยู่ม.4 ...เพิ่งย้ายเข้ามาเรียนโรงเรียนนี้ปีนี้ค่ะ" with dissolve
    tk "เพิ่งย้ายเข้ามาก็สร้างความบรรลัยเลยนะ แสบจริงๆ"
    hide eimi_2 
    show eimi_02_wakaranai 
    ei "คะ?" with dissolve
    tk "ชดใช้..."
    hide eimi_02_wakaranai
    show eimi_02_0_0
    ei "หา?????" with dissolve
    n "ผมสูดหายใจเข้าลึกๆก่อนที่จะส่งเสียงตะโกน"
    n "ผมมั่นใจว่าผมไม่เคยตะโกนดังขนาดนี้มาก่อนในชีวิต"
    tk "ยัยบ้า! ชดใช้มาเดี๋ยวนี้เลยนะเฟ้ยยยยยยยยย!!!!!!!!!!!!!!"
    hide eimi_02_0_0
    show eimi_0_panic
    ei "หวา!!! รุ่นพี่ค้า--!!" with dissolve
    n "ผมพุ่งเข้าไปหารุ่นน้องตัวแสบพร้อมกับกำพู่กันในมือแน่น"
    n "รู้ตัวอีกทีความเดือดดาลก็ทำให้ผมเอาแท่งพู่กันยาวไล่แทงคนทำลายผลงานผมจนเธอต้องวิ่งหนีผมวนไปวนมารอบกองงานศิลปะผม"
    n "ไม่สิ...ต้องเรียกว่าสุสานของงานศิลปะผมดีกว่า งานของผมถูกกาแฟลบหายไปหมดแล้ว T_T”"
    hide eimi_0_panic
    show eimi_0_hurt_meme
    ei "กรี๊ดด! รุ่นพี่! อย่าเพิ่งฆ่าหนู!" with dissolve
    tk "คนเรามันไม่ตายเพราะแท่งพู่กันเสียบหรอกโว้ย!"
    hide eimi_0_hurt_meme
    show eimi_0_cry_meme3
    ei "เมตตาหนูด้วยค่า เมตตาหนูด้วยค่า!" with dissolve
    tk "ความผิดนี้น่ะ ฮาราคีรีสักล้านครั้งยังไม่พอเลยยัยบ้านี่!!!"
    hide eimi_0_cry_meme3
    show eimi_0_hurt_meme
    ei "ฮาราคีรีครั้งเดียวก็ตายแล้วค่า จะล้านครั้งทำไมกันค้า-- " with dissolve
    tk "ไม่รู้ล่ะๆๆๆๆๆ ชดใช้มาๆๆๆๆ!!"
    ei "ไว้ชีวิตเค้าด้วย ม่ายยยยย!!!!!!!!!!!!!!!"
    scene sky_morning with Dissolve(1.0)
    n "นี่คือการพบกันครั้งแรกของผมกับเอมิ"
    n "ว่ากันตามตรงแล้วเป็นการพบกันครั้งแรกที่ตราตรึงในความทรงจำผมไปจนวันตายแน่นอน"
    stop music


    




















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