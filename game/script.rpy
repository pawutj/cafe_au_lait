# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character(None, who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define ei = Character("{font=THSarabunNew Bold.ttf}{size=+10}Eimi",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
define tk = Character("{font=THSarabunNew Bold.ttf}{size=+10}Takagi",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
define a = Character("{font=THSarabunNew Bold.ttf}{size=+10}Student A",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
# The game starts here.

image eimi_0: 
    zoom 0.35
    im.Composite((1920,2900), (0,0), "Sprite/Eimi01/Eimi_Body.png" ,(0,0),"Sprite/Eimi01/Eimi_0.0.png")

image artroom_past= im.Scale("background/artroom_sepia.png",1920,1080)
image artroom_afternoon = im.Scale("background/artroom_afternoon.png",1920,1080)

label start:

    $ point = 0
    scene black

    n "หากเราไม่พยายามและไม่เชื่อในสิ่งที่ตัวเองทำก็เท่ากับแพ้ตั้งแต่แรก"
    n "ไม่ว่าจะเกิดอะไรขึ้นก็ตาม...จงอย่าทรยศต่อความฝันของตัวเอง..."

    scene artroom_past with Dissolve(1.0)

    tk "หืม?"
    n "ผมลืมตาตื่นขึ้นท่ามกลางห้องชมรมที่ไม่เหลือใครนอกจากผม"
    n "ช่วงเวลาที่มีคนมากมายอยู่ในชมรมนี้มันกี่เดือนก่อนกันนะ? ผมเริ่มจะจำไม่ได้แล้ว"
    n "ผมขยี้ตาเพื่อปลุกให้ตัวเองตื่นขึ้นก่อนจะผุดลุกขึ้นช้าๆ"
    tk "ฝันเรื่องเก่าๆอีกแล้ว...อย่างงั้นเหรอ...?"
    n "ผมพึมพำกับตัวเองคนเดียว"

    return

label q002:
    




















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