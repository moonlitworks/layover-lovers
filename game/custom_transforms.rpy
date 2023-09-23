transform topMenu:
    subpixel True
    xalign .5
    on show, replace:
        alpha 0.0 ypos -100
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 ypos 0
    on hide, replaced:
        alpha 1.0
        parallel:
            easein 1.0 alpha 0.0
        parallel:
            easein 1.0 ypos -100

transform bottomMenu:
    subpixel True
    xalign .5
    on show, replace:
        alpha 0.0 yalign 1.0 yanchor 0.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 yanchor 1.0
    on hide, replaced:
        alpha 1.0 yalign 1.0 yanchor 1.0
        parallel:
            easein 1.0 alpha 0.0
        parallel:
            easein 1.0 yanchor 0.0

transform leftMenu:
    subpixel True
    yalign .5
    on show, replace:
        alpha 0.0 xalign 0.0 xanchor 1.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 xanchor 0.0
    on hide, replaced:
        alpha 1.0 xalign 0.0 xanchor 0.0
        parallel:
            easein 1.0 alpha 0.0
        parallel:
            easein 1.0 xanchor 1.0

transform rightMenu:
    subpixel True
    yalign .5
    on show, replace:
        alpha 0.0 xalign 1.0 xanchor 0.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 xanchor 1.0
    on hide, replaced:
        alpha 1.0 xalign 1.0 xanchor 1.0
        parallel:
            easein 1.0 alpha 0.0
        parallel:
            easein 1.0 xanchor 0.0

transform swipeLeft:
    subpixel True
    yalign .5
    on show, replace:
        alpha 0.0 xpos 100 # xzoom 0.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 xpos 0
    on hide, replaced:
        alpha 1.0
        parallel:
            easein 1.0 alpha 0.0
        parallel:
            easein 1.0 xpos -100

transform swipeUpDown:
    subpixel True
    xalign .5
    on show, replace:
        alpha 0.0 ypos -100
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 ypos 0
    on hide, replaced:
        alpha 1.0
        parallel:
            easein 1.0 alpha 0.0
        parallel:
            easein 1.0 ypos -100
