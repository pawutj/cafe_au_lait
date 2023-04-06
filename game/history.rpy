style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"
    ## Prevents Ren'Py from showing a scrollbar when there's nothing to scroll

screen history():

    tag menu

    predict False

    frame:

        style_prefix "history"

        ## Style this as needed in the style definitions
        label _("History")

        ## If you have a custom image you want to use for the screen, you can set it as
        ## a Frame below.
        # background Frame(["gui/frame.png"], gui.history_frame_borders, tile=True)

        ## Using margin properties will allow the screen to automatically adjust should
        ## you choose to use a different resolution than 1080p, and will always be centered. 
        ## You can also resize the screen using "xmaximum", "ymaximum", or "maximum(x,y)"
        ## if desired, but you will need to use "align(x,y)" to manually position it.

        ## xmargin essentially combines the left_margin and right_margin properties
        ## and sets them to the same value
        xmargin 200

        ## ymargin essentially combines the top_margin and bottom_margin properties
        ## and sets them to the same value
        ymargin 50

        ## xpadding essentially combines the left_padding and right_padding properties
        ## and sets them to the same value
        xpadding 50

        ## ypadding essentially combines the top_padding and bottom_padding properties
        ## and sets them to the same value
        ypadding 150

        vpgrid:

            cols 1
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:

                for h in _history_list:

                    window:

                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True

                        if h.who:

                            label h.who:
                                style "history_name"
                                substitute False

                                ## Take the color of the who text from the Character, if
                                ## set.
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            line_spacing 5
                            substitute False

                    ## This puts some space between entries so it's easier to read
                    null height 20

                if not _history_list:

                    text "The text log is empty." line_spacing 10
                    ## Adding line_spacing prevents the bottom of the text
                    ## from getting cut off. Adjust when replacing the
                    ## default fonts.

        textbutton "Return":
            style "history_return_button"
            action Return()
            alt _("Return") 

style history_label:
    xfill True
    top_margin -100

style history_label_text:
    xalign 0.5
    ## Note: When altering the size of the label, you may need to increase the
    ## ypadding of the Frame, or separate it again into top_padding and bottom_padding

style history_return_button:
    align(1.0,1.0)
    yoffset 100