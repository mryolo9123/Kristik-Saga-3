# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    renpy.music.register_channel("backgroundSFX", "sfx", loop=True)
    renpy.music.register_channel("backgroundmusic", "music", loop=True)
    renpy.music.register_channel("backgroundSFXnoloop", "sfx", loop=False)
init:
    $ style.button.activate_sound = 'button.ogg'
    $ style.imagemap.activate_sound = 'button.ogg'

    
    #######################################################
    $ persistent.meetingKyle = False
    $ persistent.meetAsami = False
    $ persistent.touchedAsami = 0
    $ persistent.MeetMichiko = False
    $ persistent.GoWithMichiko = 0 
    $ persistent.flirtmichiko = False
    $ persistent.michikoFlirtType = 0
    $ persistent.flirtAsami = False
    $ persistent.asamiFlirtType = 0
    $ persistent.flirtboth = False
    $ persistent.chapter1 = True
    $ persistent.chapter2 = False
    $ persistent.chapter3 = False
    $ persistent.chapter4 = False
    $ persistent.asami = False
    $ persistent.michiko = False
    $ persistent.chungcha = False
    $ persistent.huiyoung = False
    $ persistent.hannah = False
    $ persistent.chiyoko = False
    $ persistent.chinaone = False
    $ persistent.chintwo = False
    ########################## DELETE ON RELEASE ^^^^^^^
define e = Character("")
define kris = Character("Kristik", color="#FFFFFF")
define krismind = Character("")
define mom = Character("Mom", color="#FFFFFF")
define gui.name_text_outlines = [ (2, "#000000", 0, 0) ]
define gui.dialogue_text_outlines = [ (2, "#000000", 0, 0) ]
define kyle = Character("Kyle", color="#FFFFFF")
define cade = Character("Cade", color="#FFFFFF")
define json = Character("Jason", color="#FFFFFF")
define kev = Character("Kevin", color="#FFFFFF")
define bill = Character("Bill", color="#FFFFFF")
define hung = Character("Hung", color="#FFFFFF")
define cntr = Character("Air Traffic and Mission Coordinator Controller", color="#FFFFFF")
define aar = Character("Aaron", color="#FFFFFF")
define pa = Character("PA System", color="#FFFFFF")
define wes = Character("Wesley", color="#FFFFFF")
define mys = Character("???", color="#FFFFFF")
define dev = Character("sysadmin", color="#FFFFFF")
define oth = Character("Others", color="#FFFFFF")
define rx7 = Character("Cocky RX-7 Owner", color="#FFFFFF")
define waiter = Character("Waitress", color="#FFFFFF")
define silver = Character("Salty Silver", color="#FFFFFF")
define fade = Fade(1, 0.3, 1)
define dissolve = Dissolve(1.0)
define att1 = Character("Flight Attendant 1", color="#FFFFFF")
define att2 = Character("Flight Attendant 2", color="#FFFFFF")
define girl1 = Character("あさみ", color="#FFFFFF", who_font = 'msgothic.ttc')
define girl2 = Character("みちこ", color="#FFFFFF", who_font = 'msgothic.ttc')
define girl3 = Character("김충차", color="#FFFFFF", who_font = 'malgunbd.ttf')
define girl4 = Character("박희영", color="#FFFFFF", who_font = 'malgunbd.ttf')
define girl5 = Character("Hannah Schröder", color="#FFFFFF")
define girl6 = Character("ちよこ", color="#FFFFFF", who_font = 'msgothic.ttc')
define girl7 = Character("袁昌英", color="#FFFFFF", who_font = 'simhei.ttf')
define girl8 = Character("冼东妹", color="#FFFFFF", who_font = 'simhei.ttf')
define clerk1 = Character("Indian Clerk", color="#FFFFFF")
define worker1 = Character("Worker", color="#FFFFFF")
define mahneet = Character("Mahneet Sidhu", color="#FFFFFF")
define bystander1 = Character("Bystander 1", color="#FFFFFF")
define bystander2 = Character("Bystander 2", color="#FFFFFF")
define rem = Character("[COPYRIGHTED MATERIAL]", color="#FFFFFF")
define pil = Character("Main Captain 1", color="#FFFFFF")
define firo = Character("Main First Officer 1", color="#FFFFFF")
define gui.choice_text_outlines = [ (2, "#000000", 0, 0) ]
image fire = Movie(channel="movie", play="movies/fires_Trim.ogv")
image end = Movie(size=(1280,720), channel="movie", play="movies/endstat.ogv")
image menuA = Movie(size=(1280,720), channel="movie", play="movies/Untitled.ogv")
image america = Movie(size=(1280,720), channel="movie", play="movies/usaflag.ogv")
image transition1 = Movie(size=(1280,720), channel="movie", play="movies/transitionone.ogv")
define audio.doorslamclose = "audio/doorslamclose.ogg"
define audio.doorslamopen = "audio/doorslamopen.ogg"
define audio.bedsheet = "audio/bedsheetrustle.ogg"
define audio.scnightambience = "audio/scnightamb.ogg"
define audio.airportamb = "audio/airamb.ogg"
define ranguy1 = Character("Random Guy 1", color="#FFFFFF")
define ranguy2 = Character("Random Guy 2", color="#FFFFFF")
define rangir1 = Character("Random Girl 1", color="#FFFFFF")
define rangir2 = Character("Random Girl 2", color="#FFFFFF")
image asamstat = ParameterizedText(xalign=0.17, yalign=0.40)
image michstat = ParameterizedText(xalign=0.17, yalign=0.48)
image chungstat = ParameterizedText(xalign=0.17, yalign=0.56)
image huistat = ParameterizedText(xalign=0.17, yalign=0.65)
image hannahstat = ParameterizedText(xalign=0.34, yalign=0.73)
image chiyokostat = ParameterizedText(xalign=0.29, yalign=0.805)
image chin1stat = ParameterizedText(xalign=0.17, yalign=0.89)
image chin2stat = ParameterizedText(xalign=0.17, yalign=0.97)
##################################################################

#default persistent.meetingKyle = False
#default persistent.meetAsami = False
#default persistent.touchedAsami = 0
#default persistent.MeetMichiko = False
#default pesistent.chapter1 = False
#default pesistent.chapter2 = False
#default pesistent.chapter3 = False
#default pesistent.chapter4 = False
#default persistent.asami = False
#default persistent.michiko = False
#default persistent.chungcha = False
#default persistent.huiyoung = False
#default persistent.hannah = False
#default persistent.chiyoko = False
#default persistent.chinaone = False
#default persistent.chintwo = False
############### persistent data. DO NOT TOUCH. #REMOVE HASHTAG ON REAL RELEASE
#############################################################

default persistent.completedgame = 0
style default:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
# The game starts here.
transform bgslide:
    xalign 0.5 yalign 0.99
    linear 1 xalign 0.0
transform bgbackslide:
    xalign 0.0 yalign 0.99
    linear 1 xalign 0.8
transform slideleft2ppl:
    xalign 1.0 yalign 1.0
    linear 0.2 xalign -27.0
transform slideright2ppl:
    xalign 0.6 yalign 0.0
    linear 0.3 xalign 0.8
style japantext:
    font "YuGothM.ttc"
    language "japanese-loose"
style chinesetext:
    font "simhei.ttf"
style koreatext:
    font "malgunbd.ttf"
    language "korean-with-spaces"
screen disable_Lmouse():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_SELECT" action NullAction()
#label splashscreen:
    #scene bg black
    #show splash
    #$ renpy.transition(Dissolve(1.0)) 
    #$ renpy.pause(2, hard=True)
    #hide splash
    #$ renpy.transition(Dissolve(1.0)) 
    #$ renpy.pause(2, hard=True)
    #show disclaimer
    #$ renpy.transition(Dissolve(1.0)) 
    #$ renpy.pause(4, hard=True)
    #hide disclaimer
    #$ renpy.transition(Dissolve(1.0)) 
    #$ renpy.pause(2, hard=True)
    #return 
label main_menu:
    with None
    $ renpy.transition(dissolve)
    show menuA
    $ renpy.pause(2, hard=True)    
    jump main_menu_screen
    hide menuA
label start:
    stop music fadeout 2.0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ meetingKyle = 0
    $ meetAsami = 0 
    $ touchAsami = 0

    #########################################################################################################################################################################################################
    $ _skipping = True ##################################################################################################<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<CHANGE TO FALSE IN FINAL VERSION
    #########################################################################################################################################################################################################

    $ persistent.chapter1 = True
    scene bg black
    image girlnorm_reg = "ssuo0101.png"
    image girlnorm_mad = "ssuo0106.png"
    image girlnorm_lookaway = "ssuo0110.png"
    image girlnorm_emb = "ssuo0105.png"
    image girlnorm_emblookatplyr = "ssuo0124.png"
    image girlnorm_embmad = "ssuo0121.png"
    image girlnorm:
        "ssuo0101.png"
    image girlmad:
        "ssuo0106.png"
    image girllookaway:
        "ssuo0110.png"
    image girlemb:
        "ssuo0105.png"
    image girlemblookatplyr:
        "ssuo0124.png"
    image girlembmad:
        "ssuo0121.png"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    $ pointsGirl1 = 0
    $ pointsGirl2 = 0
    $ pointsGirl3 = 0
    $ pointsGirl4 = 0
    $ pointsGirl5 = 0
    $ pointsGirl6 = 0
    $ pointsGirl7 = 0
    $ pointsGirl8 = 0
    # These display lines of dialogue.
    e "Kristik...."

    e "Wake up kristik!!!"

    scene bg bed
    with fade
    play backgroundmusic "audio/Sunshine_Samba.mp3"
    mom "Kristik its literally 9 AM get yo ass off the bed "

    mom "Seriously what's with these tissues on the ground?"

    kris "Uhhhh..... Nothing!!! This is totally not nut or anything!!"

    mom "-_- goddamnit Kristik you need to stop jacking off to indian hentai"

    kris "Fuck you mom! I love jacking off!!"

    krismind "Jesus christ this woman is unbearable. And that woman is my mom LOL!!!"
    ##################$ pointsGirl1 = pointsGirl1 + 1 
    ##################kris "Point test [pointsGirl1]"       <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BASIC POINT SYSTEM TEST 

    krismind "I guess I'll just get up then..."
    window hide
    play sound bedsheet
    $ renpy.pause(2, hard=True)
    ###############################################################<<<<<<<<<<<<<<<ADD SOUND FOR RUSTLING BEDSHEETS <<<DONE
    window show
    mom "Oh and by the way, the internet is getting cut off until tomorrow morning"
    stop backgroundmusic fadeout 0.0
    play backgroundSFXnoloop "audio/DJ Record Scratch Sound Effect - copyright free sound effects.mp3" 
    krismind "WHAAAAAAAT???"
    play backgroundmusic "audio/As Tall As Lions - Maybe I'm Just Tired.mp3"

    kris "NOOOOOOOO!!! HOW WILL I JACK OFF TO THE HOTTEST INDIAN GIRLS!?!?!?!?"
    kris "MY LIFE... IS RUINED!!!"
    kris "I CANT LIVE ON THIS WORLD ANYMORE!"
    kris "THIS WORLD ISNT WORTH LIVING!"
    kris "IM SORRY MOTHER... BUT IM SURE YOU WOULD UNDERSTAND."
    kris "THIS IS SIMPLY TREASONOUS!"
    stop backgroundmusic fadeout 0.0
    mom "LMAO!!!! JK LOOK AT THIS DOOD!!!! XDDD"

    kris "..."
    
    kris "WHAT??!?!?!?!?!"
    kris "YOU MEAN TO TELL ME THAT SHIT WAS A JOKE!!!??!!!"
    play backgroundmusic "audio/The Price is Right theme song.mp3"
    mom "CONGRADULATIONS!!! YOU GET THE AWARD FOR MOST OVERREACTIVE RESPONSE FOR INTERNET CUTTING OUT!!!"
    mom "LMAOOOOOO!!!!!!!! THE WAY YOU REACTED WAS SO FUCKING FUNNY!!!!"

    kris "SHUT THE FUCK UP MOM!!!! AND TURN OFF THAT DAMN MUSIC!!!"
    window hide
    play backgroundSFXnoloop "audio/eject.ogg"
    stop backgroundmusic fadeout 0.0
    $ renpy.pause(2, hard=True)
    window show
    krismind "goddamnit my mom is such a whore..."

    krismind ". . ."

    krismind "It had been 6 years since the battle between me, Bill, Callin, Kyle, Cade, Jason, and Kevin."

    krismind "...and it also has been 6 years since i drank Bill's piss and died...."

    krismind "It doesn't really matter anyways... My hot girlfriend came and resurrected me!!!!"

    krismind "and then she left me.... OOF"

    krismind "(im kinda feeling like nutting rn... Should i???)"

    play audio "audio/popup.ogg"
    menu:
        "Nut to Ex-Girlfriend":
            play audio "audio/choiceconfirmed.ogg"
            jump j1
        "Skip nutting":
            play audio "audio/choiceconfirmed.ogg"
            jump j2
    label j1:
        kris "eh why not? lets nut boi!!!!!"
        mom "what? You're gonna nut?? Well whatever, IDC."
        kris "Mom get the fuck out of here!"
        kris "I need to nut!!! PRONTO!!!"
        window hide
        jump sc1
    label j2:
        kris "Nah... skip nutting. I have to go to SCHOOL! BOI!!!!!!!!!!!"
        window hide
        jump sc1
    label sc1:
        window show
        scene bg sc
        $ renpy.transition(Fade(1, 0.3, 1)) 
        $ renpy.pause(2, hard=True)
        #play sound scnightambience loop
       # play backgroundSFX "audio/scnightamb.ogg"
        ###############################################################<<<<<<<<<<<<<<<ADD AMBIENT BACKGROUND NOISE <<<DONE
        play backgroundmusic "audio/bgmusic7.ogg"
        kris "Hah... at school now."
        kris "WAIT. WTF??? "
        kris "ITS LITERALLY 9 PM NOT 9 AM!"
        kris "GODDAMNIT MOM YOU FUCKING TROLL!"
        kris "wait how did i not notice that when i was coming here...? well whatever might as well stalk some people out here"
        stop backgroundmusic fadeout 1.0
        show kylenorm
        $ renpy.transition(Dissolve(1.0)) 
        $ renpy.pause(2, hard=True)
        kris "..."
        stop backgroundmusic fadeout 1.0
        mys "..."
        kris "KYLE????!!!"
        kyle "KRISTIK???????!!"
        show kylenorm
        hide kylenorm
        show kylemad
        play backgroundmusic "audio/bgmusic9.ogg"
        kris "WHAT THE FUCK ARE YOU DOING HERE???"
        kyle "I COULD ASK THE SAME THING ABOUT YOU!"
        stop backgroundmusic fadeout 1.0
        window hide
        $ quick_menu = False
        scene bg black
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True)
        scene bg sc
        window show
        $ quick_menu = True
        hide kylemad
        show kylenorm
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True)
        play backgroundmusic "audio/randomusic.ogg"
        $ persistent.meetingKyle = True
        label kyle:
            window show
            hide kylenorm
            $ quick_menu = True
            scene bg sc
            show kylenorm
            kris "Since when do you go to independence? I thought you went to a shittier school AFAIK"
            kyle "Fuck you dude its not that bad you Nig-"
            kris "woah there buddy if you finish that im about to cancel you"
            kyle "shit... whatever.... "
            kyle "Anyways... How the FUCK are you alive? You died by drinking Bill's piss and Obama came to congradulate us."
            kyle "You telling me Obama had to get shot by Xi JinPing for no reason?? We all cried and looked at the sunset."
            kris "Yea i know that..."
            kyle "How???? You were dead by the time that happened...."
            kris "O i just saw the rest of the story at Hung's Hobo Nước Mắm. Server is at https://discord.gg/9NcD7S6"
            kyle "wut??? what are you talking about??"
            kris "nvm..."
            kris "Just curious, what happened after that? I remember some kid named Helixiate or whatever complained about not having end credits."
            kyle "Uhhh nothing much. We just went to bobaholics after that. Then we went home."
            kris "What??? But AFAIK arwasairl and KIDOMARU didn't model your guys' houses in ROBLOX studio..."
            kyle "tf are you talking about? are you high on curry cocaine?"
            kris "nvm again..."
            jump sc4
        label sc4:
            kris "ay so uh where is the rest of the gang?"
            kyle "Huh? oh they're at San Jose right now."
            kris "no shit sherlock"
            kris "I mean where are they"
            kyle "Well how would I know? "
            kyle "Jason is probably at the bar passed out again.... hes been drinking alot recently."
            kris "(WTF???)"
            stop backgroundmusic fadeout 1.0
            kris "For what reason?"
            play backgroundmusic "audio/bgmusic10.ogg"
            kyle "Well Jason's been under alot of stress recently. He's been having problems with the other guys so hes been smoking Marlboro Golds and drinking Heineken and Budweiser all day."
            kyle "Sometimes he likes to hit a bong with that crackhead Hung.... he smoked weed with him too."
            kyle "I went to Jason's and Hung's parties once. They disable all the smoke alarms so their smokefest doesnt get stopped by the fire department."
            kyle "They also invite strippers while smoking weed and hung eventually just fucks them all. Jason is the one who usually outsources his cocaine and brings some."
            stop backgroundmusic
            play backgroundmusic "audio/bgmusic9.ogg"
            kyle "Jesus that day was wild!"
            kyle "Although Jason doesnt do cocaine anymore. I think he just drinks now. He also stopped smoking so I guess thats good."
            kris "Damn wtf?? Where did all this stress come from?"
            kyle "Most likely his work."

            kris "(jesus... well i better change the subject...)"
            kris "do you know any hot chicks i could bang?"
            kyle "No, why would I?"
            kyle "Just invite some strippers to your house."
            kris "No not a whore. I mean like a hot pure girl that doesnt go around getting fucked by every dick she sees."
            stop backgroundmusic fadeout 1.0
            stop backgroundSFX fadeout 1.0
            hide kylenorm
            show fire
            hide bg sc
            ###############################################################<<<<<<<<<<<<<<<ADD FIRE NOISE
            show kylebruh
            kyle "well IMO my gf pretty hot but no way in hell i would let you bang her. i will literally slit your lungs and feed it to you if you do such thing."
            hide fire
            hide kylebruh
            show bg sc
            show kylenorm
            play backgroundmusic "audio/bgmusic6.ogg"
            kris "goddamn you gotta chill... i wasnt even talking about banging your gf"
            kyle "well why are you asking me? i have a girlfriend already why would i be actively looking for girls?"
            kris "idk shut up okay i didnt think about it that hard"
            kyle "you hardly ever think at all"
            kris "-_-"
            kris "well do you have a friend that knows a bitch?"
            kyle "if youre gonna call your future girlfriend a bitch then dont expect any coochie on yo dick"
            kris "whatever... ill find a girl MYSELF."
            kyle "Haha..."
            kyle "HAHAHAHAHAHA"
            kyle "AHAHAHAHAHAHAHAHAHHAHAHAH!!!"
            kyle "youre so fucking funny lmao"
            kris "i wasnt telling a joke wdym"
            kyle "haha ok joker"
            kyle "Well I kinda gotta go somwehere."
            kris "Where are you going?"
            kyle "Im gonna go to Orchard school. I need to put spray some graffiti on the wall-ball courts."
            kris "Why???"
            kyle "Well I and a few other people have formed a clan so we're just marking our territory."
            kris "That shits illegal!!"
            kyle "Who cares?"
            kyle "Whatever im going."
            kris "I guess ill go too..."
            window hide
            $ quick_menu = False
            stop backgroundmusic fadeout 1.0
            scene bg black
            hide kylenorm
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(1, hard=True)
            show transition1
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(6, hard=True)


            scene bg black
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(1, hard=True)

            scene bg sj
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(1, hard=True)
            show kylenorm
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(1, hard=True)
            stop backgroundSFX fadeout 1.0
            ###############################################################<<<<<<<<<<<<<<<ADD BACKGROUND NOISE
            play backgroundmusic "audio/bgmusic7.ogg"
            $ quick_menu = True
            window show
            kyle "well we're here"
            kris "yea"
            kyle "Right i brought some spray paint."
            kris "Dude this shit is illegal though!"
            kyle "Do i look like i care?"
            stop backgroundmusic
            play backgroundmusic "audio/US National Anthem Earrape.mp3"
            hide kylenorm
            show america
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(0.2, hard=True)
            show kylenorm
            kyle "I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in secret raids on Al-Quaeda, and I have over 300 confirmed kills."
            kyle "I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target."
            kyle "I will wipe you out with precision the likes of which has never been seen before on this Earth, mark my words. You think you can get away with saying shit to me?"
            hide america
            stop backgroundmusic
            play backgroundSFXnoloop "audio/DJ Record Scratch Sound Effect - copyright free sound effects.mp3" 
            kris "ok literally stop with the navy seals copypasta i heard this shit already like 5,000,000 times"
            play backgroundmusic "audio/bgmusic9.ogg"
            kyle "make it 5,000,001 times"
            kris "-_-"
            kris "im tried of hearing that shit...."
            kris "anyways im bored, wanna do something?"
            kyle "why? you think we're still your friends?"
            kyle "you literally tried to kill us at the police station and when we were invading your base"
            kris "hey thats not the full story"
            kris "i obviously wouldve done something if youre just gonna raid my base"
            kris "and i only tried to stab you guys at the police station cause YOU guys raided my house and took me into prison"
            kris "then Aaron came with an F/A-18C and blew the whole shit up with AIM-9X sidewinders"
            kris "so of COURSE im gonna be mad"
            kyle "why would you kill us tho?? shouldnt you be killing Aaron?"
            kris "well he wasn't in Kristik Saga 1 or Kristik Saga 2 so i didnt have much to do"
            kyle "i have no idea what youre saying but ok"
            stop backgroundmusic fadeout 1.0
            label asami:
                window show
                hide kylenorm
                $ quick_menu = True
                scene bg sj
                show kylenorm
                $ persistent.meetAsami = True
                mys "Hey"
                krismind "(Who tf was that??)"
                hide kylenorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                play backgroundmusic "audio/bgmusic3.ogg"
                show girlnorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                mys "Do you guys know where N37°32 57.1 E126°57 35.7 is?"
                hide girlnorm
                #$ renpy.transition(Dissolve(0.3))
                #$ renpy.pause(0.2, hard=True)
                show kylenorm
                #$ renpy.transition(Dissolve(0.3))
                #$ renpy.pause(0.2, hard=True)
                kyle "Who are YOU?"
                kyle "And btw, why do the girls look different from guys?"
                kris "yo ITS A GIRL!! OMG!!"
                kyle "idc i have coochie kys"
                kris ".-."
                ####################################################################################################################################kris "{cps=40}FOR INTITAL D SCENES.{/cps}{p=1.0}{nw}"
                kris "ay imma talk to her"
                kyle "lmao ok sure you gonna fail tho"
                hide kylenorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                show girlnorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                mys "..."
                kris "hey babyyyyyyy how you doin????"
                kris "so uh... wanna get out of here or smth??"
                hide girlnorm
                show girlmad
                mys "Huh???"
                kris "so uh... erm... yea  so uh.."
                hide girlmad
                $ renpy.transition(Dissolve(0.4))
                $ renpy.pause(0.3, hard=True)
                show kylenorm
                $ renpy.transition(Dissolve(0.4))
                $ renpy.pause(0.3, hard=True)
                stop backgroundmusic
                play backgroundmusic "audio/bgmusic1.ogg"
                kris "goddamnit bruh i cant do it"
                hide kylenorm
                $ renpy.transition(Dissolve(0.2))
                show kylebruh
                $ renpy.transition(Dissolve(0.2))
                kyle "look at this dude"
                kris "yoo pleeeeeeeeeeaaaase give me advice yoo!! PLSSS"
                hide kylebruh
                $ renpy.transition(Dissolve(0.3))
                #with irisin
                $ renpy.pause(0.3, hard=True)
                show girllookaway
                $ renpy.transition(Dissolve(0.3))
                $ renpy.pause(0.3, hard=True)
                mys "Um... Yeah, I think I should go..."
                krismind "(Fuck! Shit bruh why am I such a retard?)"
                kris "oh yea... hahahaaaaaaaaaaaaaaaaaaaaaaaaaa....... you look like a busy person.."
                hide girllookaway
                show girlmad
                mys "Why are you speaking so weird?"
                play backgroundSFXnoloop "audio/lol.wav"
                krismind "(OOF)"
                krismind "(self confidence destroyed)"
                kris "Uhm, yea... UHHHHH...."
                mys "Yea... I'm going to go.."
                stop backgroundmusic fadeout 1.0
                hide girlmad
                $ renpy.transition(Dissolve(0.3))
                $ renpy.pause(0.3, hard=True)
                krismind "..."
                show kyledis
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                play backgroundmusic "audio/bgmusic2.ogg"
                kyle "dude... that was so bad..."
                kyle "im gonna die of cringe over here"
                kris "Shut the fuck up."
                hide kyledis
                $ renpy.transition(Dissolve(0.2))
                show kylebruh
                $ renpy.transition(Dissolve(0.2))
                kyle "WTF LMAO!!!"
                kyle "YOU HAVE A BONER!!!"
                kris "AY!! SHUT UP WHY ARE YOU YELLING THAT OUT LOUD??"
                hide kylebruh
                $ renpy.transition(Dissolve(0.2))
                show kylemad
                $ renpy.transition(Dissolve(0.2))
                kyle "DONT TELL ME TO SHUT UP!!!! YOU NOOB!!"
                kris "WDYM YOURE THE ONE WHOS YAPPING OUT LOUD I HAVE A BONER!!"
                hide kylemad
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(0.3, hard=True)
                window hide
                show bg sj at bgslide
                $ renpy.pause(1.5, hard=True)
                #$ renpy.transition(Dissolve(0.6))
                #$ renpy.pause(1, hard=True)
                window show
                show girlemb
                $ renpy.transition(Dissolve(0.4))
                mys "..."
                krismind "(... I thought she had to go? Why does she look embarrassed?)"
                show girlemblookatplyr
                krismind "(...)"
                kris "Uh....."
                show girlembmad
                mys "W-What are you staring at? You idiot!"
                krismind "????????"
                krismind "(Why is she suddenly acting like this????)"
                hide girlembmad
                show girlemblookatplyr
                kris "Hey you okay? Your face is super red."
                hide girlemblookatplyr
                show girlembmad
                mys "Shut up! I didn't ask you!"
                e "!!!!!"
                krismind "(shit... if i say anything more i might become a virgin forever...)"
                krismind "(i gotta do something)"
                window hide
                play audio "audio/popup.ogg"
            menu:
                "Go up to her":
                    play audio "audio/choiceconfirmed.ogg"
                    $ persistent.touchedAsami = 2
                    jump l1
                "Walk away":
                    play audio "audio/choiceconfirmed.ogg"
                    if persistent.touchedAsami > 0:
                        $ persistent.touchedAsami = 3
                    else:
                        $ persistent.touchedAsami = 1
                    jump l2 

        label l1:
            window show
            hide girlembmad
            $ quick_menu = True
            scene bg sj
            show girlembmad
            hide girlemb
            kris "Hey are you sick? What's wrong with you?"
            $ pointsGirl1 += 1
            mys "Nothing is wrong!!! Don't-"
            hide girlembmad
            show girlemblookatplyr
            kris "Hmmm you don't seem to have a fever..."
            mys "..."
            hide girlemblookatplyr
            show girlemb
            mys "Nothing..."
            mys "W-Well I'm going to go now.... "
            window hide
            hide girlemb 
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(2, hard=True)
            window show
            krismind "(What was that about?)"
            window hide
            show bg sj at bgbackslide
            $ renpy.pause(1.5, hard=True)
            window show
            show kylebruh
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(0.3, hard=True)
            stop backgroundmusic fadeout 1.0
            kyle "...."
            hide kylebruh
            show kylemad
            play backgroundSFX "audio/bgmusic1.ogg"
            kyle "WHAT THE FUCK DUDE???"
            kris "??????"
            kris "What??"
            kyle "ARE YOU A RETARD?"
            kyle "SHE CLEARLY HAS INTERESTS IN YOU!"
            kris "What makes you say that?"
            hide kylemad
            show kylebruh
            kyle "Omg... fucking blockhead..."
            hide kylebruh
            show kylemad
            kyle "YOU DIDNT EVEN ASK HER NAME OR ANYTHING!"
            hide kylemad
            show kylebruh
            kyle "You're so fucking lucky she likes you... otherwise you just touched her"
            kris "Shit that sounds bad... Wait how do YOU know HUH??"
            kyle "..."
            hide kylebruh
            show kylemad
            kyle "I'M OUT. I GIVE UP WITH THIS SHIT"
            kris "WAIT!! wtf..."
            stop backgroundSFX fadeout 1.0
            hide kylemad
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1.2, hard=True)
            krismind "tf was he on?"
            window hide 
            $ quick_menu = False
            jump u1
        label l2:
            window show
            hide girlembmad
            $ quick_menu = True
            scene bg sj
            show girlembmad
            hide girlemb
            kris "Yeah, nevermind."
            kris "Well I'll be going."
            hide girlembmad
            show girlemblookatplyr
            mys "O-Oh..."
            hide girlemblookatplyr
            show girlemb
            mys "Well... bye then..."
            krismind "???"
            krismind "(...why does it feel like i've done something wrong?)"
            window hide 
            $ quick_menu = False
            jump u1
        label u1:
            ###############################################################<<<<<<<<<<<<<<<ADD OUTSIDE NOISE
            scene bg hs
            with fade
            $ renpy.pause(1.2, hard=True)
            scene bg room
            with fade
            window show
            $ quick_menu = True
            play backgroundmusic "audio/bgmusic4.ogg"
            kris "ah..."
            mom "What was that noise? Are you nutting again?"
            kris "NO MOM IM NOT IM JUST BREATHING STFU"

            kris "always thinking im nutting..."
            mom "Well youe father loved to nut alot so im not surprised if you got that trait."
            kris "MOM!!! TMI!!! I DID NOT NEED TO KNOW THAT!!!"
            play sound doorslamclose
            krismind "(Jesus... shes so annoying...)"
            kris "Wtf was kyle on today? he seemed a bit weird."
            kris "Not only that... but that girl...."
            kris "That girl at school... she was weird..."
            stop backgroundmusic 
            play sound doorslamopen
            ###############################################################<<<<<<<<<<<<<<<ADD DOOR BUSTING SOUND
            mom "{cps=140}Why, was she not good cause she was a virgin?{/cps}"
            kris "MOM! WTF? WHY DID YOU COME BACK IN MY ROOM??? AND I DIDNT EVEN DO THAT YET! I BARELY TALKED TO HER!!"
            mom "Yeah, yeah, but make sure to bring this next time."
            kris "..."
            play backgroundmusic "audio/bgmusic9.ogg"
            kris "A CONDOM???"
            mom "Well we don't want you making children yet amirite"
            kris "well, you are right... NO WAIT STFU!!"
            mom "Haha well have fun"
            play sound doorslamclose
            kris "..."
            krismind "(Fuck you mom...)"
            kris "Well I'm kinda bored...."
            kris "Now that I think about it I literally have nothing to do besides jack off and play tekken or smth"
            stop backgroundmusic fadeout 1.0
            window hide
            play backgroundSFX "audio/ringtone.mp3"
            $ renpy.pause(2, hard=True)
            ###################################################################<<<<<<<<<<<<<<<<<<<<< ADD PHONE RINGTONE
            window show
            kris "Huh?"
            kris "Who the hell is calling me ?"
            krismind "(Damn its probably an indian scammer.... i don't know this number at all)"
            stop backgroundSFX
            kris "HeLlO I wiLl GiVe ThE CrEdiT CArD inForMatIon"
            mys "Yo! Long time no see"
            kris "Uh wrong number bye"
            mys "DONT HANG UP! It's me!!!"
            kris "If you just say its me how do you expect me to know who you are"
            mys "Just come to N30°35 19.4 E114°16 13.2"
            kris "Uhh.... no... "
            kris "For all i know you could come and shank me"
            mys "JUST GET HERE OR I MIGHT ACTUALLY SHANK YOU"
            kris "????? "
            krismind "(The hell is wrong with this guy?)"
            kris "Yeah... i have no idea who you are...."
            kris "and i looked up those coordinates and they're in Wuhan, China"
            kris "I think i'd rather get shanked than getting Coronavirus"
            mom "Hey Kristik someone is at the door for you!"
            kris "What??? I'm trying to tell some indian scammer to fuck off rn!"
            mom "Just get here! They want to see you!"
            krismind "(They?)"
            kris "Hey buddy I have somewhere to go so cya"
            mys "Alright we'll see you at your door"
            play backgroundSFXnoloop "audio/hangup.ogg"
            ##########################################################################<<<<<<<<<<<<<<<<<<<<<< ADD HANGUP NOISE
            krismind "(WOT???)"
            mom "HURRY UP AND GET HERE YOU TWAT"
            kris "JESUS CHRIST IM COMING!"
            krismind "(have they(?) actually come here to shank me???)"
            krismind "(well since this is my last chance at life i might as well bust a nut...)"
            window hide
            $ quick_menu = False
            play backgroundSFX "audio/fap.ogg"
            $ renpy.pause(3.2, hard=True)
            ##########################################################################<<<<<<<<<<<<<<<<<<<<<< ADD FAPPING NOISE
            play sound doorslamopen
            ###############################################################<<<<<<<<<<<<<<<ADD DOOR BUSTING SOUND <><<<<< DONE
            show kevinnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1.2, hard=True)
            window show
            $ quick_menu = True
            kev "Where the hell is kristik????"
            stop backgroundSFX
            ##<<<STOP FAPPING SOUND
            kev "..."
            kris "..."
            kris "Ummmm..."
            kev "Sorry wrong house"
            hide kevinnorm
            play sound doorslamclose
            kris "..."
            ###<<<<PLAY SOUND EFFECT IDK WHICH ONE YET
            kris"NOOO!!! WTFF??"
            kris "WHY DID THE PERSON WHO SAW ME MASTURBATE HAD TO BE A GUY???"
            kris "IM RUINED!!"
            play sound doorslamopen
            mom "jesus christ dude just clean up and come downstairs"
            mom "Remember the people who tried to capture you in Kristik Saga 2? Well they're all here"
            kris "O..."
            krismind "(damnit... so i just fapped for no reason....)"
            window hide
            ##<<< PLAY SINK RUNNING SOUND EFFECT
            scene downstairs
            ##<<< PLAY WALKING DOWNSTAIRS SOUND EFFECT
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            scene livingroom
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            window show
            krismind "(Damn... how the hell did they find my house?)"
            show kevindis 
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1.2, hard=True)
            play backgroundmusic "audio/bgmusic1.ogg"
            kev "BRO!!! THAT WAS SO NASTY!!!"
            krismind "(SHIT!! i better hide before they see me)"
            ##<<ADD SOME SORT OF RUSTLING NOISE 
            kev "HIS SMALL INDIAN CURRY MASALA WAS SO BAD IM LITERALLY CRYING!"
            hide kevindis
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show jasonbruh
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "You should've just knocked...."
            hide jasonbruh
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show kevinmad
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            kev "HOW WAS I SUPPOSED TO KNOW HE WAS NUTTING???"
            hide kevinmad
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            krismind "(SHIT!!! its way too awkward to come out now...)"
            mom "Hey guys. Want some cookies?"
            krismind "(WTF?? she never gave me cookies... ;-;)"
            show kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            kyle "HELL YA!! INDIAN COOKIES!!"
            ###<<<< ADD ROBLOX NOM NOM NOM SFX
            kyle "*nom nom nom*"
            hide kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            krismind "(i want some indian cookies!!!)"
            mom "Kristik come out behind the sofa and eat some"
            kris "Shit.... Fine..."
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "Did you hear us?"
            kris "Yea... i did..."
            show kevinnorm:
                xalign 20.0 yalign 1.0
            $ renpy.transition(Dissolve(0.4))
            show jasonnorm at slideleft2ppl
            kev "AY make sure you wash them hands cuz i aint eating no nut cookies"
            kris "Yea yea... i already did..."
            hide kevinnorm
            hide jasonnorm
            show kevinnorm
            kev "with soap?"
            kris "YEA YEA I DID NOW STFU AND LET ME EAT THIS COOKIE"
            play sound doorbell
            #<<<< PLAY DOORBELL
            e "..."
            mom "Oh someone's at the door"
            kris "I'll get it"
            window hide
            $ quick_menu = False
            stop backgroundmusic fadeout 1.0
            scene doorclose
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(1, hard=True)
            ##<<<PLAY DOOR OPEN sound
            play backgroundSFXnoloop "audio/dooropen.ogg"
            scene dooropen
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1, hard=True)
            show remnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            window show
            $ quick_menu = True
            kris "..."
            krismind "Ummmm WTF???"
            show remtalk
            rem "Hello."
            kris "What the f-{p=0.5}{nw}"
            rem "Have you seen 2020 Subaru WRX Premium CVT?"
            hide remtalk
            show remnorm
            krismind "(Who is she talking about??)"
            kris "Uh yeah i think hes in https://www.emiliamotors.com/"
            hide remnorm
            show remmad
            rem "Not... funny..."
            hide remmad 
            show remmadtlak
            rem "I'll kill you because of that joke."
            krismind "(EEK! Why is she so scary???)"
            hide remmadtlak
            show remmad
            kris "Alright well he isn't here so... "
            kris "BYE!!!"
            hide remmad
            play backgroundSFXnoloop "audio/doorclose.ogg"
            scene doorclose
            ###<<<<DOOR SLAM
            $ renpy.pause(2, hard=True)
            krismind "phew..."
            play sound doorbellexc
            $ renpy.pause(2, hard=True)
            ##<< PLAY OVEREXCESSIVE DOORBELL
            krismind "(AAAH!!!)"
            mom "What's going on over there?"
            kris "Nothing!!!"
            kris "its just an indian solicitor!"
            mom "what?"
            kris "wait! mom dont open the-"
            play backgroundSFXnoloop "audio/dooropen.ogg"
            ##<<<PLAY DOOR OPEN sound
            scene dooropen
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1, hard=True)
            show remmad
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            rem "..."
            mom "{=japantext}Oh its レムちゃん!! お元気ですか？{/=japantext}"
            hide remmmad
            show remtalk
            rem "{=japantext}ああ！！クリスティクのお母さんです！君に会って久しぶりだ。{/=japantext}"
            mom "{=japantext}大変申し訳ありません。これは私の息子クリスティクです。彼はとても礼儀正しくはない。{/=japantext}"
            krismind "(SINCE WHEN CAN MY MOM SPEAK JAPANESE???)"
            hide remtalk
            show remtalkhap
            rem "{=japantext}ああなるほど。彼は本当に迷惑です。彼を殺したい♥♥~~{/=japantext}"
            krismind "(somehow i think shes insulting me....)"
            hide remtalkhap
            show remnorm
            kris "Well you two talk i guess... I'll just catch up with the bros."
            window hide
            hide remmad
            hide remnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1, hard=True)
            scene livingroom
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            show kylenorm
            window show
            play backgroundmusic "audio/bgmusic4.ogg"
            kyle "i thought your mom was indian?"
            kris "she is but i didnt know she could speak japanese"
            kyle "youve got a weird ass family going on here"
            kris "Yea..."
            kris "anyways, what are you guys doing here?"
            kyle "Well...."
            hide kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "Bill, Callin, Welsey, and Aaron have all gone missing."
            kris "So???? Who cares???"
            kris "Aaron blew me up with AIM 9X sidewinders, i died when i drank Bill's piss, Callin beheaded my soldiers with a sword, and Wesley was..."
            kris "Welsey was never in the story... OOF"
            json "we only need them cause they owe us money"
            kris "What??? Why???"
            hide jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            kyle "You know that F/A-18C? Yea I actually rented that but Aaron never paid me back."
            kyle "Bill owed me money cause he promised that he would give me some after he accidentally pissed on me twice."
            kyle "Callin owes Jason money cause that sword was actually stolen from a Vietnam War museum and it was not easy heisting that place."
            kyle "And wesley..."
            kyle "Yea Wesley was useless...."
            kris "How much money are we talking here?"
            kyle "Ehhhh i'd say around $29 Million"
            kris "WTF???"
            kris "How do you even have that money?"
            kyle "Im rich duh"
            kris "Can you buy me a girlfriend then??"
            kyle "Fuck off."
            kris "Soooo how are we going to find them?"
            hide kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "Well we pinpointed their location with my Oppressor Mark. II and using OC3 Optical Line."
            json "We predicted their location to be somewhere in Somalia."
            kris "wat are they doing there?"
            json "Probably creating an army so they can overthrow us."
            kris "Wait a minute. Hold on."
            kris "WHY are they doing that?"
            json "Well, basically after we had succesfully \"killed\" you we became the new super powers in the demon world"
            kris "What the fuck."
            json "However we got into an argument about who should hold the throne."
            json "We ultimately decided it would be me as I am the smartest person here. /s"
            kris "Okay i have about 5 million more questions but i dont feel like asking them."
            json "After I became the leader, those 4 had gotten into an argument about me being the leader and threaten to kill us all. They left the realm 2 days later."
            kris "So are we catching them for money or to stop an upbringing?"
            json "Both i guess"
            kris "well..."
            kris "FUCK THAT! i dont feel like doing shit!"
            kris "I need to get a girlfriend first before i dive into this demon shit"
            json "the demon realm could give you up to 8 girls"
            kris "SIGN ME UP!!!"
            json "lmao"
            kris "so where do i start chief???"
            json "we're going to the demon realm"
            kris "wait. RIGHT NOW??!!"
            json "No. Flight leaves in 2 days."
            ###<<<<<<<ADD SOUND EFFECT IDK
            kris "WHAAAAAAAAT?"
            json "better pack extra curry"
            kris "Wait... How can we fly there with a plane??"
            json "Are you stupid?"
            json "The demon realm is right under thailand"
            json "That's like 3rd grade geography..."
            json "Well me Kyle, Kevin, and cade will meet you at San Jose airport. Flight leaves at 2 PM."
            hide jasonnorm
            window hide
            scene airportoutside
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            ######<<<<<<<<ADD AIRPORT AMBIENCE
            show jasonnorm
            window show
            json "Well we're here"
            hide jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            show kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            kyle "What airline are we flying on?"
            kris "Apparently we're flying on Southwest."
            hide kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            json "Yea i hacked into SWAlife databases and registered us as nonrevs so I didn't have to pay a dime for these tickets."
            kris "Well lets hurry up and get there so i could get some girls!!!"
            window hide
            scene airport
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            window show
            pa "Attention all passengers in the terminal looking for Southwest 69420 with service to the Demon Realm. The flight has been cancelled. All ticketed passengers must see a podium agent."
            kris "Shit!!! No!!!!!!!!"
            kris "My hot girls!!!!!!!!!"
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            json "Welp. That kinda sucks."
            json "Guess we'll have to wait for the next one"
            kris "When is that?"
            json "Well, theres another one in 1 hour but that flight is completely full. The next availiable one is in 3 days."
            kris "HUHH???? I CANT WAIT 3 DAYS!!! I NEED TO GET TO THE DEMON REALM NOW!!"
            mys "Did someone say demon realm?"
            label michiko:
                $ persistent.MeetMichiko = True
                window show
                $ quick_menu = True
                hide jasonnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                window hide
                show airport at bgslide
                $ renpy.pause(2, hard=True)
                window show
                show smay0101
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                girl2 "I can help with that."
                krismind "!!!!!"
                krismind "(ITS A GIRL!!!)"
                krismind "wait..."
                krismind "(No offense, but how is she going to be any help?)"
                show jasonnorm at slideleft2ppl
                $ renpy.transition(Dissolve(0.2))
                show smay0101 at slideright2ppl
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                json "Michiko???"
                krismind "WHAAAAT??? HE KNOWS HER??"
                kris "Do you know this person?"
                json "Yeah, shes the one who printed out the tickets cause my printer ran out of ink. I go to her house a few times too."
                krismind "(IVE NEVER SEEN HER BEFORE!)"
                krismind "(ah shit dude... this is another dead end.)"
                girl2 "I've already removed the no-show passengers on flight 69421 which departs in 1 hour. You guys should be able to fill those empty seats."
                json "Alright thanks."
                hide jasonnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                hide smay0101
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                scene airport at bgbackslide
                show jasonnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                json "Well it looks like we can go after all. So you can get girls i guess..."
                krismind "(well im not in that great of a mood... now that i know that even JASON has a girl...)"
                krismind "(Now that i think about it... what happened to that girl i saw before? I wonder where she's been)"
                json "Us 4 will be gone to get some starbucks. I'm kinda thirsty..."
                kris "(the only thing im thirsty for is love hehehehe....)"
                hide jasonnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show kylenorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                kyle "Yea maybe i'll get some Pho instead"
                hide kylenorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show kevinnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                kev "Do they even have pho here? Well I mean this IS San Jose.... pretty much Little Saigon at this point..."
                hide kevinnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show cadedis
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                cade "Ew... pho... nasty... PHOcking nasty xD!!"
                hide cadedis
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                kris "Yeah well... I guess I'll see you guys in a bit. Next flight is only in 1 hour at Gate 27 according to the timetable."
                show jasonnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                json "Alright well we'll see you there."
                kris "Peace."
                hide jasonnorm
                $ renpy.transition(Dissolve(0.5))
                $ renpy.pause(0.5, hard=True)
                ####ADD WALKING AWAY FOOTSTEP SOUND
                kris "(Hmmm... maybe ill get some Chicken Tikka masala??)"
                window hide
                show airport at bgslide
                $ renpy.pause(2, hard=True)
                window show
                mys "Yohooo~~♪♪♪"
                kris "(????)"
                show smay0101
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                girl2 "Heya~! ♪"
                kris "GAHH!"
                hide smay0101
                show smay0106
                girl2 "Hehehee... Why are you so startled...?"
                hide smay0106
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show smay0107zoom
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                girl2 "Have you already..... fallen in love?"
                kris "(shit dude... she smells nice... )"
                kris "(WAIT why am i acting cliche?? Im KRISTIK goddamnit!!! Im a CHAD! I GET ALL THE GIRLS IF I WANTED TO!)"
                window hide
            menu:
                "Assert Dominance":
                    $ pointsGirl2 += 2
                    jump air1
                "Act Embarrassed":
                    $ pointsGirl2 += 1
                    jump air2
        label air1:
            window show
            kris "Hey."
            kris "Let me touch your boobs."
            hide smay0107zoom
            show smay0117
            girl2 "Huh????"
            girl2 "U-um..."
            hide smay0117
            show smay0118
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "W-we should probably get a room first..."
            hide smay0118
            show smay0213
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            kris "..."
            kris "(SHES SERIOUS????)"
            kris "Wait hold on. I was just joking...."
            girl2 "W-What kind of person just says that?? Idiot!"
            kris "(shit dude im getting some real tsundere vibes and its really sexy!)"
            hide smay0213
            show smay0108
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Hahaha!! Look at your face!"
            girl2 "It's super red!"
            kris "(SHIT!!! i got bamboozled...)"
            girl2 "You actually thought....!!"
            hide smay0108
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            girl2 "Boys are so easy to manipulate..."
            kris "Shut up! You shouln't be saying that out loud!"
            kris "(im acting so cliche its cringy!)"
            kris "So this is what Jason's girl is like..."
            hide smay0101
            show smay0117
            girl2 "Huh? You thought i was with Jason?"
            hide smay0117
            show smay0107zoom
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Why... are you... jealous??"
            kris "Gh!"
            hide smay0107zoom
            show smay0108
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Ahahaha!"
            girl2 "Welp! I have to go now! Bye-bye! ♪"
            #<<<<<<<<< ADD WALK AWAY SOUNDS
            hide smay0108
            $ renpy.transition(Dissolve(0.5))
            $ renpy.pause(0.3, hard=True)
            kris "Fuck..."
            kris "Well at least I've gotten some progress."
            kris "At least I know her name..."
            kris "Michiko was it?"
            kris "I'll remember that...."
            kris "I'll remember how much of a piece of shit you are!"
            window hide
            jump pln1
        label air2:
            window show
            kris "(Well... maybe ill hold off on the chad personality...)"
            girl2 "Hey hey! What are you thinking in that lewd brain?"
            kris "I wasn't even thinking of anything lewd!"
            hide smay0107zoom
            show smay0201
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Hmmm... really?"
            kris "Yes really!"
            hide smay0201
            show smay0109
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Hmmm... I don't know about that."
            kris "Why do you want me to think of something lewd?!"
            hide smay0109
            show smay0111
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Absolutely not."
            kris "o..."
            hide smay0111
            show smay0109
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Awww... You look so sad!"
            hide smay0109
            show smay0107zoom
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Are you sad cause I denied your thoughts?"
            kris "Fuck you!"
            hide smay0107zoom
            show smay0109
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Hahahaha!"
            hide smay0109
            show smay0106
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "Well see you around. Bye~! ♪"
            hide smay0106
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            kris "Fuck her... playing with my feelings all the time..."
            window hide
            jump pln1
        label pln1:
            scene airport
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            window show
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            json "Yo! We're back!"
            json "That was some good pho right bois?"
            oth "Hell yea!!"
            hide jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            show cadedis 
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            cade "Hmmm well it was ok..."
            hide cadedis
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            show kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            kyle "They have a suprisingly good vietnamese resturaunt here!"
            kyle "I even said đụ má mày and the chef responded with tôi ghét bạn"
            kyle "It was super funny I nearly choked on the Nạm gầu"
            kris "Hey Jason."
            hide kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            json "Yeah?"
            kris "You know that Michiko girl?"
            json "What about her?"
            kris "Has she teased you before?"
            json "What do you mean?"
            kris "Like has she said anything like \"are you falling in love\" or \"lets get a room first\"?"
            json "Uhhh... no..."
            json "She's not that kind of person if I'm not wrong."
            kris "(You are CLEARLY wrong)"
            kris "Oh... hahaha... well I guess it's just my imagination..."
            hide jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            show jasonbruh
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)           
            json "Just what are you imagining... You've got some weird imagination..."
            kris "(shit!!! he probably thinks im thinking about some kinky shit or whatever)"
            hide jasonbruh
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            pa "Attention all passengers in the terminal we are now boarding fight 69421 with service to the Demon Realm. A group lines up first followed by B and C group."
            pa "We will first start by boarding any disabled or military veterans."
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            json "Well, I guess it's time we line up."
            kris "Yeah... it is..."
            if pointsGirl2 >= 2:
                kris "(I look back and try to find Michiko, but It appears she had already left...)"
                jump fly1
            else:
                kris "Well time to get some girls"
                jump fly1
        label fly1:
            scene cabin
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            json "Ayyy free seating"
            kris "yup SWA do be like that doe."
            hide jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            pa "Hello and welcome aboard flight 69421 with service to the Demon Realm. Just need to fill out some performance paperwork with ramp and we'll get going."
            kris "Haah..."
            kris "Haven't been on a plane since Kristik Saga 2..."
            pa "We will also be taking Kristik off of the plane because he shat on the seats."
            kris "Shit!!! I needed to poop badly so i pooped on the seats!"
            pa "Will passenger Kristik Lal make himself known to a flight attendant and leave the aircraft immediately."
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            json "What happened-"
            hide jasonnorm
            show jasonbruh
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            json "OH MY GOD IS THAT SHIT?"
            json "OMG IT SMELLS SO BAD!!"
            hide jasonbruh
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            att1 "Sir, could you please leave the aircraft?"
            kris "Yes ma'am..."
            kyle "AY KRISTIK WE'LL MEET YOU OVER THERE IN 3 DAYS!!"
            kris "Right, right..."
            kris "(Shit... next demon realm flight is in 3 days...)"
            att2 "Hey Flight Attendant 1? Could you pass me that Nuclear Waste Hazmat suit? This is some atomic waste."
            att1 "Roger."
            window hide
            scene airport
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            window show
            kris "Aghhh... shit.... now Im stuck here for 3 days..."
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            girl2 "Heyoo~~!!♪♪ I thought you were going to the Demon Realm?"
            kris "Yea, but well I got kicked off the flight cause I pooped on the seats..."
            hide smay0101
            show smay0109
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            girl2 "Pfff..."
            hide smay0109
            show smay0108
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)   
            girl2 "Ahahaha!"
            kris "(Wtf??? I thought she would be disgusted?)"
            girl2 "You're not serious are you?"
            ##<<< ADD SOUND EFFECT IDK
            kris "I'm dead serious."
            hide smay0108
            show smay0111
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)  
            girl2 "Ew...."
            kris "(THATS the kind of reaction i expected!)"
            hide smay0111
            show smay0201
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)  
            girl2 "Well... now that you're here... You're gonna wait 3 days for the next one?"
            kris "I guess so..."
            girl2 "Well... you DO want to get there right?"
            kris "I mean yea i do but it's too far to drive and i dont have a plane..."
            girl2 "Want to fly with me?"
            kris "(HUH???)"
            kris "Wait... Are you gonna hijack the plane?? Or hack into the system??"
            hide smay0201
            show smay0108
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)  
            girl2 "Hahah! No no no..."
            hide smay0108
            show smay0201
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "I'm going to use my private jet!"
            kris "(WTF??? IS SHE RICH LIKE KYLE??)"
            kris "I'm calling your bluff. There's no way you could possibly have a jet."
            girl2 "Wanna come with me and find out?"
            kris "that does sound interesting...."
            window hide
        menu:
            "Go with her":
                if persistent.GoWithMichiko > 0:
                        $ persistent.GoWithMichiko = 3                 
                else:
                    $ persistent.GoWithMichiko = 2 
                $ pointsGirl2 += 1
                jump flyg
            "Play it safe and stay back":
                if persistent.GoWithMichiko > 0:
                        $ persistent.GoWithMichiko = 3 
                else:
                    $ persistent.GoWithMichiko = 1
                jump noflyg

        label flyg:
            window show
            kris "Eh what the heck. This might be the last time i live before i get murdered by you."
            hide smay0201
            show smay0108
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Hahah! Trust me I won't do such thing."
            kris "It's sorta hard to trust you when i barely know you..."
            hide smay0108
            show smay0207
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Are you gonna come or not?"
            kris "Yea yea... I'm coming..."
            hide smay0207
            show smay0205
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Perfect! Let's go Poopie Pants! ♪"
            kris "Ugh..."
            hide smay0205
            window hide
            $ flyunforced = 1
            jump flywithg
        label noflyg:
            window show
            kris "I think I can wait out those 3 days."
            girl2 "Too bad. You're coming anyways!"
            hide smay0201
            show smay0106
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            kris "What?? I never agreed to this!!"
            girl2 "I'll see you at the ramp Poopie Pants! ♪"
            kris "Ugh..."
            hide smay0106
            window hide
            $ flyunforced = 0
            jump flywithg
        label flywithg:
            scene jetoutside
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            show smay0109
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "We're here! ♪ "
            kris "..."
            kris "(WHAT THE FUCK???)"
            kris "Just how rich are you???"
            girl2 "Not telling~~ ♪"
            hide smay0109
            show smay0106
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Let's hurry up and get there! We don't have much time!"
            girl2 "Also, one of my friends are already onboard. So you could say hi to them if you want!"
            kris "(A friend?)"
            kris "Hm alright whatever."
            hide smay0106
            window hide
            scene jet
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            show smay0108
            girl2 "We're here!"
            kris "(oh my fucking...)"
            mys "Heya Michiko chan!"
            kris "(Huh??)"
            show smay0108:
                linear 0.3 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            show ssuo0113 at slideright2ppl
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Heya Asami chan!"
            kris "(ASAMI????)"
            hide ssuo0113
            hide smay0108
            show ssuo0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "..."
            girl1 "Wait... a minute..."
            hide ssuo0101
            show ssuo0128
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "YOURE THAT ONE PERVERTED GUY!!"
            kris "WHAT DO YOU MEAN PERVERTED???"
            hide ssuo0128
            show smay0115
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Do you guys know eachother?"
            hide smay0115
            show smay0109
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "It seems like you two have a pretty good relationship!"
            hide smay0109
            show ssuo0121
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "It's certainly not like that... his friend said that he got a b... when talking to me..."
            hide ssuo0121
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "What? What did he have? A \"b...\"?"
            kris "(shit shes gonna expose me!)"
            hide smay0101
            show ssuo0104
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "A boner..."
            hide ssuo0104
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "What was that? I couldn't hear you."
            hide smay0101
            show ssuo0121
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "A BONER!!!"
            kris "(SHIT!!! she said it! what if she kicks me off the plane???)"
            hide ssuo0121
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "O-oh..."
            hide smay0101
            show smay0118
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "I guess it's normal for men to have it... right?"
            kris "(shit dude! My heart is RACING!)"
            hide smay0118
            show smay0213
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "W-well, I'll inform the captain that we're ready for departure..."
            hide smay0213
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            show ssuo0105
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "So.... Why are you here?"
            kris "I could ask the same for you..."
            kris "(the awkwardness IS OFF THE CHARTS!!)"
            girl1 "Well I'm going to the demon realm so I could go to the castle with Michiko..."
            kris "Wait... Do you both have business there?"
            hide ssuo0105
            show ssuo0113
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "Yea.. me and Michiko like to meet up with our other friends in the realm."
            kris "I see..."
            hide ssuo0113
            show smay0106
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Right we're ready to go!"
            girl2 "We'll be taxing out of the stand and takeoff pretty soon."
            kris "Alright."
            hide smay0106
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(1.2, hard=True) 
            kris "Ughhh..... Jeez give me a break..."
            window hide
            scene takeoff 
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(4, hard=True)
            scene jet
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(4, hard=True)
            window show
            show smay0107zoom
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "Good morning~"
            kris "Mmmmm.... how many hours did I fall asleep for?"
            girl1 "3 hours."
            kris "Jesus... How long is this flight?"
            hide smay0107zoom
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            pil "Well the route is 6781 Nautical Miles."
            firo "Yeah and it will take us about 25 more hours to get to the Demon realm."
            kris "What the???"
            kris "How do we even have enough fuel to get there?"
            pil "We're using OC3 Optical Line as our fuel source."
            firo "OC3 Optical Line can let us travel for 541 hours continuosly."
            kris "Goddamn."
            pil "Well we gotta attend to the flight deck, so peace."
            kris "Peace, i guess."
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "Jeez, I already watched all the movies on here..."
            girl1 "Why is there no indian dramas on here??????"
            kris "(i guess she likes indian dramas...)"
            kris "(WAIT! Im indian! I can flex my indian drama knowledge in front of her and make her love me! Yes!!)"
            kris "(But.. i'll feel bad hitting on Michiko when Asami is around...)"
            kris "(What should i do?)"
            hide smay0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            window hide
        menu:
            "Flirt with Michiko":
                $ persistent.flirtmichiko = True
                $ pointsGirl2 += 1
                jump michhit
            "Flirt with Asami":
                $ persistent.flirtAsami = True
                $ pointsGirl1 += 2
                jump asamhit
        label michhit:
            window show
            kris "(I'll hit on Michiko)"
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Jeez! This is so boring watching the same movies again!"
            kris "Hey... Michiko"
            girl2 "Hm?"
            show smay0106
            girl2 "What's up? You need me for something?"
            kris "(what should i say?)"
            window hide
            menu:
                "I love you":
                    $ persistent.michikoFlirtType = 1
                    $ pointsGirl2 += 3
                    jump ilymich
                "You look beautiful today":
                    $ persistent.michikoFlirtType = 2
                    $ pointsGirl2 += 1
                    jump beautmich
                "You're so sexy I wish I could do you right here in the plane!":
                    $ persistent.michikoFlirtType = 3                   
                    $ pointsGirl2 += 1
                    jump sexymich
            label ilymich:
                hide smay0101
                window show 
                kris "I love you."
                hide smay0106
                show smay0117
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl2 "H-Huh?? What are you saying??"
                kris "I love you with all my heart. I wish to be with you forever!"
                hide smay0117
                show smay0213
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl2 "H-Hold on!! This is too sudden..."
                kris "Nothing is too sudden! I love you Michiko!"
                kris "I know it's only been a few hours since first sight... But I fell in love with you as soon as I saw you!"
                hide smay0213
                show smay0214
                girl2 "P-Please stop! Let me process this...."
                kris "(shit!! i think ive gone a bit overboard...)"
                hide smay0214
                show ssuo0111
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                kris "?"
                kris "(she does not look all that happy about this...)"
                kris "(shouldve done this in private or something...)"
                window hide
                jump awklanding
            label beautmich:
                hide smay0101
                window show
                kris "You look very beautiful right now."
                hide smay0106
                show smay0117
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl2 "Huh?"
                girl2 "What's this for?"
                kris "Nothing. Just wanted to state the obvious."
                hide smay0117
                show smay0214
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                girl2 "O-Ok..."
                window hide
                jump landing
            label sexymich:
                hide smay0101
                window show
                kris "You're so sexy I wish I could do you right here in the plane!"
                hide smay0106
                show smay0213
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl2 "H-huh??"
                girl2 "W-wow... You like me that much?"
                girl2 "We'd do it even in front of.... Asami....?"
                kris "Hell yes!"
                hide smay0213
                show smay0214
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl2 "T-Thanks... but I think we need to start a bit slower.... and i'd be too embarrassed to do it in front of Asami..."
                kris "(OOF)"
                kris "(RIP my pride)"
                hide smay0214
                show ssuo0111
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                kris "(shit... that must be cringy for her to watch...)"
                kris "(shouldve done this in private or something...)"
                window hide
                jump awklanding
        label asamhit:
            window show
            kris "(I'll hit on Asami)"
            show ssuo0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "Oooh Big Bang Theory Episode 8!"
            kris "Hey... Asami"
            hide ssuo0101
            show ssuo0104
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "Y-yes?"
            hide ssuo0104
            show ssuo0105
            girl1 "Do you want me to do soemthing?"
            kris "(what should i say?)"
            window hide
            menu:
                "I really love you":
                    $ persistent.asamiFlirtType = 1
                    $ pointsGirl2 += 3
                    jump ilyasam
                "You're really cute looking today even at this hour":
                    $ persistent.asamiFlirtType = 2
                    $ pointsGirl2 += 1
                    jump cuteasam
                "Your body is so slender it's turning me on!":
                    $ persistent.asamiFlirtType = 3
                    $ pointsGirl2 += 1
                    jump sexyasam
            label ilyasam:
                window show
                kris "I really love you, Asami"
                hide ssuo0105
                show ssuo0124
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl1 "W-What are you saying??"
                girl1 "We've only just met!"
                kris "I don't care about that! It was love at first sight! Asami, I love you!"
                hide ssuo0124
                show ssuo0121
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl1 "Don't say such embarrassing things with others around!"
                kris "I don't care about that! Asami.. Do you love me?"
                girl1 "I-i can't say for sure! "
                hide ssuo0121
                show ssuo0124
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl1 "I'd have to spend more time with you... to find out...."
                kris "I'll take that as a sort-of yes!"
                hide ssuo0124
                show smay0213
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                kris "(looks like Michiko wasn't thrilled about my announcement...)"
                window hide
                jump awklanding
            label cuteasam:
                window show
                kris "You look really cute right now!"
                hide ssuo0105
                show ssuo0121
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl1 "W-What are you saying??"
                kris "I'm just telling you the facts."
                girl1 "W-Well, you don't need to tell me that captain obvious!"
                kris "Haha you're all red!"
                hide ssuo0121
                show ssuo0105
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl1 "Be quiet!"
                kris "Haha... Just stating the obvious!"
                window hide
                jump landing
            label sexyasam:
                window show
                kris "Your body is so slender it's turning me on!"
                hide ssuo0105
                show ssuo0124
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl1 "U-um..."
                hide ssuo0124
                show ssuo0104
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True) 
                girl1 "You should've said that in private..."
                kris "Let's do it right now!"
                hide ssuo0104
                show ssuo0128
                girl1 "W-Wha...?"
                hide ssuo0128
                show ssuo0121
                girl1 "I-I'm not a whore! I have standards!"
                kris "It's fine! Let's go to the lavatory."
                girl1 "..."
                hide ssuo0121
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(2.0, hard=True) 
                ##########<<<<<<<<<<<<<<<CLOTHES RUSTLING SOUND EFFECT
                show ssuo0403
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(2.0, hard=True) 
                kris "!!!!!!"
                kris"(OMG SHE ACTUALLY DID IT!!)"
                show ssuo0403 at slideright2ppl
                show smay0117:
                    linear 0.3 xalign 0.1
                girl2 "Asami???!!!!"
                girl1 "You want to do it? Okay follow me."
                kris "Whoa whoa whoa whoa whoa!!! I-I reconsider this..."
                hide ssuo0403
                show ssuo0404:
                    linear 0.0 xalign 0.8
                girl1 "What??? You just made me remove my clothes and now you want to call it off?"
                kris "I-I'm sorry!"
                girl1 "Ugh..."
                hide ssuo0404
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(2.0, hard=True) 
                show ssuo0105:
                    linear 0.0 xalign 0.8
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(2.0, hard=True) 
                girl1 "That was embarrassing...."
                kris "Tell me about it..."
                hide ssuo0105
                show ssuo0121: 
                    linear 0.0 xalign 0.8
                girl1 "What do you mean \"Tell me about it\" ??? You weren't the one stripping!"
                kris "O-Okay im sorry!"
                hide smay0117
                $ renpy.transition(Dissolve(0.2))
                show smay0213: 
                    linear 0.0 xalign 0.1
                $ renpy.transition(Dissolve(0.2))
                girl2 "Jeez you two..."
                window hide
                jump awklanding          
        label awklanding:
            scene demonair
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            window show
            kris "(It's been pretty awkward for the rest of the flight...)"
            show smay0213
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "..."
            kris "(jesus... whats with this tension?)"
            hide smay0213
            show ssuo0105
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "..."
            kris "So where is this castle place?"
            girl1 "I'm not entirely sure..."
            kris "(Fuck bro! I need someone to break the tension!!)"
            hide ssuo0105
            show smay0213
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "They're here...."
            kris "(I wonder who \"they\" are...)"
            hide smay0213
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(1, hard=True) 
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(1, hard=True) 
            json "Yo."
            kris "Hey..."
            json "Why are the 3 of you so awkward?"
            kris "Some stuff just happened on the flight here..."
            json "Don't tell me you already lost your virginity...."
            kris "I DID NOT!!"
            json "Hahaha. Okay. SuRe BuDdY"
            json "Well i've rented out a car to drive to the main castle."
            kris "Alright."
            hide jasonnorm
            show kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            kyle "Since when did Southwest do such long International flights?"
            hide kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            show kevinnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            kev "IKR! That shit took way too long!"
            hide kevinnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            json "Alright guys. Hurry up lets go."
            kris "..."
            jump demonout

        label landing:
            scene demonair
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            window show
            kris "(Jesus christ that took a while...)"
            show smay0108
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Finally!! We're here!"
            hide smay0108
            show ssuo0113
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "Wow that felt much longer than normal!"
            hide ssuo0113
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            pil "We had headwind of 220 knots which limited our max cruise airspeed."
            kris "(nobody cares nerd lol)"
            firo "Well I'm gonna get some mcdonalds or smth"
            pil "Same. I'm DYING for Chinese food rn"
            firo "{=chinesetext} 現在去給我的陰莖放鴨 {/=chinesetext}"
            pil "{=chinesetext} 我不是同性戀。我不喜歡陰莖。我愛陰道。 {/=chinesetext}"
            kris "(????)"
            kris "So where is this castle place?"
            show ssuo0113
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "Let me bring it up on Google Maps."
            kris "(When did she smell so good??)"
            kris "(Oh fuck... i have a boner...)"
            kris "Ahaha! Yea Google Maps! I love google maps!"
            kris "{=chinesetext} 六四事件，又稱六四天安門事件，狹義上指六四清場，是八九民运的結局，即1989年6月3日晚間至6月4日凌晨，中国人民解放军、武装警察部队和人民警察在北京天安門廣場对示威集会进行的武力清场行动。 {/=chinesetext}"
            hide ssuo0113
            show ssuo0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl1 "????"
            girl1 "Is there something wrong?"
            kris "(Dont look at my pants please!!)"
            hide ssuo0101
            show smay0106
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl2 "Hey c'mon let's go! They're waiting for us!"
            kris "(Who's waiting for us?)"
            hide smay0106
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(1, hard=True) 
            show jasonnorm
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(1, hard=True) 
            json "Yo what's up"
            json "I thought you we're coming in 3 days later?"
            if flyunforced == 1:
                kris "Yeah i just decided to hop on Michiko's Dassault Falcon 50."
            else:
                kris "Well... I was sort of dragged here..."
            json "cool."
            json "Also nice buldge."
            kris "STFU!!! DONT SAY IT TOO LOUD OR THEY'll HEAR!!"
            json "lol getting hung up on that stuff."
            json "At least you got here right?"
            json "I got a car and we're gonna all drive to the main castle."
            kris "Okay."
            kris "You said you became the lord of this place right?"
            json "Yeah i did."
            kris "Why are you not being flocked by hoards of girls cause you're super popular?"
            json "Because I'm vietnamese ;-;"
            kris "What does that have to do with anything?"
            json "Girls here only care for European guys."
            kris "(OOF)"
            json "Alright. Hurry up."
            kris "Yup."
            hide jasonnorm
            window hide
            jump demonout
    label demonout:
        scene demonairoutside
        $ renpy.transition(Fade(1, 0.3, 1)) 
        $ renpy.pause(2, hard=True)
        kris "What car is it?"
        show jasonnorm
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        json "I got an R34. It's not the Coupe so it has extra seats."
        kyle "Ahh sweet!"
        json "Except... it can only fit up to 6 people... There's 7 of us... Me, Kevin, Cade, Kyle, Michiko, Asami, and you..."
        json "Sorry Kristik but you can't ride in the R34."
        kris "WHAT??"
        kris "Why me?"
        kris "Why not take kyle out or something?!"
        hide jasonnorm
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(0.3, hard=True) 
        show kylemad
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        kyle "Hell no! It's and R34 of course I'm driving it!!"
        hide kylemad
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(0.3, hard=True) 
        show jasonnorm
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        json "Sorry kristik. We don't have space."
        kris "How the hell am I gonna get there?"
        json "Simple. We got a smaller backup car just for you."
        kris "well... whats the car?"
        json "It's an Ibishu Pigeon."
        kris "A what?"
        json "Take a look."
        show pigeon
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        play backgroundSFX "audio/pigeon.ogg"
        kris "What the fuck is that?!!"
        show smay0108small:
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.4))
        #$ renpy.pause(0.7, hard=True) 
        girl2 "Hahahah! What is that???"
        girl2 "That looks like a really bad car!!!"
        hide smay0108small
        $ renpy.transition(Dissolve(0.2))
        #$ renpy.pause(0.3, hard=True) 
        kris "I cant drive that ugly ass shit!!"
        json "Relax. It has stabilizers so it doesn't fall over easily."
        kris "Who cares? This thing is so slow!!"
        hide pigeon
        show pigeonengine
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        json "It's not as weak as you think it is. It has a 600cc l3 engine with 5 speed manual transmission. Even the windows are manual!"
        hide pigeonengine
        show pigeoninterior
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        json "There isn't any power steering, but it does have an Adjustable Race ECU with NoS injection and a custom engine block."
        hide pigeon
        hide pigeoninterior
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        stop backgroundSFX fadeout 1.0
        kris "I dont know what ching chong mumbo jumbo techno nerd shit you just said was but one thing is for sure I am NOT driving that."
        json "Well... then.. I guess you'll be stuck here!"
        hide jasonnorm
        $ renpy.transition(Dissolve(0.2))
        play sound "audio/skid.ogg"
        $ renpy.pause(1.6, hard=True) 
        #######<<<<<<<<<<DRIVING AWAY sounds
        kris "WAIT!!"
        kris "(Did they seriously all abandon me???)"
        kris "I guess I have to drive this rustbucket then..."
        window hide
        scene bg black text
        with wipeleft
        scene mountain
        with wipeleft
        $ renpy.pause(1, hard=True) 
        window show
        kris "Ahh shit! I'm completely lost!"
        kris "I really need to upgrade my phone..."
        kris "I'm still using the Motorolla DynaTAC 8000X..."
        mys "Hey kid!"
        kris "?"
        mys "Wanna drift race?"
        scene rx-7 view
        $ renpy.transition(Dissolve(0.6))
        $ renpy.pause(1, hard=True) 
        kris "nah im fine"
        rx7 "If you dont, im going to steal your girlfriend"
        kris "{cps=20}WHAT... DID... YOU... JUST... SAY???{/cps}"
        kris "I WONT LET A CHAD LIKE YOU STEAL MY BITCHES!!"
        rx7 "Ohoho... Let's get started."
        window hide
        #
        #
        #
        #
        #
        #
        #
        ######################<<<<<<<<<<< INITNAL D SCENE 
        window show
        rx7 "Shit... How did he do that?"
        kris "Hahaha Get your broke ass RX7 out of here"
        kris "You're worse than Shingo lmao"
        rx7 "..."
        kris "(Wait shit! I'm gonna be fucking late getting there!)"
        kris "Lucky for you, I have to be somewhere right now. You might want to upgrade that transmission to Level 3 is all I'm saying."
        rx7 "This isn't CSR Racing 2 where you just click a button and it upgrades shit!"
        kris "Yeah yea, why don't you get your VTEC out of here"
        rx7 "This isn't a Honda! It's a Mazda you retard!"
        kris "Whatever. Just don't get too hung up on your Ray Tracing."
        rx7 "What does ray tracing have to do with my car??"
        kris "I have no idea. I'm just saying some random techno nerd shit. Anyways, I'm repping ground, so get out of my terrirtory."
        rx7 "Gh..."
        kris "Well... that guy was super easy to race..."
        window hide
        scene bg black
        with wipeleft
        play backgroundSFX "audio/bggyoung.ogg"
        scene castle1
        with wipeleft
        $ renpy.pause(1, hard=True) 
        window show
        $ wenttobbq = 0
        kris "Jesus... I finally made it! I had to use a conventional map for this shit..."
        mys "{cps=40}{=koreatext} 실례 합니다만, 실제로 한국인입니다. 당신이 잘못된 곳으로 갔다고 생각합니다. {/=koreatext}{/cps}"
        kris "Uhh..."
        show syuz0101: 
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        show srik0101: 
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        kris "(Since when do people in the demon realm speak singaporean?)"
        mys "{cps=40}{=koreatext} 그는 우리가 무슨 말을하는지 모른다. 그는 외국인입니다. {/=koreatext}{/cps}"
        mys "{cps=40}{=koreatext} 그래, 당신 말이 맞아. 그는 인도인처럼 보인다. 그는 아마도 우리가 무엇을 말하는지 모를 것입니다. {/=koreatext}{/cps}"
        hide srik0101
        show srik0105:
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "{cps=40}{=koreatext} 그것은 우리가 그를 놀릴 수 있다는 것을 의미합니다. ㅋㅋㅋㅋㅋㅋㅋㅋ ㅌㅌㅌㅌㅌㅌ ㅎㅎㅎㅎ {/=koreatext}{/cps}"
        hide syuz0101
        show syuz0206:
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "{cps=40}{=koreatext} 야, 한국 여자 좋아해? ㅎㅎㅎㅎ {/=koreatext}{/cps}"
        kris "(What did she say?)"
        mys "{cps=40}{=koreatext} 그는 얼굴이 붉어졌다 !!! 나는 그가 매우 당황 스럽다고 말할 수있다! ㅎㅎㅎㅎ (ノ*°▽°*)  (￣▽￣*){/=koreatext}{/cps}"
        hide srik0105
        show srik0214: 
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "{cps=40}{=koreatext} 젠장, 왜 한국 남자들이 이쁘지 않니? ㅠㅠㅠㅠㅠㅠ {/=koreatext}{/cps}"
        hide syuz0206
        show syuz0101:
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "{cps=40}{=koreatext} 적어도이 소년은 당신을 좋아합니다!	(￣ε￣＠) {/=koreatext}{/cps}"
        mys "{cps=40}{=koreatext} 알았어, 그것으로 충분 해 서둘러 갑시다. {/=koreatext}{/cps}"
        kris "Uhhhhh.... "
        mys "{cps=40}{=koreatext} 그는 길을 잃었다! 우리가 그를 떠나야합니까? {/=koreatext}{/cps}"
        hide srik0214
        show srik0118: 
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "{cps=40}{=koreatext} 호 호 호! 좋은 생각이 있습니다 .. {/=koreatext}{/cps}"
        kris "(I dont like the look on her face...)"
        hide syuz0101
        show syuz0206:
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "Hey foreigner! Why don't you come with us?"
        kris "(i do not like the sound of that...)"
        kris "Hey hold on. Just speak english! Why are you speaking singaporean to eachother?"
        hide syuz0206
        hide srik0118
        show syuz0101: 
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        show srik0101: 
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "Singaporean?"
        hide syuz0101
        hide srik0101
        show syuz0108: 
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        show srik0204:
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "Ahahaah! It's korean! You do realize that we're in korea right?"
        kris "(WOT????)"
        kris "HOWWW????"
        kris "I.... I was... WHAAAAAAAAT???"
        mys "{cps=40}{=koreatext} 세상에! 이런 멍청이 같으니라고!{/=koreatext}{/cps}"
        kris "(How in the hell??? WHAT?)"
        hide srik0204
        hide syuz0108
        show syuz0206:
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        show srik0204:
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "You're a real funny foreigner!"
        kris "Well, whatever!"
        kris "Why don't you guys just speak english!"
        mys "Well, we ARE in korea... And plus Chung Cha can't understand english. Well just a bit i guess..."
        hide syuz0206
        hide srik0204
        show srik0101
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        girl3 "{cps=40}{=koreatext} 안녕하세요! 만나서 반갑습니다! （＞y＜）{/=koreatext}{/cps}"
        window hide
        show screen disable_Lmouse()
        show pattern 3
        with wipeleft
        hide pattern 3
        show pattern 3
        $ renpy.movie_cutscene("chungchaintro.ogv")
        hide pattern 3
        with moveoutleft
        window show
        hide screen disable_Lmouse
        kris "(damn... got that nerdy look too...)"
        girl3 "HeRrO i KenNot SpeEk EngRish sO PrEasE dO nOt BullY mE PrEasE TAnk YoU"
        kris "(RIP the english lmao)"
        hide srik0101
        show syuz0106
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "Hey hey! Don't just give her all the attention!"
        kris "Well, what's your name then?"
        hide syuz0106
        show syuz0101
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "Ooohhh... So you're being assertive already?"
        kris "How is that being assertive? I just asked for your name!"
        hide syuz0101
        show syuz0201
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        mys "Hahaha... Well my name is Park Hui Young."
        window hide
        show screen disable_Lmouse()
        show pattern 3
        with wipeleft
        hide pattern 3
        show pattern 3
        #$ renpy.pause(5.0, hard=True)
        $ renpy.movie_cutscene("parkhuiintro.ogv")
        hide pattern 3
        with moveoutleft
        window show
        hide screen disable_Lmouse
        girl4 "Just call me Hui Young."
        girl4 "Nice to meet you~"

        kris "Alright. And uh yeah... nice to meet you too..."
        hide syuz0201
        show srik0105:
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        show syuz0201:
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        girl3 "{cps=40}{=koreatext} 그의 얼굴을 봐! 그는 매우 당황 스럽다! ㅋㅋㅋㅋㅋㅋ{/=koreatext}{/cps}"
        hide syuz0201
        show syuz0102:
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        girl4 "{cps=40}{=koreatext} 우와 !! 그는 매우 당황 스럽다!{/=koreatext}{/cps}"
        kris "(why am i embarrassed?)"
        kris "(They're probably laughing about how im blushing...)"
        girl4 "Well, just a question. What are you doing here?"
        kris "Oh i was trying to get to the demon realm castle but i ended up drift racing a guy... and i got lost after that."
        kris "So i got a map to navigate to the castle and i thought this was the place."
        girl4 "Hmmm... interesting story."
        girl4 "Well this is Gyoungbokgung Palace. It's a historical place so you can't step inside any of the buildings, but you could walk around in the palace."
        girl4 "Can i see that map you have?"
        kris "Sure..."
        hide syuz0102
        hide srik0105
        show map1: 
            linear 0.0 xalign 0.5 yalign 0.3
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        girl4 "Thats!!"
        girl4 "Thats the map of Bucheon!"
        girl4 "What? How did you even get here? We're in Seoul!"
        kris "Uh yeah... had to change some routes i guess... "
        kris "I couldn't read any of the ching chong so i had to guess."
        hide map1
        show srik0105:
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        show syuz0201:
            linear 0.0 xalign 0.8
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        girl4 "{cps=40}{=koreatext} 그는 실제로 부천지도를 가지고 있습니다! 와! ㅋㅋㅋㅋㅋㅋㅋ{/=koreatext}{/cps}"
        girl3 "{cps=40}{=koreatext} 세상에, 그는 어떻게 두 장소를 혼동 했습니까? ㅋㅋㅋ{/=koreatext}{/cps}"
        hide sirk0105
        show srik0101:
            linear 0.0 xalign 0.1
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.3, hard=True) 
        girl4 "Well... since you're already here... Why don't we all go somwhere?"
        kris "(But i have to go to the castle! Ugh... what should i say?)"
        window hide
        menu:
            "Alright sure.":
                $ pointsGirl3 += 1
                $ pointsGirl4 += 1
                jump kor
            "Sorry, i have to go somewhere.":
                jump cstl
        label cstl:
            window show
            kris "Sorry. I have to get there, i can't be hanging around."
            girl4 "Well why don't you bring us with you?"
            kris "Huh?? Why do you want to go there?"
            girl4 "We have to meet up some people over there. We were waiting here for the bus to get there."
            girl4 "But since youre going there, why don't you drive us there with you?"
            kris "Well, one small problem with that."
            hide srik0101
            hide srik0105
            hide syuz0201
            show syuz0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl4 "What is it?"
            kris "My car is a two seater..."
            girl4 "What kind of car do you have?"
            kris "It's this..."
            hide syuz0101
            show pigeon
            stop backgroundSFX fadeout 1.0
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.5, hard=True) 
            play backgroundSFX "audio/pigeon.ogg"
            show syuz0108small:
                linear 0.0 xalign -0.01
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl4 "{cps=40}{=koreatext} 아 하하하! 이게 뭐야? ㅋㅋㅋㅋㅋㅋㅋ{/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext} 이것은 쓰레기처럼 보인다! ㅋㅋㅋ{/=koreatext}{/cps}"
            hide syuz0108small
            hide pigeon
            $ renpy.transition(Dissolve(0.2))
            stop backgroundSFX fadeout 1.0
            $ renpy.pause(1.0, hard=True) 
            play backgroundSFX "audio/bggyoung.ogg"
            show srik0105:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            show syuz0201:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl4 "Well, we could ride in it."
            kris "How?"
            girl4 "You'll just have to sit in the back."
            kris "The back?"
            girl4 "Yup. The bed of the truck."
            kris "Whaat? Im NOT sitting out there!"
            girl4 "Well you wouldn't want these 2 elegant women out there sitting would you?"
            kris "tch!"
            kris "Fine..."
            girl4 "Perfect!"
            hide srik0105
            show srik0204:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl3 "{cps=40}{=koreatext} 당신은 그를 속였다 ...{/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext} 알 겠어? 너무 쉬웠다!{/=koreatext}{/cps}"
            stop backgroundSFX fadeout 3.0
            window hide
            jump demonactualcastle
        label kor:
            window show
            kris "Sure. I'll go. I've got nothing else to do..."
            hide syuz0201
            hide srik0101
            hide srik0105
            show srik0204:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            show syuz0206:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl4 "Yay! Let's start our date!"
            kris "(D-date???)"
            kris "Wait hold on. We don't have that kind of thing going on between us. I only decided to go cause im bored AF."
            hide syuz0206
            hide srik0204

            show syuz0113zoom:
                linear 0.0 xalign 0.5
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl4 "Why? Would i not be the kind of person you would date?"
            kris "U-um.."
            kris "Well, i mean... "
            kris "Uhh...."
            hide syuz0113zoom
            show srik0204:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            show syuz0206:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            girl4 "Just joking with you~~~"
            girl3 "{cps=40}{=koreatext}와! 그는 동시에 매우 무서워하고 부끄러워 보인다! ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ{/=koreatext}{/cps}"
            girl3 "{cps=40}{=koreatext} 당신의 미친 성격은 정말 남자를 두려워합니다! ㅋㅋㅋ ㅎㅎㅎㅎ{/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext} 남편이 나쁜 일을하기로 결정한다면, 나는 분명히 그에게 교훈을 줄 것입니다! ㅎㅎㅎㅎ{/=koreatext}{/cps}"
            hide srik0204
            show srik0105:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            girl3 "{cps=40}{=koreatext} 그는 지금 정말 무서워요! ㅎㅎㅎㅎㅎㅎㅎㅎ{/=koreatext}{/cps}"
            hide syuz0206
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            girl4 "Hey did I make you scared of me? "
            kris "U-Uh no... obivously not..."
            hide syuz0101
            show syuz0108:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            girl4 "{cps=40}{=koreatext} ㅎㅎㅎㅎㅎㅎ 그는 실제로 나를 두려워합니다!{/=koreatext}{/cps}"
            kris "(i really wish i knew what they were saying...)"
            hide syuz0108
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            hide srik0105
            show srik0101:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            girl4 "Well let's hurry up and go!"
            kris "Wait where are we even going??"
            girl4 "You'll see~"
            girl3 "{cps=40}{=koreatext}처녀들의 저녁식사!{/=koreatext}{/cps}"
            girl3 "{cps=40}{=koreatext}우리와 함께 한 소년이 있습니다!!{/=koreatext}{/cps}"
            ####<<<< PLAY GIRL FOOTSTEPS
            stop backgroundSFX fadeout 3.0
            window hide
            jump girlsnightout
        label girlsnightout:
            show screen disable_Lmouse()
            scene bg black
            with wipeleft
            scene nightkor
            with wipeleft
            $ renpy.pause(1.0, hard=True)
            hide screen disable_Lmouse
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            hide srik0105
            show srik0101:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            girl4 "We're here!"
            kris "Damn! This place is so well lit at night!"
            girl4 "Well, Korea and Japan are pretty popular for the night environments!"
            girl3 "{cps=40}{=koreatext}노래방! 노래방! 노래방!{/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext}왜 노래방?{/=koreatext}{/cps}"
            girl3 "{cps=40}{=koreatext}실제로 나중에 노래방을 할 수 있습니다. 배가 고파서 고기를 먹으러 가자!{/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext}좋구나! 먹자!{/=koreatext}{/cps}"
            girl4 "We're going to eat Korean BBQ. There's a good KBBQ place i know over here."
            kris "I have never tried it, but it sounds intriguing."
            girl4 "Well this'll be a new experience for you."
            hide srik0101
            hide syuz0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            window hide
            show screen disable_Lmouse()
            scene bg black
            with wipeleft
            scene kbbqinterior1
            with wipeleft
            ##############<<<<<<<<<<<<<<<<<<<PLAY LOUD INTERIOR NOISES
            $ renpy.pause(1.0, hard=True)            
            window show
            hide screen disable_Lmouse
            girl4 "Hmmm..."
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.2))
            hide srik0105
            show srik0101:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.2))
            girl4 "{cps=40}{=koreatext}무엇을 원하세요?{/=koreatext}{/cps}"
            girl3 "{cps=40}{=koreatext}불고기!{/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext}알 겠어.{/=koreatext}{/cps}"
            girl4 "What do you want?"
            kris "Uhh... im hindi so i cant eat any sort of beef or pork."
            girl4 "It's fine. We can get you the chicken katsu."
            hide syuz0101
            hide srik0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True) 
            waiter "{cps=20}{=koreatext}어서 오십시오. 주문은 어떻게합니까?{/=koreatext}{/cps}"
            girl4 "{cps=20}{=koreatext}예, 우리는 불고기 팬, 치킨 돈까스 한 접시, 칼비 한 접시를 갖고 싶습니다.{/=koreatext}{/cps}"
            waiter "{cps=20}{=koreatext}예, 그게 될거야?{/=koreatext}{/cps}"
            girl4 "{cps=20}{=koreatext}아니, 그게 다야.{/=koreatext}{/cps}"
            waiter "{cps=20}{=koreatext}알 겠어, 음식이 올거야.{/=koreatext}{/cps}"
            girl4 "{cps=20}{=koreatext}감사합니다.{/=koreatext}{/cps}"
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.6))
            hide srik0105
            show srik0101:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.6))  
            $ renpy.pause(1.0, hard=True)                    
            girl4 "Sooo..."
            girl4 "Want to tell more about yourself?"
            kris "Well, I'm only here cause I was drift racing a Mazda RX-7, and eventually got lost when i was trying to drive to the demon realm's castle."
            girl4 "Why were you going there in the first place?"
            kris "I had to meet with the demon realm's lord, Jason. Apparently, they needed me to help with capturing some of my old friends...."
            hide syuz0101
            hide srik0101
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.2, hard=True) 
            show syuz0102:
                linear 0.0 xalign 0.5
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.2, hard=True) 
            girl4 "Oooh... so it sounds like you're tangled in this mess."
            kris "Yup. But i gotta get back soon. I have 6 people waiting for me..."
            girl4 "Well you could bring us with you. We have some business over there too."
            kris "What business may that be?"
            girl4 "We have to meet with the demon realm's arsenal management secretary."
            girl4 "You might know her, her name is Asami Yamamoto."
            kris "What??? ASAMI??? MILITARY SECRETARY??"
            girl4 "Huh...? Yeah..."
            kris "I know her!! I flew on Michiko's private jet with Asami when i was flying to the demon realm!"
            girl4 "Ahh... So you know her huh?"
            kris "Yeah i do!"
            girl4 "And you've met Michiko too?"
            kris "Yeah i have. What's her role?"
            girl4 "As far as I know, she's apart of the Air Force. She flies an F-16C Block 50 and is usually doing dogfights and classified bombing runs."
            kris "(Jesus??? Really???)"
            girl4 "She's been apart of multiple bombing runs in Syria."
            kris "(No wonder why she has a private jet and everything....)"
            kris "Just curious, what do you and Chung Cha do?"
            girl4 "Oh? Me and Chung Cha are apart of the Central Intelligence Agency."
            kris "(WTF???)"
            girl4 "We usually take part in spying or sometimes assassinations."
            kris "Isn't it sort of dangerous for you guys to stand out in the open?"
            girl4 "It's fine. Me and Chung Cha have been trained in weapon smuggling. I have an AK47 hidden inside my top right now."
            kris "(HUH???? HOW??? I'm actually not even going to question it...)"
            kris "Wow. So why do you need Asami if you dont mind me asking?"
            girl4 "Well, we're heading back after a mission and report our findings to Asami."
            kris "What was the mission?"
            girl4 "Its a secret~~~"
            kris "Alright..."
            $ wenttobbq = 1
            hide syuz0102
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.6))
            show srik0104:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.6))  
            $ renpy.pause(1.0, hard=True) 
            girl3 "{cps=40}{=koreatext}음식이왔다!{/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext}O K ! 먹자!{/=koreatext}{/cps}"
            hide srik0104
            hide syuz0101
            $ renpy.transition(Dissolve(0.6))  
            ####<<<<<<<<< PLAY GRILLING SOUND
            window hide
            $ renpy.pause(3.0, hard=True) 
            scene bg black
            with wipeleft
            scene kbbqinterior1
            with wipeleft
            $ renpy.pause(1.0, hard=True)    
            window show
            kris "ughhh... damn im full...."
            kris "(koreans eat so much... jesus the food portion was so big)"
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.6))
            show srik0104:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.6))  
            $ renpy.pause(3, hard=True) 
            ####<<<<<<<<< PLAY GRILLING SOUND
            kris "(HUHH??? THEYRE COOKING MORE???)"
            kris "How are you guys not full??"
            kris "Im pretty much stuffed!"
            girl4 "Well, we do love beef so..."
            kris "(Ughh... i wanna try beef too! But Ghandi is going to slice my head off even if i just touch it.)"
            kris "(Mmmm.... Ghhhh..... Tch.....!)"
            hide srik0104
            show srik0204:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.6))  
            $ renpy.pause(0.4, hard=True) 
            girl3 "{cps=40}{=koreatext}(그가 원하는 것 같아요?){/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext}(네,하지만 그의 종교는 그를 허용하지 않습니다.){/=koreatext}{/cps}"
            kris "(Grrr.... I really want to eat beef!!! I just felt full 2 minutes ago, but now this is making me hungry again!!)"
            girl4 "{cps=40}{=koreatext}(그는 정말로 일부를 원합니다 ...){/=koreatext}{/cps}"
            girl3 "{cps=40}{=koreatext}(네가 옳아....){/=koreatext}{/cps}"
            girl4 "{cps=40}{=koreatext}(꽤 귀엽다 ...){/=koreatext}{/cps}"
            girl3 "{cps=40}{=koreatext}(네 ... 그는 좋은 남편을 만들 수 있습니다 ...){/=koreatext}{/cps}"
            hide syuz0101
            show syuz0117:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.3))
            girl4 "{cps=40}{=koreatext}(내가 그렇게 생각하게하지 마라!){/=koreatext}{/cps}"
            hide srik0204
            show srik0205:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.3))
            girl3 "{cps=40}{=koreatext}(당신을 보면! 당신은 홍당무입니다!){/=koreatext}{/cps}"
            kris "(Hm...?)"
            kris "(Why are they looking at eachother?)"
            kris "What are you guys doing? Telepathically communicating?"
            girl4 "its nothing..."
            hide srik0205
            hide syuz0117
            $ renpy.transition(Dissolve(0.3))
            window hide
            $ renpy.pause(0.4, hard=True) 
            scene bg black
            with wipeleft
            scene nightkor
            with wipeleft
            $ renpy.pause(1.0, hard=True)   
            window show
            kris "Ughh..... im so tired. I dont think i can drive to the demon realm like this..."
            show syuz0101:
                linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.6))
            show srik0104:
                linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.6))  
            $ renpy.pause(1, hard=True) 
            girl4 "Then we'll drive!"
            kris "Yea sure...."
            kris "do whatverr yuo wahnt...."
            kris "uhgg.h....."
            girl4 "You are really tired huh?"
            kris "yaeh......"
            window hide
            scene bg black
            with irisin
            $ renpy.pause(3.0, hard=True)
            scene castleintdark
            with irisout
            $ renpy.pause(1.0, hard=True)
            window show
            kris "huh???"
            window hide
            $ renpy.pause(1.0, hard=True)
            ##<<< LIGHTSWITCH SOUND
            scene castleint
            $ renpy.pause(0.6, hard=True)
            kris "Where am i?"
            jump demonactualcastle
        label demonactualcastle:
            window hide
            scene bg black
            with wipeleft
            scene castleint
            with wipeleft
            $ renpy.pause(1.0, hard=True)   
            kris "Ugh..."
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            json "Yo. You're finally here."
            json "You're lucky those 2 were there to pick you up."
            json "How was the car?"
            kris "Bro it was trash! Well..."
            json "Hmmm, well those 2 told me you drift raced an RX-7."
            json "How did that go?"
            kris "I won that race."
            json "Oh really? Well that's cool."
            if wenttobbq == 1:
                kris "Yea, but i ended up falling asleep after i ate some BBQ with those two."
                kris "Do you know what happened to me after?"
                json "No idea. You'll have to ask them."
            else:
                kris "Yea, well i had to sit in the back of the truck bed."
                json "Oof. Tough."
            json "Well, let's go to the planning room."
            kris "Planning room?"
            json "Yup. We gotta discuss our plan."
            kris "Plan for what?"
            json "You'll see."
            hide jasonnorm
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            window hide
            jump planroom
        label planroom: 
            scene bg black
            with wipeleft
            scene castle2
            with wipeleft
            $ renpy.pause(1.0, hard=True)   
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            json "Alright, well let's get started real quick."
            hide jasonnorm
            show smay0101:
                linear 0.0 xalign -0.1
            show ssuo0101:
                linear 0.0 xalign 0.3
            show srik0101:
                linear 0.0 xalign 0.7
            show syuz0101:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            kris "..."
            kris "(jesus!!! 4 of them in front of me!!!)"
            kris "(ok... gotta calm down....)"
            hide smay0101
            hide ssuo0101
            hide srik0101
            hide syuz0101
            show jasonnorm:
                linear 0.0 xalign -47.0
            show kylenorm:
                linear 0.0 xalign -11.3
            show kevinnorm:
                linear 0.0 xalign 10.7
            show cadedis:
                linear 0.0 xalign 17.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            kris "(maybe if i dont focus on the girls ill be calmer...)"
            kris "So... what's the plan?"
            hide jasonnorm
            hide kylenorm
            hide kevinnorm
            hide cadedis
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            json "We're going to Somalia"
            json "And Kristik youre also going to meet 4 new people when we get there."
            kris "Cool. I don't really know why you need to tell me that but okay...."
            json "Anyways, we'll be meeting up over there and give our briefing at a nearby base."
            json "But ill explain the plan right now."
            json "Asami and Michiko will be flying a F/A-18F giving air support and holding off incoming Hostiles. They will be accompanied with a fleet F-16Cs and F-14B Tomcats to help remove any flankers."
            json "Hui Young and Chung Cha will be coordinators for the fleet and for ground support."
            json "Kristik you're coming with us 4, in M1 Abrams and you will most likely be controlling the main gun."
            json "You will be joined with a fleet of the them so do not worry about that."
            json "I will be driving in the tank you're going to be in."
            json "The other 3 will be doing good ol' Vietnam fighting, hide in holes and shoot people who go over them, place mines on the ground and blow them up, etc."
            kris "So, how is this going to help with capturing Aaron, Bill, Welsey and Callin?"
            json "This is one of their main hubs. This location in particular has almost no citizens and are mostly bandits from their clan."
            kris "If they're just bandits, why do we ned such overkill weaponry?"
            json "They are armed and dangerous. They have one such weapon we do not have."
            kris "What is it?"
            json "Its the smell of their poop."
            kris "(wtf??? how is that a weapon?)"
            kris "But I still have one question."
            json "What is it?"
            kris "Those 4 people im gonna meet, who are they?"
            json "You don't need to worry about that. You'll get to know them once we get there."
            hide jasonnorm
            show smay0118:
                linear 0.0 xalign -0.1
            show ssuo0105:
                linear 0.0 xalign 0.3
            show srik0212:
                linear 0.0 xalign 0.7
            show syuz0117:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kris "(???????)"
            kris "Uhhh..."
            kris "What's with the pensiveness?"
            girl4 "Just for your information.... those 4 new people you're going to meet are girls..."
            girl2 "Yeah..."
            kris "(so??? who cares?)"
            kris "But what's the big idea about it?"
            kris "I don't really care if they're girls or guys..."
            hide smay0118
            hide ssuo0105
            hide syuz0117
            hide srik0212
            show syuz0113zoom
            show syuz0113zoom
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1.0, hard=True) 
            girl4 "It's already getting competitive between us 4! Imagine having 4 NEW girls!"
            kris "Competitive??? What are we playing counter strike?"
            girl4 "Ughh..."
            hide syuz0113zoom
            show smay0118:
                linear 0.0 xalign -0.1
            show ssuo0105:
                linear 0.0 xalign 0.3
            show srik0212:
                linear 0.0 xalign 0.7
            show syuz0117:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl1 "Anyways... let's hurry up and get this plan started!"
            json "The flight to Somalia isn't until 4 days from now."
            girl1 "Well, whatever."
            hide smay0118
            hide ssuo0105
            hide syuz0117
            hide srik0212
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            json "Right, so, Kristik."
            kris "Yeah?"
            json "Since the flight won't be till 4 days from now, you can do anything you want right now."
            kris "(hmmm... maybe jack off?)"
            json "So you guys are all dismissed. I'm hungry as fuck and I need some pho or something."
            hide jasonnorm
            show syuz0206
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            girl4 "Hey Kris want to get something to eat together?"
            kris "Uh.. sure i guess..."
            hide syuz0206
            show smay0111:
                linear 0.0 xalign 0.03
            show ssuo0107:
                linear 0.0 xalign 0.5
            show srik0109:
                linear 0.0 xalign 1.0
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl2 "Hey no fair!"
            girl2 "Why can't I come too?"
            hide srik0109
            hide ssuo0107
            hide smay0111
            show syuz0113
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            girl4 "Hey no! He's mine only!! Right honey~~?"
            hide syuz0113
            show syuz0206
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            kris "(WTF??? HONEY???)"
            kris "(IM NOT HER PROPERTY!)"
            kris "Um... Uhhh...."
            kris "I really don't know what to say to that..."
            girl4 "Awww cmon I know you're head over heels in love with me."
            kris "(if im going to be honest, im neutral with this girl.)"
            kris "(im definitely NOT saying that out loud cause a girl's emotions are as fragile as a rusted piece of 1 milimeter thick iron)"
            hide syuz0206
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True)
            json "Alright guys, take this argument somewhere else. I gotta fap to some viet hentai"
            hide jasonnorm
            window hide
            scene bg black
            with wipeleft
            scene outside
            with wipeleft
            $ renpy.pause(1.0, hard=True) 
            window show
            kris "Huh... this place looks surprisngly similar to Japan."
            show smay0214:
                linear 0.0 xalign -0.1
            show ssuo0103:
                linear 0.0 xalign 0.3
            show srik0103:
                linear 0.0 xalign 0.7
            show syuz0116:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl4 "So what do you want to do Kristik?"
            hide syuz0116
            hide srik0103
            hide ssuo0103
            hide smay0214
            show syuz0206
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl4 "Do you want to go on a date with just me?"
            kris "Uh..."
            hide syuz0206
            show smay0111:
                linear 0.0 xalign 0.03
            show ssuo0107:
                linear 0.0 xalign 0.5
            show srik0109:
                linear 0.0 xalign 1.0
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl2 "Grrr....."
            girl2 "Hey! Stop acting like he's your boyfriend or something!"
            hide srik0109
            hide ssuo0107
            hide smay0111
            show srik0108
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl3 "Just cause she's my friend that doesn't mean she gets a freebie from me!"
            kris "Wait I thought you couldn't speak English?!!"
            girl3 "I only did that so she could get into you!"
            girl3 "But now I'm going to win over your heart!"
            hide srik0108
            show srik0109:
                    linear 0.0 xalign 0.8
            show syuz0110:
                    linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl4 "Huh??? You think you could challenge me???"
            girl3 "Yeah!! I will be the one to win his heart!"
            hide syuz0110
            hide srik0109
            show smay0111:
                    linear 0.0 xalign 0.8
            show ssuo0107:
                    linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl2 "Hey don't forget about us!"
            girl1 "Yeah! Give some attention to us Kristik!"
            kris "(Ahhh shit this is getting too intense!!)"
            hide ssuo0107
            hide smay0111
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            mys "Whats with the commotion?"
            $ renpy.pause(1.2, hard=True) 
            show sner0101:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            mys "What are you guys arguing about?"
            kris "(BRUH)"
            kris "(MORE GIRLS???)"
            hide sich0101
            hide sner0101
            show srik0116:
                    linear 0.0 xalign 0.8
            show syuz0102:
                    linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl4 "Hannah??? And Chiyoko??"
            girl3 "What are you two doing here??"
            girl4 "You're supposed to be in Somalia!"
            hide syuz0102
            hide srik0116
            $ renpy.transition(Dissolve(0.4))  
            show sner0101:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kris "(Hannah??? Chiyoko???)"
            girl5 "Yeah, but me and Chiyoko decided to come here to just check out the place. The plan wont be carried out until 2 days after you arrive."
            girl6 "Yeah, What's wrong with us being here?"
            hide sich0101
            hide sner0101
            $ renpy.transition(Dissolve(0.4))  
            show smay0118:
                linear 0.0 xalign -0.1
            show ssuo0105:
                linear 0.0 xalign 0.3
            show srik0212:
                linear 0.0 xalign 0.7
            show syuz0117:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl2 "Nothing!! It's nothing!!"
            girl3 "Yeah... its nothing... you shouldnt worry about us too much!"
            hide smay0118
            hide ssuo0105
            hide syuz0117
            hide srik0212
            $ renpy.transition(Dissolve(0.4))  
            show sner0204:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Does it by any chance have to do with this boy right here?"
            girl6 "Hooo! Is he dating all 4 of you?!"
            hide sich0101
            hide sner0204
            $ renpy.transition(Dissolve(0.4))  
            show smay0118:
                linear 0.0 xalign -0.1
            show ssuo0105:
                linear 0.0 xalign 0.3
            show srik0212:
                linear 0.0 xalign 0.7
            show syuz0117:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl2 "What?? No!! Who would date such a weird kid!"
            girl4 "Says the girl that IS a kid..."
            hide smay0118
            hide ssuo0105
            hide syuz0117
            hide srik0212
            $ renpy.transition(Dissolve(0.4))  
            show sner0204:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Hmmm? If that's the case can I date him?"
            girl6 "I don't know Hannah, you'd have some serious competition between me!"
            hide sich0101
            hide sner0204    
            $ renpy.transition(Dissolve(0.4))  
            show srik0109
            $ renpy.transition(Dissolve(0.4))
            girl3 "No! You cannot! He's mine!"
            hide srik0109
            show syuz0110
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl4 "Huh? Who thinks that he would be with you? He's obviously dating me!"
            kris "(jesus christ this is getting insane!!!!)"
            hide syuz0110
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            bystander1 "Wow... he's got quite a bit of ladies!"
            bystander1 "How come you can't get that many girls Iachima-kun?"
            bystander2 "Hey! He's just lucky i guess... and besides i already have a girl and its you..."
            bystander1 "Hohoho! Well it's a good thing you only have me! Or else I would be terribly jealous~~"
            bystander2 "ugh... dont say that too loud..."
            bystander1 "Its okay~~ Nobody can hear us!"
            kris "(I totally heard that!)"
            show sner0204:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Hey! Wanna come with us? Its a bit too public out here."
            girl6 "Yeah Yeah! Come with us!"
            hide sich0101
            hide sner0204  
            show smay0111:
                linear 0.0 xalign -0.1
            show ssuo0107:
                linear 0.0 xalign 0.3
            show srik0109:
                linear 0.0 xalign 0.7
            show syuz0117:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl2 "We're gonna come to."
            girl4 "Yeah. Who knows what kind of fishy stuff that pervert could do."
            kris "(pervert?!??!?! since when?!?!? i never even did such things to you guys!!)"
            hide syuz0117
            hide srik0109
            hide ssuo0107
            hide smay0111
            show sner0204:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Well, if you insist..."
            kris "(UGhh.... i have no idea what im gonna do with these 6 girls...)"
            hide sich0101
            hide sner0204  
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            window hide
            scene bg black
            with wipeleft
            scene house #####################################<<<<<<<<<<<<<<CHANGE THIS
            with wipeleft
            $ renpy.pause(1.0, hard=True)   
            show sner0101
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            girl5 "We're here!"
            kris "(why is literally everybody else literally richer than me???!!!)"
            hide sner0101
            show sich0101
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl6 "So... who are you?"
            kris "Uhh.... its a bit complicated... Im pretty sure even those 4 dont even know my history with Jason and the other guys..."
            girl6 "Hmm.. sounds interesting!"
            hide sich0101
            show sner0204:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Tell us about your history with them!"
            girl5 "Sounds sort of bad if im going to be honest..."
            hide sich0101
            hide sner0204  
            show smay0214:
                linear 0.0 xalign -0.1
            show ssuo0103:
                linear 0.0 xalign 0.3
            show srik0103:
                linear 0.0 xalign 0.7
            show syuz0116:
                linear 0.0 xalign 1.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl1 "Now that I think about it... we don't know where you came from..."
            girl4 "Hmmm... Yeah! You always ask me about our history! Why dont you tell us yours?"
            kris "(Uhh shit... its a bit weird but ill try...)"
            kris "Well.... this is what happened...."
            window hide
            scene white
            $ renpy.transition(Dissolve(2.4))  
            $ renpy.pause(3.2, hard=True) 
            e "Skipping has been enabled. The skip feature is used to skip Kristik Saga 1 .{p=2.0}{nw}"
            e "You can press the TAB key or press the skip button to skip all text until Kristik Saga 1 is done.{p=3.0}{nw}"
            window hide
            scene krissag1
            $ renpy.transition(Dissolve(2.4))  
            $ renpy.pause(2.4, hard=True) 
            $ _skipping = True
            kyle "Hostile located on the second floor. Apparently he's got a hostage."
            kyle "You see anything up there Cade?"
            hide krissag1
            show krissag2
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            cade "Affirmative. We have the target in sight. He's in a bedroom, left side of the hallway, 3 doors from the stairs."
            kyle "Roger, Wilco."
            hide krissag2
            show krissag1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kev "Sir this is the FBI! Open your door now!"
            kris "..."
            window hide
            #######<<<<<<PLAY DOOR BUST SOUND
            $ renpy.pause(1.2, hard=True) 
            window show 
            kyle "Let's move lets move!"
            hide krissag1
            $ renpy.transition(Dissolve(0.4))  
            show krissag3
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kyle "We have you surrounded!"
            kev "Put your hands up in the-"
            kris "OhhHHHhHH YeS!!! oMG!!!!!!!! oOoOooOoOH!!!"
            kev "...."
            hide krissag3
            $ renpy.transition(Dissolve(0.4))  
            show krissag4
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kev "EWWWWWWWWWWWWWWWWWW!!!!!!!!! WTFFFFFFFFFFFFFFFFFF"
            kyle "OH MY GOD! THATS DISGUSTING!"
            hide krissag4
            $ renpy.transition(Dissolve(0.4))  
            show krissag2
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            cade "What's going on? Do you need backup?"
            kyle "No no we're fine! Just... OH MY GOD!"
            kev "IM GONNA PUKE!"
            hide krissag2
            $ renpy.transition(Dissolve(0.4))  
            show krissag4
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kyle "SIR WE HAVE YOU SURROUNDED! YOU MUST COME WITH US!"
            kris "Not until i come if you know what i mean ;)"
            kyle "EWWEWEWEWEWEWEWWWWWWWW"
            kris "OoOOooooo!!!!!!!!"
            kris "dam that felt guuuuud"
            kyle "AY!"
            hide krissag4
            show krissag5
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kyle "YOURE COMING WITH US!"
            kris "how did we suddenly change bedrooms"
            kyle "STFU!"
            window hide
            scene bg black
            with wipeleft
            hide krissag6
            scene krissag6
            with wipeleft
            $ renpy.pause(1.0, hard=True)   
            kyle "Looks like you'll be going to the slammer, kid."
            kris "Who you callin kid?"
            hide krissag6   
            show krissag7
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2.2, hard=True) 
            hide krissag7   
            show krissag8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True)     

            cntr "Do you have the target in sight?"
            aar "Yes, target is 12 o 'clock. "
            cntr "Fire Fox 2."
            aar "Fox 2 ! Fox 2!"
            ######<<<<<<<PLAY MISSLE SOUND
            hide krissag8
            show krissag9
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True)     
            aar "We've got a hit. IR Radar is showing a perfect hit."
            cntr "Roger. R2B."
            aar "Wilco."
            hide krissag9
            show krissag10
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)    
            window hide
            scene bg black
            with wipeleft
            hide krissag10
            scene krissag12 
            with wipeleft
            $ renpy.pause(1.0, hard=True)   
            kris "..."
            kris "..."
            hide krissag12
            show krissag13
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True)   
            kris "AUGGH!!!!!"
            kris "AAHHHHHHHHH!!!!!"
            hide krissag13
            show krissag14
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True)  
            kris "HUghh...."
            kris "Ive been reincarnated..."
            kris "I MUST KILL THEM."
            kris "ALL OF THEM."
            window hide
            scene bg black
            with wipeleft
            hide krissag14
            scene krissag15
            with wipeleft
            window show
            cade "Yo! Whats up?"
            kyle "Hey Cade. Nothing much."
            window hide
            hide krissag15
            show krissag16
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)  
            hide krissag16
            show krissag18
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)  
            hide krissag18
            show krissag19
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)  
            window show
            kev "WHAT?? Its KRISTIK!!"
            kyle "HUH?? HOW ARE YOU ALIVE? I THOUGHT WE BLEW YOU UP WITH AIM-9Xs?"
            cade "Woah. Cool."
            kev "CADE THIS AINT COOL!"
            kris "... Ive been seeking revenge. Satan has reincarted me. I will destroy all of you."
            window hide
            hide krissag19
            show krissag20
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)  
            kev "Woah wait WAIT-"
            ###knife stab sound
            hide krissag20
            show krissag21
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)  
            kris "W̴H̴O̷S̸ ̷N̷E̵X̸T̶?̴"
            hide krissag21
            show krissag22
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.5, hard=True)  
            kyle "You cant be serious! Did you seriously...?"
            hide krissag22
            show krissag23
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.5, hard=True)  
            kris "D̴̞̝͠Ȍ̸͙͝ ̶͉̤͒̈́I̵̩̺̎ ̸͛L̸̀̓O̸̙͝O̷̡̫͋K̶̝̉̂ͅ ̴͎͂͝L̸͚͉̃I̴̮͝K̸̮̞̾̎Ë̵̟́ ̶̞̂I̴̲̤̎Ḿ̷͎̘͂ ̸̢̼́̂J̵̙̜̊͂Ò̸̢̱K̴̖͝I̶̮͘Ñ̴̬G̵̘̺̑̾?̶͐̉"
            hide krissag23
            show krissag24
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.5, hard=True)  
            kyle "(Im gonna shoot this motherfucker!)"
            hide krissag24
            show krissag25
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True)             
            kyle "Engage on him Cade!"
            cade "i dont have my guns"
            kyle "Are you serious????"
            kyle "How could you not-"
            window hide
            hide krissag25
            show krissag27
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1.0, hard=True)   
            hide krissag27
            show krissag28
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1.0, hard=True)   
            kris "C̶̛͚̊H̶͓͚͗͘Ẹ̴͗C̸͉̾̚K̴̞̃M̶̚Ā̴̭̍T̴̲̞̚E̷̥̋.̴͖̋̎"
            hide krissag28
            show krissag29
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.4, hard=True)   
            kyle "Ghh!"
            kyle "Call the others Cade! Hurry up!"
            window hide
            hide krissag29
            show krissag30
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)   
            hide krissag30
            show krissag31
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(2, hard=True)   
            kev "Ive got you now you sunovabi-"
            window hide
            hide krissag31
            show krissag32
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)  
            hide krissag32
            show krissag33
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            ##play 3 headshot sounds
            hide krissag33
            show krissag34
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            kris "Ive done what i need to do."
            window hide
            hide krissag34
            show krissag35
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            hide krissag35
            show krissag36
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            kris "Oh? Who is this?"
            hide krissag36
            show krissag38
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.6, hard=True)
            ###<<< play car door close sounds
            bill "What have you done... KRISTIK LAL!!!!"
            hide krissag38
            show krissag39
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.6, hard=True)
            bill "I WILL AVENGE ALL THREE OF THEM!!"
            hide krissag39
            show krissag42
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.6, hard=True)
            kris "YOU THINK YOU CAN BEAT ME MORTAL?"
            hide krissag42
            show krissag45
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            hide krissag45
            show krissag48
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            bill "YOU WONT BEAT ME KRISTIK LAL!!!"
            hide krissag48
            show krissag50
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            bill "I WILL ACTIVATE MY SECRET POWER!!"
            bill "INDIANBOMB 2.0!!"
            hide krissag50
            show krissag51
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            hide krissag51
            show krissag52
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            kris "N-NANI?!??!?! INDIANBOMB 2.0!!?!?!"
            hide krissag52
            show krissag53
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(1, hard=True)
            kris "AHGGGGGG!!!!!"
            window hide
            scene white
            $ renpy.transition(Dissolve(2.4))  
            $ renpy.pause(3.2, hard=True) 
            $ _skipping = False 
            scene demoend
            $ renpy.transition(Dissolve(2.4))  
            $ renpy.pause(3.2, hard=True) 
            return
            ####################################################################################################################################
            
            ##########################<<<<<<<<<<<<<<<<<END OF DEMO
          
            ####################################################################################################################################             
            
                                                    #label fuckyou:
                                                        #window show
                                                       # kris "Fuck you. I aint doing this shit so kys."
                                                      #  window hide
                                                     #   show screen disable_Lmouse()
                                                    #    hide house
                                                    #    $ renpy.movie_cutscene("expend.ogv")
                                                    #    show end
                                                    #    $ renpy.pause(5.0, hard=True) 
                                                    #    show asamstat "{size=42}{color=#0026ff}[pointsGirl1]{/color}{/size}" onlayer screens
                                                      #  show michstat "{size=42}{color=#0026ff}[pointsGirl2]{/color}{/size}" onlayer screens
                                                  #      show chungstat "{size=42}{color=#0026ff}[pointsGirl3]{/color}{/size}" onlayer screens
                                                    #    show huistat "{size=42}{color=#0026ff}[pointsGirl4]{/color}{/size}" onlayer screens
                                                    #    show hannahstat "{size=42}{color=#0026ff}[pointsGirl5]{/color}{/size}" onlayer screens
                                                    #    show chiyokostat"{size=42}{color=#0026ff}{color=#0026ff}[pointsGirl6]{/color}{/size}" onlayer screens
                                                      #  show chin1stat "{size=42}{color=#0026ff}[pointsGirl7]{/color}{/size}" onlayer screens
                                                   #     show chin2stat"{size=42}{color=#0026ff}[pointsGirl8]{/color}{/size}" onlayer screens
                                                    #    $ renpy.pause(4.0, hard=True) 
                                                   #     return


                                                   ###^^^^^^^END SCENES
