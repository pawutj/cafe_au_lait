
screen show_cg01_01():
    key "mouseup_3" action Hide("show_cg01_01",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_01",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_02",Dissolve(0.1)),Hide("show_cg01_01")]
    add "CG/CG01/coffee01.png"

screen show_cg01_02():
    key "mouseup_3" action Hide("show_cg01_02",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_02",Dissolve(0.1))
    key "mouseup_1" action [Hide("show_cg01_02",Dissolve(0.1))]
    add "CG/CG01/coffee02.png"

screen show_cg01_03():
    key "mouseup_3" action Hide("show_cg01_02",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_02",Dissolve(0.1))
    add "CG/CG01/coffee03.png"



screen show_cg01_04():
    key "mouseup_3" action Hide("show_cg01_04",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_04",Dissolve(0.1))
    add "CG/CG01/coffee04.png"

screen show_cg01_05():
    key "mouseup_3" action Hide("show_cg01_05",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_05",Dissolve(0.1))
    add "CG/CG01/coffee04.png"


screen show_cg01_06():
    key "mouseup_3" action Hide("show_cg01_06",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_06",Dissolve(0.1))
    add "CG/CG01/coffee05.png"