# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character(None, who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define c = Character("{font=THSarabunNew Bold.ttf}{size=+10}น้องแมวที่บ้านผม",color="#F0F8FF", who_outlines=[(1,"#000000")], what_outlines=[(2,"#000000")])
# The game starts here.

image cat1: 
    zoom 0.35
    im.Composite((1920,2900), (0,0), "Sprite/Eimi01/Eimi_Body.png" ,(0,0),"Sprite/Eimi01/Eimi_0.0.png")

label start:

    $ point = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cat1 at left
    

    # These display lines of dialogue.

    c "น้องแมวที่บ้านผมมันไม่เล่นกับผมแล้ว"
    c "ไปหยิบแมวหน้าบ้านมาดีไหม"

    hide cat1

    menu : 
        "หยิบดิ รอไร" : 
            $ point +=1
        "แล้วแมวที่เมิงหล่ะ" : 
            $ point +=0
    # This ends the game.
    if point > 0:
        n "คุณได้รับแมวหนึ่งตัว"
    else :
        n "คุณไม่เหลืออะไรอีกต่อไป"
 
    return
