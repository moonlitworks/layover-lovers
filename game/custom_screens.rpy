#
# STYLES
#
style menu_text:
    color "#000"
    selected_color "#c62525"
    hover_color "#989aa0"
    font "fonts/Roboto-Condensed.ttf"

style map_text:
    color "#fff"
    hover_color "#989aa0"



#
# SCREENS
#
screen logo:
    fixed:
        at swipeUpDown
        add "logo.png":
            xalign 0.5 yalign 0.2

screen sky:
    add "images/title_bg.png"

screen titleToMain:
    fixed:
        at leftMenu
        textbutton "< Back to Main Menu":
            text_style "menu_text"
            text_font "fonts/Roboto-Condensed.ttf"
            align(0.05,0.1)
            action MainMenu(confirm=True)

screen returnbtn:
    fixed:
        at leftMenu
        textbutton "< Return":
            text_style "menu_text"
            align(0.05,0.9)
            action Return()

screen quitbtn:
    fixed:
        at leftMenu
        textbutton "< Quit":
            text_style "menu_text"
            align(0.05,0.9)
            action Quit()

screen registerbtn:
    fixed:
        at rightMenu
        textbutton "Register >":
            text_style "menu_text"
            align(0.95,0.9)
            action Start()

screen settingsbtn:
    fixed:
        at rightMenu
        textbutton "Settings >":
            text_style "menu_text"
            align(0.95,0.9)
            action ShowMenu("preferences")

screen loadbtn:
    fixed:
        at rightMenu
        textbutton "Save/Load >":
            text_style "menu_text"
            align(0.95,0.9)
            action ShowMenu('loadInGame')

screen prefsbtn:
    fixed:
        at rightMenu
        textbutton "Preferences >":
            text_style "menu_text"
            align(0.95,0.9)
            action ShowMenu('preferencesInGame')

screen about:
    tag menu
    use sky
    fixed:
        at topMenu
        text "Layover Lovers was originally a solo project for NaNoRenO 2019":
            style "menu_text"
            anchor(0.5,0.5)
            align(0.5,0.1)
        text "This has been revamped for official release":
            style "menu_text"
            anchor(0.5,0.5)
            align(0.5,0.15)
        
        vbox:
            anchor(0.5,0.5)
            align(0.5,0.5)
            spacing 5
            text "Story: Eyzi" style "menu_text" xalign 0.5
            text "Writer: Kyoki Chiho" style "menu_text" xalign 0.5
            text "Sprites/CG: YayaChann" style "menu_text" xalign 0.5
            text "Backgrounds: ThreeAngleWork" style "menu_text" xalign 0.5
            text "Logo: Eriko" style "menu_text" xalign 0.5
            text "UI: Re.Alice" style "menu_text" xalign 0.5
            text "Music (Departure): Mock Off" style "menu_text" xalign 0.5
            text "Music (Arrival): Eyzi" style "menu_text" xalign 0.5
            text "Sound (Plane): bolkmar" style "menu_text" xalign 0.5
    
    fixed:
        at bottomMenu
        text "Special thanks to Pytom":
            style "menu_text"
            size 18
            anchor(0.5,0.5)
            align(0.8,0.83)
        text "and his Ren'Py engine":
            style "menu_text"
            size 18
            anchor(0.5,0.5)
            align(0.8,0.88)




    use returnbtn

screen register:
    tag menu
    use sky
    fixed:
        at swipeUpDown
        add "ticket.png"

        text "Name of Passenger":
            style "menu_text"
            size 15
            align(0.2,0.37)
            xanchor 0.0
        input default "[name]":
            color "#c62525"
            xanchor 0.0
            length 12
            align(0.2,0.4)
            value VariableInputValue('name')

        text "Date":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.45,0.37)
        text "31MAR":
            style "menu_text"
            xanchor 0.0
            align(0.45,0.4)

        text "Time":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.6,0.37)
        text "20:00":
            style "menu_text"
            xanchor 0.0
            align(0.6,0.4)



        text "Sex":
            style "menu_text"
            size 15
            align(0.2,0.47)
            xanchor 0.0
        textbutton "Male":
            text_style "menu_text"
            xanchor 0.0
            align(0.2,0.5)
            action [Function(setSex,"Male"),SetVariable("sex","Male")]
        textbutton "Female":
            text_style "menu_text"
            xanchor 0.0
            align(0.27,0.5)
            action [Function(setSex,"Female"),SetVariable("sex","Female")]

        text "Flight":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.45,0.47)
        text "NANO19":
            style "menu_text"
            xanchor 0.0
            align(0.45,0.5)

        text "Seat":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.6,0.47)
        text "42A":
            style "menu_text"
            xanchor 0.0
            align(0.6,0.5)



        text "From":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.2,0.57)
        text "█ █ █ █ █ ":
            style "menu_text"
            font "DejaVuSans.ttf"
            xanchor 0.0
            align(0.2,0.6)

        text "Gate":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.6,0.57)
        text "N3":
            style "menu_text"
            xanchor 0.0
            align(0.6,0.6)



        text "To":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.2,0.67)
        text "█ █ █ █ █ ":
            style "menu_text"
            font "DejaVuSans.ttf"
            xanchor 0.0
            align(0.2,0.7)



        text "Name of Passenger":
            style "menu_text"
            size 15
            align(0.76,0.37)
            xanchor 0.0
        text "[name]":
            style "menu_text"
            align(0.76,0.4)
            xanchor 0.0

        text "Sex":
            style "menu_text"
            size 15
            align(0.76,0.47)
            xanchor 0.0
        text "[sex]":
            style "menu_text"
            align(0.76,0.5)
            xanchor 0.0

        text "Date":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.76,0.57)
        text "31MAR":
            style "menu_text"
            xanchor 0.0
            align(0.76,0.6)

        text "Time":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.85,0.57)
        text "20:00":
            style "menu_text"
            xanchor 0.0
            align(0.85,0.6)

        text "Flight":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.76,0.67)
        text "NANO19":
            style "menu_text"
            xanchor 0.0
            align(0.76,0.7)

        text "Seat":
            style "menu_text"
            xanchor 0.0
            size 15
            align(0.85,0.67)
        text "42A":
            style "menu_text"
            xanchor 0.0
            align(0.85,0.7)

    use returnbtn
    use registerbtn

screen saveInfo(passenger, sex):
    vbox:
        xpos 10
        yalign 0.3
        text "Name of Passenger":
            style "menu_text"
            size 15
    
        text "[passenger]":
            style "menu_text"

    vbox:
        xpos 10
        yalign 0.5
        text "Sex":
            style "menu_text"
            size 15
    
        text "[sex]":
            style "menu_text"

screen saveLoader(saved, saveSlot, saveName):
    if saved:
        textbutton "Load":
            text_style "menu_text"
            xalign 0.5
            yalign 0.8
            action Function(renpy.load, saveName)
        textbutton "Delete":
            text_style "menu_text"
            text_color "#f00"
            xalign 0.5
            yalign 0.9
            action Function(deleteTicket, saveSlot)
    else:
        text "No Saved Data":
            font "fonts/Roboto-Condensed.ttf"
            color "#f00"
            xalign 0.5
            yalign 0.9

screen saveSaver(saveSlot):
    textbutton "Save":
        text_style "menu_text"
        xalign 0.5
        yalign 0.7
        action Function(saveTicket, saveSlot)

screen load:
    tag menu
    use sky
    fixed:
        at topMenu

        frame:
            align(0.25,0.5)
            anchor(0.5, 0.5)
            xysize(232,420)
            background 'ticketload.png'
            use saveInfo(persistent.save1['name'], persistent.save1['sex'])
            use saveLoader(persistent.save1['saved'], 1, "ticket1")
        
        frame:
            align(0.5,0.5)
            anchor(0.5, 0.5)
            xysize(232,420)
            background 'ticketload.png'
            use saveInfo(persistent.save2['name'], persistent.save2['sex'])
            use saveLoader(persistent.save2['saved'], 2, "ticket2")

        frame:
            align(0.75,0.5)
            anchor(0.5, 0.5)
            xysize(232,420)
            background 'ticketload.png'
            use saveInfo(persistent.save3['name'], persistent.save3['sex'])
            use saveLoader(persistent.save3['saved'], 3, "ticket3")

    use returnbtn

screen loadInGame:
    tag menu
    add Solid("#fff5")
    fixed:
        at topMenu

        frame:
            align(0.25,0.5)
            anchor(0.5, 0.5)
            xysize(232,420)
            background 'ticketload.png'
            use saveInfo(persistent.save1['name'], persistent.save1['sex'])
            use saveSaver(1)
            use saveLoader(persistent.save1['saved'], 1, "ticket1")
        
        frame:
            align(0.5,0.5)
            anchor(0.5, 0.5)
            xysize(232,420)
            background 'ticketload.png'
            use saveInfo(persistent.save2['name'], persistent.save2['sex'])
            use saveSaver(2)
            use saveLoader(persistent.save2['saved'], 2, "ticket2")
        
        frame:
            align(0.75,0.5)
            anchor(0.5, 0.5)
            xysize(232,420)
            background 'ticketload.png'
            use saveInfo(persistent.save3['name'], persistent.save3['sex'])
            use saveSaver(3)
            use saveLoader(persistent.save3['saved'], 3, "ticket3")

    use returnbtn
    use prefsbtn
    use titleToMain

screen preferences:
    tag menu
    use sky
    fixed:
        at topMenu

        vbox:
            align(0.33,0.25)
            anchor(0.5,0.0)
            style_prefix "radio"
            label _("Display")
            textbutton _("Window") action Preference("display", "window") text_style "menu_text" 
            textbutton _("Fullscreen") action Preference("display", "fullscreen") text_style "menu_text"

        vbox:
            align(0.66,0.25)
            anchor(0.5,0.0)
            style_prefix "check"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")  text_style "menu_text"
            textbutton _("After Choices") action Preference("after choices", "toggle")  text_style "menu_text"
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))  text_style "menu_text"

        vbox:
            align(0.33,0.55)
            anchor(0.5,0.0)
            label _("Text Speed")
            bar value Preference("text speed") xmaximum 200
            label _("Auto-Forward Time")
            bar value Preference("auto-forward time") xmaximum 200

        vbox:
            align(0.66,0.55)
            anchor(0.5,0.0)
            if config.has_music:
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume") xmaximum 200
            if config.has_sound:
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume") xmaximum 200
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound) text_style "menu_text"

    use returnbtn

screen preferencesInGame:
    tag menu
    add Solid("#fff5")
    fixed:
        at topMenu

        vbox:
            align(0.33,0.25)
            anchor(0.5,0.0)
            style_prefix "radio"
            label _("Display")
            textbutton _("Window") action Preference("display", "window") text_style "menu_text"
            textbutton _("Fullscreen") action Preference("display", "fullscreen") text_style "menu_text" 

        vbox:
            align(0.66,0.25)
            anchor(0.5,0.0)
            style_prefix "check"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")  text_style "menu_text"
            textbutton _("After Choices") action Preference("after choices", "toggle")  text_style "menu_text"
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))  text_style "menu_text" 

        vbox:
            align(0.33,0.55)
            anchor(0.5,0.0)
            label _("Text Speed")
            bar value Preference("text speed") xmaximum 200
            label _("Auto-Forward Time")
            bar value Preference("auto-forward time") xmaximum 200

        vbox:
            align(0.66,0.55)
            anchor(0.5,0.0)
            if config.has_music:
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume") xmaximum 200
            if config.has_sound:
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume") xmaximum 200
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound) text_style "menu_text"

    use returnbtn
    use loadbtn
    use titleToMain

screen main_menu():
    tag menu
    use sky
    use logo
    fixed:
        at bottomMenu
        textbutton "New Passenger":
            text_style "menu_text"
            text_size 30
            align(0.5,0.6)
            action ShowMenu("register")
        textbutton "Existing Passenger":
            text_style "menu_text"
            text_size 20
            align(0.5,0.7)
            action ShowMenu("load")
        textbutton "About":
            text_style "menu_text"
            text_size 20
            align(0.5,0.75)
            action ShowMenu("about")
    use quitbtn
    use settingsbtn

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) text_font "fonts/Roboto-Condensed.ttf"
            textbutton _("Auto") action Preference("auto-forward", "toggle") text_font "fonts/Roboto-Condensed.ttf"
            textbutton _("Save/Load") action ShowMenu('loadInGame') text_font "fonts/Roboto-Condensed.ttf"
            textbutton _("Prefs") action ShowMenu('preferencesInGame') text_font "fonts/Roboto-Condensed.ttf"
