label q3_2:
    show art_room1 with Dissolve(1.0)
    play music "audio/bgm/yuki_kaze.mp3" volume 0.5
    n "เป็นเวลาประมาณสัปดาห์หนึ่งแล้วที่เอมิชอบมาหาผมที่ห้องชมรม" with dissolve
    "สมัยก่อนที่นี่เคยเนืองแน่นไปด้วยผู้คนในชมรม แต่ด้วยเหตุผลบางอย่างทำให้คนอื่นๆในชมรมต่างลาออกไป สุดท้ายก็เหลือแค่ผมเหลืออยู่ตัวคนเดียว"
    "หลายเดือนแล้วที่ห้องชมรมนี้เป็นสถานที่ที่แสนสงบเพราะแทบไม่มีคนเดินผ่านทางมาและ\nสมาชิกชมรมก็ต่างหายหัวกันไปหมด"
    "แต่หลังจากเอมิเข้ามาเยี่ยมผมในชมรม สถานที่ที่เงียบเหงาก็กลายเป็นสถานที่ที่คึกคักไปโดยปริยายและก็เป็นแบบนั้นมาราวๆสัปดาห์หนึ่งแล้ว"
    "แต่วันนี้ห้องชมรมกลับเงียบเหงาเหมือนเดิม"
    "เอมิไม่เข้ามาในห้องชมรมในวันนี้เลย"
    "ไม่รู้เพราะว่าอะไร"
    "...วันนี้เหลือแต่ผมนั่งวาดรูปอยู่คนเดียว ทั้งช่วงเช้าและช่วงพักกลางวัน"
    show sky_morning with Dissolve(1.0)
    hide art_room1

    "เอมิ เธอหายไปไหนกันนะ?"
    show sunset1 with Dissolve(1.0)
    hide sky_morning

    "แม้กระทั่งตอนหลังเลิกเรียน เธอก็ยังไม่โผล่หัวมา"
    "...หรือมันจะมีอะไรเกิดขึ้นกับเธอกัน? ความกังวลเริ่มก่อตัวในใจผม"
    show art_room2 with Dissolve(1.0)
    hide sunset1

    "บางทีมันอาจจะเกี่ยวกับเรื่องที่ทำให้เธอเครียดเมื่อวันก่อนก็ได้ ถึงผมไม่รู้ก็เถอะว่ามันคือเรื่องอะไรก็ตาม และผมก็ไม่แน่ใจว่าตัวเองมีสิทธิเข้าไปยุ่งด้วยหรือเปล่า"
    "สำหรับผมแล้ว เอมิก็เป็นแค่รุ่นน้องที่เพิ่งทำความรู้จักกันได้ไม่นาน"
    "พวกเราไม่ได้สนิทกันและไม่ได้มีความสัมพันธ์พิเศษอะไรกัน"
    "ผมเองก็อยู่ในช่วงที่ต้องตั้งใจทำผลงานส่งประกวดด้วย"
    "ถ้าหากเข้าไปยุ่งมากเกินไปก็จะถือก้าวก่ายเธอมากเกินไปหรือเปล่านะ? หรือผมคิดมากไปเอง?"
    "......"
    "ว่าแต่ทำไมผมต้องคิดถึงเรื่องเอมิขนาดนี้ด้วยนะ?"
    "เธอจะอยู่หรือเธอจะไปก็ไม่มีผลอะไรกับผมสักหน่อย "
    "นี่มันแปลกชะมัด...?"
    "......"
    "ผมควรจะทำยังไงดีเนี่ย?"
    "ทำอะไรดี?"
    menu:
        "ผมต้องตามหาเอมิ":
            jump q3_3
        "ผมต้องสนใจปัญหาตัวเองก่อน":
            jump badend2_1
    return
