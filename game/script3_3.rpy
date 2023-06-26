label q3_3:
    show art_room2 with Dissolve(1.0)
    n "การที่ยัยนั่นอยู่หรือไม่อยู่เกี่ยวกับเรา แต่พอมีอะไรสักอย่างคาใจแล้วมันทำงานต่อไม่ลงชอบกล" with dissolve
    "ผมต้องตามหาเอมิ"
    "...ไม่อยากจะนึกเลยว่าตัวเองจะทำแบบนี้ "
    "แต่พอถามตัวเองขึ้นมาว่าควรจะทำอะไรต่อไปดี เสียงแรกที่ดังขึ้นมาคือเสียงตะโกนในใจตัวเองว่าต้องไปหายัยนั่น"
    "...สังหรณ์ไม่ดีเลย "
    "ปกติยัยนั่นไม่ใช่คนที่น่าจะหายตัวไปแบบไม่มีปี่ไม่มีขลุ่ยด้วย"
    "มันต้องมีเหตุผลอะไรสักอย่างสิ..." 
    show School_Hallway1_sunset with fade    
    hide art_room2
    play sound "audio/SoundEffect/walk.mp3" volume 5.0
    "ผมเดินไปตามทางเดินห้องเรียนเพื่อตามหาเอมิ"
    "ส่องสายตาเข้าไปแต่ละห้องๆก็ไม่เจอยัยนั่นนั่งอยู่สักห้อง"
    "ลองแอบถามคนตามทางว่าห้องเรียนเอมิไปทางไหน แต่พอไปถึงแล้วก็ไม่มีแม้แต่เงาหรือปลายเส้นผมของยัยนั่นอยู่"
    "...ผมคงต้องเดินตามหาต่อไปสินะ"
    show school_gym_b with fade
    hide School_Hallway1_sunset
    play sound "audio/SoundEffect/walk.mp3" volume 5.0
    "หลังจากในอาคารเรียนเสร็จก็ลองมาส่องโรงยิมดู"
    "ไม่มีใครอยู่ที่นี่แม้แต่คนเดียว ทุกคนน่าจะกลับไปหมดแล้ว "
    "เพราะเอมิดูเป็นคนขยันซ้อม ผมเลยนึกว่าเธอน่าจะซุ่มฝึกอยู่แถวๆนี้ แต่กลับไม่เจอเหมือนกัน"
    "ดูเหมือนจะมาเสียเที่ยว..."
    "บางทียัยนั่นอาจจะกลับบ้านไปแล้ว..."
    "หรือผมกำลังทำอะไรที่ไม่มีประโยชน์อยู่นะ "
    "บางทีพรุ่งนี้ยัยนั่นอาจจะกลับมาหาผมที่ห้องชมรมเหมือนเดิมก็ได้ แล้ววันนี้ที่ไม่มาก็อาจจะเพราะติดธุระ ผมคงคิดมากไปเอง"
    "แต่ความรู้สึกแปลกๆนี่มันอะไรกัน?"
    "...บางอย่างในตัวผมบอกผมว่ามันมีความขัดแย้งในความคิดผม"
    "ผมควรจะทำยังไงต่อไปดี?"
    "ทำอะไรดี?"
    menu :
        "ตามหาต่อ":
            jump q3_4
        "เลิกตามหาแล้วเดินกลับบ้าน":
            jump badend2_2
    return
