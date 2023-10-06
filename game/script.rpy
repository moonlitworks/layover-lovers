define guyUnknown = Character("???",color="#ffffff",image="guy")
define girlUnknown = Character("???",color="#ffffff",image="girl")
define dj = Character("DJ",color="#ffffff")
define guy = Character("[guyName]",color="#ffffff",image="guy")
define girl = Character("[girlName]",color="#ffffff",image="girl")
define attendant = Character("Airport Attendant",color="#ffffff")
define pa = Character("PA System",color="#ffffff")
image white = Solid("#fff")

# label splashscreen:
#     play audio "sounds/plane.ogg"
#     scene splashscreen with Dissolve(2)
#     $ renpy.pause(3.0)
#     scene black with Dissolve(2)
#     return

label start:
    # init names
    if sex.lower()=="male":
        if name!="":
            $ guyName = name
            $ guy = Character("[name]")
    else:
        if name!="":
            $ girlName = name
            $ girl = Character("[name]")

    # story
    $ callLabel('intro')
    $ callLabel('encounter')
    $ callLabel('interlude')
    $ callLabel('coffee')
    $ callLabel('bonding')
    $ callLabel('departure')
    $ callLabel('ending')
    return
