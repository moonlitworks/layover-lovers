init python:
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('K_MENU')
    config.keymap['game_menu'].remove('mouseup_3')

    girlName = "Lucia"
    guyName = "Dan"

    name = guyName
    sex = "Male"

    if persistent.save1 is None:
        persistent.save1={
            'saved':False,
            'name':'',
            'sex':''
        }

    if persistent.save2 is None:
        persistent.save2={
            'saved':False,
            'name':'',
            'sex':''
        }

    if persistent.save3 is None:
        persistent.save3={
            'saved':False,
            'name':'',
            'sex':''
        }

    def setSex(newSex):
        global name
        if newSex=="Male" and name==girlName:
            name=guyName
        if newSex=="Female" and name==guyName:
            name=girlName

    def saveTicket(slot):
        renpy.save('ticket'+str(slot))
        if slot==1:
            persistent.save1={
                'saved':True,
                'name':name,
                'sex':sex
            }
        elif slot==2:
            persistent.save2={
                'saved':True,
                'name':name,
                'sex':sex
            }
        elif slot==3:
            persistent.save3={
                'saved':True,
                'name':name,
                'sex':sex
            }

    def deleteTicket(slot):
        renpy.unlink_save('ticket'+str(slot))
        if slot==1:
            persistent.save1={
                'saved':False,
                'name':'',
                'sex':''
            }
        elif slot==2:
            persistent.save2={
                'saved':False,
                'name':'',
                'sex':''
            }
        elif slot==3:
            persistent.save3={
                'saved':False,
                'name':'',
                'sex':''
            }

    def callLabel(label):
        renpy.call("".join([sex.lower(),'_',label]))
