
#   _____ _     _                                           _             
#  / ____| |   (_)                                         (_)            
# | |    | |__  _ _ __   ___  ___  ___  __   _____ _ __ ___ _  ___  _ __  
# | |    | '_ \| | '_ \ / _ \/ __|/ _ \ \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
# | |____| | | | | | | |  __/\__ \  __/  \ V /  __/ |  \__ \ | (_) | | | |
#  \_____|_| |_|_|_| |_|\___||___/\___|   \_/ \___|_|  |___/_|\___/|_| |_|
                                                                         
                                                                         

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
define kris = Character("肥仔", color="#FFFFFF")
define krismind = Character("")
define mom = Character("母親", color="#FFFFFF")
define gui.name_text_outlines = [ (2, "#000000", 0, 0) ]
define gui.dialogue_text_outlines = [ (2, "#000000", 0, 0) ]
define kyle = Character("凱爾", color="#FFFFFF")
define cade = Character("凱德", color="#FFFFFF")
define json = Character("傑森", color="#FFFFFF")
define kev = Character("凱文", color="#FFFFFF")
define bill = Character("Bill", color="#FFFFFF")
define hung = Character("Hung", color="#FFFFFF")
define cntr = Character("任務控制", color="#FFFFFF")
define aar = Character("亞倫", color="#FFFFFF")
define pa = Character("擴聲系統", color="#FFFFFF")
define wes = Character("衛斯理", color="#FFFFFF")
define mys = Character("???", color="#FFFFFF")
define dev = Character("系統管理員", color="#FFFFFF")
define oth = Character("其他人", color="#FFFFFF")
define rx7 = Character("RX7所有者", color="#FFFFFF")
define waiter = Character("侍應生", color="#FFFFFF")
define silver = Character("Salty Silver", color="#FFFFFF")
define fade = Fade(1, 0.3, 1)
define dissolve = Dissolve(1.0)
define att1 = Character("空姐1", color="#FFFFFF")
define att2 = Character("空姐2", color="#FFFFFF")
define girl1 = Character("麻美", color="#FFFFFF", who_font = 'msgothic.ttc')
define girl2 = Character("美智子", color="#FFFFFF", who_font = 'msgothic.ttc')
define girl3 = Character("김충차", color="#FFFFFF", who_font = 'malgunbd.ttf')
define girl4 = Character("樸熙英", color="#FFFFFF", who_font = 'malgunbd.ttf')
define girl5 = Character("漢娜·施羅德", color="#FFFFFF")
define girl6 = Character("千代子", color="#FFFFFF", who_font = 'msgothic.ttc')
define girl7 = Character("袁昌英", color="#FFFFFF", who_font = 'simhei.ttf')
define girl8 = Character("冼东妹", color="#FFFFFF", who_font = 'simhei.ttf')
define clerk1 = Character("印度文員", color="#FFFFFF")
define worker1 = Character("工人", color="#FFFFFF")
define mahneet = Character("印度男孩", color="#FFFFFF")
define bystander1 = Character("旁觀者1", color="#FFFFFF")
define bystander2 = Character("旁觀者2", color="#FFFFFF")
define rem = Character("[版權材料]", color="#FFFFFF")
define pil = Character("主隊長1", color="#FFFFFF")
define firo = Character("主要副駕駛1", color="#FFFFFF")
define allofthem = Character("所有的女孩", color="#FFFFFF")
define gui.choice_text_outlines = [ (2, "#000000", 0, 0) ]
image fire = Movie(channel="movie", play="movies/fires_Trim.ogv")
image end = Movie(size=(1280,720), channel="movie", play="movies/endstat.ogv")
image menuA = Movie(size=(1280,720), channel="movie", play="movies/Untitled.ogv")
image america = Movie(size=(1280,720), channel="movie", play="movies/usaflag.ogv")
image transition1 = Movie(size=(1280,720), channel="movie", play="movies/transitionone.ogv")
image under1 = Movie(size=(1280,720), channel="movie", play="movies/FirstsecOfBattle.ogv")
image underidle = Movie(size=(1280,720), channel="movie", play="movies/idlefight.ogv")
image underattack1 = Movie(size=(1280,720), channel="movie", play="movies/attackattempt.ogv")
image underattack2 = Movie(size=(1280,720), channel="movie", play="movies/attackattempt2.ogv")
image itempage = Movie(size=(1280,720), channel="movie", play="movies/item.ogv")
image actpage1 = Movie(size=(1280,720), channel="movie", play="movies/actpage.ogv")
image underend1 = Movie(size=(1280,720), channel="movie", play="movies/underend.ogv")
image sparepage = Movie(size=(1280,720), channel="movie", play="movies/mercy.ogv")
image blueheart = Movie(size=(1280,720), channel="movie", play="movies/fightblue.ogv")
image somaliaArcintro = Movie(size=(1280,720), channel="movie", play="movies/f16intro.ogv")
define audio.doorslamclose = "audio/doorslamclose.ogg"
define audio.doorslamopen = "audio/doorslamopen.ogg"
define audio.bedsheet = "audio/bedsheetrustle.ogg"
define audio.scnightambience = "audio/scnightamb.ogg"
define audio.airportamb = "audio/airamb.ogg"
define ranguy1 = Character("隨機傢伙1", color="#FFFFFF")
define ranguy2 = Character("隨機傢伙2", color="#FFFFFF")
define rangir1 = Character("隨機女孩1", color="#FFFFFF")
define rangir2 = Character("隨機女孩2", color="#FFFFFF")
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
transform bgslidefast:
    xalign 0.5 yalign 0.99
    linear 0.0 xalign 0.0
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
label splashscreen:
    scene bg black
    show splash
    $ renpy.transition(Dissolve(1.0)) 
    $ renpy.pause(2, hard=True)
    hide splash
    $ renpy.transition(Dissolve(1.0)) 
    $ renpy.pause(2, hard=True)
    #show disclaimer
    #$ renpy.transition(Dissolve(1.0)) 
    #$ renpy.pause(4, hard=True)
    #hide disclaimer
    #$ renpy.transition(Dissolve(1.0)) 
    #$ renpy.pause(2, hard=True)
    return 
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
    e "「肥仔...」"

    e "「喚醒胖男孩！」"

    scene bg bed
    with fade
    play backgroundmusic "audio/Sunshine_Samba.mp3"
    mom "「胖男孩，實際上是早上9點，讓你的屁股下床。」"

    mom "「嚴重的是這些地面上的組織是什麼？」"

    kris "「嗯.....什麼都沒有！這完全不是精液或任何東西！」"

    mom "「哥該死的胖男孩，你需要停止手淫到色情...」"

    kris "「媽你媽！我喜歡自慰！!!」"

    krismind "耶穌基督這個女人是無法忍受的。那女人是我媽媽，哈哈！"
    ##################$ pointsGirl1 = pointsGirl1 + 1 
    ##################kris "Point test [pointsGirl1]"       <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BASIC POINT SYSTEM TEST 

    krismind "我想我就起來..."
    window hide
    play sound bedsheet
    $ renpy.pause(2, hard=True)
    ###############################################################<<<<<<<<<<<<<<<ADD SOUND FOR RUSTLING BEDSHEETS <<<DONE
    window show
    mom "「哦，順便說一下，直到明天早上，互聯網才被切斷。」"
    stop backgroundmusic fadeout 0.0
    play backgroundSFXnoloop "audio/DJ Record Scratch Sound Effect - copyright free sound effects.mp3" 
    krismind "什~麼？！"
    play backgroundmusic "audio/As Tall As Lions - Maybe I'm Just Tired.mp3"

    kris "「不!!!!我將如何向最熱的印度女孩致敬！？！??！？！？」"
    kris "「我的生活...被毀了！！！」"
    kris "「我無法在這個世界上生存！」"
    kris "「這個世界沒有生命！」"
    kris "「抱歉，媽媽...但是我確定您會理解的。」"
    kris "「這很簡單！」"
    stop backgroundmusic fadeout 0.0
    mom "「哈哈！我剛才是開玩笑的！瞧瞧你，你看起來真傻！!!!哈哈哈哈哈哈！！！！wwwwwwwww」"

    kris "..."
    
    kris "「什麼？？！？！？！？！？！」"
    kris "「您想告訴我那是個笑話!!!!!!!!!???」"
    play backgroundmusic "audio/The Price is Right theme song.mp3"
    mom "「恭喜！！！您獲得了互聯網淘汰活動中最過激的響應獎！！！」"
    mom "「哈哈哈哈wwwwwwww 你的反應真是太可笑了！！！」"

    kris "「閉上媽！！！並關閉該死的音樂！」"
    window hide
    play backgroundSFXnoloop "audio/eject.ogg"
    stop backgroundmusic fadeout 0.0
    $ renpy.pause(2, hard=True)
    window show
    kris "該死的我媽媽真是個妓女..."

    kris ". . ."

    kris "我，Callin，Kyle，Cade，Jason和Kevin之間的戰鬥已經過去了6年。"

    kris "...從我死於攝入尿液已經6年了..."

    kris "無論如何都沒關係……我的女友來找我複活了！！！!"

    kris "然後她離開了我... ( ≧Д≦)"

    kris "我現在要手淫...我應該嗎？？？"

    play audio "audio/popup.ogg"
    menu:
        "自慰到前女友":
            play audio "audio/choiceconfirmed.ogg"
            jump j1
        "跳過手淫":
            play audio "audio/choiceconfirmed.ogg"
            jump j2
    label j1:
        kris "「嗯，為什麼不呢？讓手淫！！！」"
        mom "「什麼？你要自慰嗎？好吧，我不在乎。」"
        kris "「媽媽在這裡滾蛋！」"
        kris "「我需要手淫！！！馬上！！！」"
        window hide
        jump sc1
    label j2:
        kris "「不...跳過手淫。我得去學校了！」"
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
        kris "「嗯...現在在學校。」"
        kris "「等待。 WTF ??? 」"
        kris "「從晚上9點到上午9點！」"
        kris "「天哪，媽媽，你該死！」"
        kris "「等等，我怎麼沒注意到我來這裡的時候...？好吧，無論如何，都會把一些人帶到這裡」"
        stop backgroundmusic fadeout 1.0
        show kylenorm
        $ renpy.transition(Dissolve(1.0)) 
        $ renpy.pause(2, hard=True)
        kris "..."
        stop backgroundmusic fadeout 1.0
        mys "..."
        kris "「凱爾????!!!」"
        kyle "「肥仔???????!!」"
        show kylenorm
        hide kylenorm
        show kylemad
        play backgroundmusic "audio/bgmusic9.ogg"
        kris "「你在幹什麼？？？」"
        kyle "「我想問一問關於你的事情！」"
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
            kris "「從什麼時候開始上Independence高中？我以為你去了更臭的學校。」"
            kyle "「操你這個傢伙，你黑鬼還不-」"
            kris "「哇，哥們，如果你說完我就要取消你了」"
            kyle "「狗屎...隨便...」"
            kyle "「反正...你還活著嗎？您因喝了比爾的小便而喪生，而奧巴馬來祝賀我們。」"
            kyle "「您告訴我，奧巴馬無緣無故被習近平開槍？？我們都哭了，看著日落。」"
            kris "「是，我知道...」"
            kyle "「怎麼樣？？？？事情發生的時候你已經死了...」"
            kris "「我剛剛在洪的HoboNuocMam看了故事的其餘部分。服務器位於https://discord.gg/9NcD7S6」"
            kyle "「什麼？？？你在說什麼？？」"
            kris "「沒關係...」"
            kris "「只是好奇，之後發生了什麼？我記得有個叫Helixiate的孩子，或者任何抱怨沒有學分的人。」"
            kyle "「嗯，沒什麼。在那之後，我們剛剛去了狂歡。然後我們回家了。」"
            kris "「「什麼？？？但是據我所知，arwasairl和KIDOMARU並沒有在ROBLOX工作室中為你們的房子建模...」"
            kyle "「你到底在說什麼你咖哩可卡因高嗎？」"
            kris "「再也不要介意...」"
            jump sc4
        label sc4:
            kris "「嗯，那幫其他人在哪裡？」"
            kyle "「?？哦，他們現在在聖何塞。」"
            kris "「顯然，笨蛋」"
            kris "「我的意思是他們在哪裡」"
            kyle "「好吧，我怎麼知道？」"
            kyle "「傑森（Jason）可能又在酒吧昏倒了……最近他喝了很多酒。」"
            kris "WTF???"
            stop backgroundmusic fadeout 1.0
            kris "「是什麼原因？」"
            play backgroundmusic "audio/bgmusic10.ogg"
            kyle "「傑森最近承受了很大的壓力。他一直在和其他人打交道，所以他整天都在抽煙萬寶路（Marlboro Golds）和喝喜力和百威啤酒。」"
            kyle "「有時候，他喜歡用那個裂紋頭（Hung）擊打……。他也和他一起抽大麻。」"
            kyle "「我曾經參加（Jason's）和（Hung's）的聚會。他們禁用了所有煙霧警報器，以使消防部門不會阻止他們的煙霧狂歡。」"
            kyle "「他們還在抽大麻的同時邀請了脫衣舞孃，然後（Hung）最後把他們全部操了。傑森（Jason）通常是將可卡因外包並帶來一些。」"
            stop backgroundmusic
            play backgroundmusic "audio/bgmusic9.ogg"
            kyle "「那天耶穌太狂野了！」"
            kyle "「儘管（Jason）不再服用可卡因。我想他現在才喝酒。他還停止吸煙，所以我想那很好。」"
            kris "「該死的他媽的什麼？這些壓力從何而來？」"
            kyle "「很可能是他的工作。」"

            kris "「耶穌...好吧，我最好換個話題...」"
            kris "「你知道我可以和任何熱小雞發生性關係嗎？」"
            kyle "「不，我為什麼呢？」"
            kyle "「只是邀請一些脫衣舞孃到你家。」"
            kris "「不，不是妓女。我的意思是說，就像一個熱辣的純潔女孩，她不會四處走動，被她看到的每一個雞巴操。」"
            stop backgroundmusic fadeout 1.0
            stop backgroundSFX fadeout 1.0
            hide kylenorm
            show fire
            hide bg sc
            ###############################################################<<<<<<<<<<<<<<<ADD FIRE NOISE
            show kylebruh
            kyle "「我認為我的女朋友很好，但是在地獄我絕對不會讓你與她發生性關係。如果您這樣做，我真的會割裂您的肺並將其餵給您。」"
            hide fire
            hide kylebruh
            show bg sc
            show kylenorm
            play backgroundmusic "audio/bgmusic6.ogg"
            kris "「該死的你該死的...我什至沒有在談論和你的女朋友做愛...」"
            kyle "「那你為什麼問我？我已經有一個女朋友了，為什麼我要積極尋找女孩？」"
            kris "「我不知道，閉嘴好吧，我沒那麼想」"
            kyle "「你幾乎從來沒有想過」"
            kris "-_-"
            kris "「好吧，你有一個認識蕩婦的朋友嗎？」"
            kyle "「如果你要稱呼你未來的女朋友是個蕩婦，那就不要期望與任何女孩發生性關係」"
            kris "「隨便...我會自己找到一個女孩的。」"
            kyle "「哈哈..."
            kyle "「哈哈哈哈哈哈哈...」"
            kyle "「哈哈哈哈哈哈哈哈哈哈哈哈哈哈!!!!!!wwwwwwwwwwwwwww」"
            kyle "「你真的很有趣」"
            kris "「我不是在開玩笑」"
            kyle "「我不相信你」"
            kyle "「好吧，我一定要去某個地方。」"
            kris "「你要去哪裡？」"
            kyle "「我要去「Orchard School」。我需要在壁球場上噴些塗鴉。」"
            kris "「為什麼？？？」"
            kyle "「好吧，我和其他一些人已經組成了氏族，所以我們只是在標記我們的領土。」"
            kris "「那個狗屎是非法的！」"
            kyle "「誰在乎？」"
            kyle "「隨便我怎麼走。」"
            kris "「我想我也會去...」"
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
            kyle "「好吧，我們在這裡」"
            kris "「是的」"
            kyle "「我帶來了一些噴漆。」"
            kris "「老兄，這狗屎是非法的！」"
            kyle "「我看起來喜歡嗎？」"
            stop backgroundmusic
            play backgroundmusic "audio/US National Anthem Earrape.mp3"
            hide kylenorm
            show america
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(0.2, hard=True)
            show kylenorm
            kyle "「I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in secret raids on Al-Quaeda, and I have over 300 confirmed kills.」（美國笑話）"
            kyle "「I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target.」（美國笑話）"
            kyle "「I will wipe you out with precision the likes of which has never been seen before on this Earth, mark my words. You think you can get away with saying shit to me?」（美國笑話）"
            hide america
            stop backgroundmusic
            play backgroundSFXnoloop "audio/DJ Record Scratch Sound Effect - copyright free sound effects.mp3" 
            kris "「好的，從字面上停止Navy Seals Copypasta，我聽說這個狗屎已經像5,000,000次了」"
            play backgroundmusic "audio/bgmusic9.ogg"
            kyle "「達到5,000,001次」"
            kris "-_-"
            kris "「我厭倦了聽到那屎...」"
            kris "「反正我很無聊，想做什麼？」"
            kyle "「為什麼？你以為我們還是你的朋友？」"
            kyle "「您實際上是在警察局和我們入侵您的基地時試圖殺死我們」"
            kris "「嘿，這還不是全部！」"
            kris "「如果你只是突襲我的基地，我顯然會做些什麼」"
            kris "「我只是試圖在警察局刺你們，因為你們突襲了我的房子，把我帶進了監獄」"
            kris "「然後Aaron裝備了F / A-18C，並用AIM-9X響尾蛇將整個炸毀」"
            kris "「所以我當然會生氣」"
            kyle "「你為什麼要殺死我們？你不應該殺死亞倫嗎？」"
            kris "「好吧，他不在Kristik Saga 1或Kristik Saga 2中，所以我沒有太多事情要做」"
            kyle "「我不知道你在說什麼」"
            stop backgroundmusic fadeout 1.0
            label asami:
                window show
                hide kylenorm
                $ quick_menu = True
                scene bg sj
                show kylenorm
                $ persistent.meetAsami = True
                mys "「嘿!」"
                kris "那是誰？"
                hide kylenorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                play backgroundmusic "audio/bgmusic3.ogg"
                show girlnorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                mys "「你們知道N37°32 57.1 E126°57 35.7在哪裡嗎？」"
                hide girlnorm
                #$ renpy.transition(Dissolve(0.3))
                #$ renpy.pause(0.2, hard=True)
                show kylenorm
                #$ renpy.transition(Dissolve(0.3))
                #$ renpy.pause(0.2, hard=True)
                kyle "「你是誰？」"
                kyle "「順便說一句，為什麼女孩看起來與男孩不同？」"
                kris "「喲它的女孩！」"
                kyle "「我不在乎」"
                kris ".-."
                ####################################################################################################################################kris "{cps=40}FOR INTITAL D SCENES.{/cps}{p=1.0}{nw}"
                kris "「我要去跟她說話」"
                kyle "「你對女孩一無所知！」"
                hide kylenorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                show girlnorm
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                mys "..."
                kris "「你好嗎~ 女孩~~」"
                kris "「那你想和我出去嗎？」"
                hide girlnorm
                show girlmad
                mys "「嗯？」"
                kris "「恩...恩...恩...」"
                hide girlmad
                $ renpy.transition(Dissolve(0.4))
                $ renpy.pause(0.3, hard=True)
                show kylenorm
                $ renpy.transition(Dissolve(0.4))
                $ renpy.pause(0.3, hard=True)
                stop backgroundmusic
                play backgroundmusic "audio/bgmusic1.ogg"
                kris "「我做不到！我太害怕了！」"
                hide kylenorm
                $ renpy.transition(Dissolve(0.2))
                show kylebruh
                $ renpy.transition(Dissolve(0.2))
                kyle "「我就知道。你真的對女孩不好。」"
                kris "「請給我有關如何接女孩的建議！」"
                hide kylebruh
                $ renpy.transition(Dissolve(0.3))
                #with irisin
                $ renpy.pause(0.3, hard=True)
                show girllookaway
                $ renpy.transition(Dissolve(0.3))
                $ renpy.pause(0.3, hard=True)
                mys "「嗯，我想我應該去...」"
                kris"操！該死，我為什麼這麼遲鈍？"
                kris "「哦，是的...哈哈....你看起來很忙...」"
                hide girllookaway
                show girlmad
                mys "「你為什麼這麼奇怪？」"
                play backgroundSFXnoloop "audio/lol.wav"
                kris"OOF"
                kris"自信心被破壞"
                kris "「恩，是的... UHHHHH ....」"
                mys "「是的...我要走了。」"
                stop backgroundmusic fadeout 1.0
                hide girlmad
                $ renpy.transition(Dissolve(0.3))
                $ renpy.pause(0.3, hard=True)
                krismind "..."
                show kyledis
                $ renpy.transition(Dissolve(0.6))
                $ renpy.pause(1, hard=True)
                play backgroundmusic "audio/bgmusic2.ogg"
                kyle "「真是太失敗了。」"
                kyle "「我認為您不會以這樣的速度娶妻。」"
                kris "「閉嘴」"
                hide kyledis
                $ renpy.transition(Dissolve(0.2))
                show kylebruh
                $ renpy.transition(Dissolve(0.2))
                kyle "「哈哈哈哈哈哈哈哈!!!! wwwwwwwwwwwwwwwwwwwwww」"
                kyle "「你跟一個女孩說話，陰莖勃起！」"
                kris "「啊！閉嘴，你為什麼大聲喊？」"
                hide kylebruh
                $ renpy.transition(Dissolve(0.2))
                show kylemad
                $ renpy.transition(Dissolve(0.2))
                kyle "「不要告訴我閉嘴！！！」"
                kris "「，您在喊我的陰莖勃起！」"
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
                kris "...我以為她必須走？為什麼她看起來很尷尬？"
                show girlemblookatplyr
                kris "..."
                kris "「嗯...」"
                show girlembmad
                mys "「你盯著什麼？你個傻冒！」"
                kris "????????"
                kris "為什麼她突然這樣表現？？？"
                hide girlembmad
                show girlemblookatplyr
                kris "「嘿，你還好嗎？你的臉超級紅。」"
                hide girlemblookatplyr
                show girlembmad
                mys "閉嘴！我沒問你！"
                e "!!!!!"
                kris "該死...如果我再說什麼我可能永遠成為處女..."
                kris "我要做點什麼"
                window hide
                play audio "audio/popup.ogg"
            menu:
                "跟她說話":
                    play audio "audio/choiceconfirmed.ogg"
                    $ persistent.touchedAsami = 2
                    jump l1
                "走開":
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
            scene bg sj at bgslidefast
            show girlembmad
            hide girlemb
            kris "嘿，你病了嗎？你這人怎麼回事？"
            $ pointsGirl1 += 1
            mys "沒有什麼是錯的！！！別-"
            hide girlembmad
            show girlemblookatplyr
            kris "嗯，你似乎沒有發燒..."
            mys "..."
            hide girlemblookatplyr
            show girlemb
            mys "沒有..."
            mys "嗯，我現在要走了。"
            window hide
            hide girlemb 
            $ renpy.transition(Dissolve(0.6))
            $ renpy.pause(2, hard=True)
            window show
            krismind "（那是關於什麼的？）"
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
            kyle "他媽的什麼？！"
            kris "??????"
            kris "什麼？？"
            kyle "你退休了嗎？！！"
            kyle "她顯然對您有興趣！"
            kris "是什麼讓你這麼說？"
            hide kylemad
            show kylebruh
            kyle "天哪...該死的傻瓜..."
            hide kylebruh
            show kylemad
            kyle "您甚至都沒有問她的名字！"
            hide kylemad
            show kylebruh
            kyle "你真他媽的幸運她喜歡你...否則你就碰了她"
            kris "聽起來很糟糕...等等，你怎麼知道？"
            kyle "..."
            hide kylebruh
            show kylemad
            kyle "我出去了。我放棄了這個狗屎！"
            kris "等待！！ wtf ..."
            stop backgroundSFX fadeout 1.0
            hide kylemad
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1.2, hard=True)
            krismind "他怎麼了?"
            window hide 
            $ quick_menu = False
            jump u1
        label l2:
            window show
            hide girlembmad
            $ quick_menu = True
            scene bg sj at bgslidefast
            show girlembmad
            hide girlemb
            kris "是的，沒關係。"
            kris "沒關係。"
            hide girlembmad
            show girlemblookatplyr
            mys "哦..."
            hide girlemblookatplyr
            show girlemb
            mys "好吧再見..."
            krismind "???"
            krismind "（...為什麼感覺我做錯了？）"
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
            kris "啊..."
            mom "那是什麼聲音？你再自慰嗎？"
            kris "沒有媽媽我不是我只是呼吸！"

            kris "一直以為我在自慰..."
            mom "很好，您的父親很喜歡自慰，所以如果您具備這種特質，我不會感到驚訝。"
            kris "媽媽！！！我不需要知道那個！！！"
            play sound doorslamclose
            krismind "（耶穌...她真煩人...）"
            kris "今天凱爾怎麼了？他似乎有點不可思議。"
            kris "不僅那個...那個女孩..."
            kris "那個在學校的女孩……她很奇怪……"
            stop backgroundmusic 
            play sound doorslamopen
            ###############################################################<<<<<<<<<<<<<<<ADD DOOR BUSTING SOUND
            mom "{cps=140}為什麼，您第一次因為她是處女而毀了？{/cps}"
            kris "媽媽！為什麼您要回到我的房間？？？而且我什至沒有做！我幾乎對她說！"
            mom "是的，但是請確保下次再帶。"
            kris "..."
            play backgroundmusic "audio/bgmusic9.ogg"
            kris "避孕套???"
            mom "好吧，我們還不希望您生育孩子。"
            kris "好吧，你是對的...沒有等待！"
            mom "哈哈很好玩"
            play sound doorslamclose
            kris "..."
            krismind "（媽你媽...）"
            kris "好吧，我有點無聊。"
            kris "現在我考慮了一下，除了手淫和玩“鐵拳”，我真的無所事事"
            stop backgroundmusic fadeout 1.0
            window hide
            play backgroundSFX "audio/ringtone.mp3"
            $ renpy.pause(2, hard=True)
            ###################################################################<<<<<<<<<<<<<<<<<<<<< ADD PHONE RINGTONE
            window show
            kris "?？"
            kris "誰在給我打電話？"
            krismind "（該死的可能是印度騙子。...我一點都不知道這個數字）"
            stop backgroundSFX
            kris "我將為您提供認證信息(笑)"
            mys "！好久不見"
            kris "呃錯號再見"
            mys "不要掛斷電話！是我！！！"
            kris "如果你只是說這是我，你如何期望我知道你是誰"
            mys "剛到N30°35 19.4 E114°16 13.2"
            kris "呃....不..."
            kris "就我所知，你可能會殺了我"
            mys "只要到這裡，否則我可能會殺死您"
            kris "????? "
            krismind "（這個傢伙到底怎麼了？）"
            kris "是的...我不知道你是誰..."
            kris "我抬頭看那些坐標，他們在中國武漢"
            kris "我想我寧願被殺死也不願獲得冠狀病毒"
            mom "嘿，胖男孩，有人在門口為您服務！"
            kris "什麼？？？我想告訴一些印度騙子馬上滾蛋！"
            mom "快到這裡！他們想見你！"
            krismind "（他們？）"
            kris "嗨，哥們，我有地方要走，所以見"
            mys "好吧，我們會在你家門口見你"
            play backgroundSFXnoloop "audio/hangup.ogg"
            ##########################################################################<<<<<<<<<<<<<<<<<<<<<< ADD HANGUP NOISE
            krismind "（??? !!!）"
            mom "快點，到這裡來吧！"
            kris "耶穌基督，我要來了！"
            krismind "（他們（？）實際上是來這裡殺我的？？）"
            krismind "（好吧，既然這是我一生中的最後一次機會，我最好還是最後一次自慰...）"
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
            kev "胖男孩到底在哪裡？？？？"
            stop backgroundSFX
            ##<<<STOP FAPPING SOUND
            kev "..."
            kris "..."
            kris "嗯..."
            kev "對不起錯房子"
            hide kevinnorm
            play sound doorslamclose
            kris "..."
            ###<<<<PLAY SOUND EFFECT IDK WHICH ONE YET
            kris"不！ WTFF ？？"
            kris "為什麼看到我自慰的人成為了一個人？？？"
            kris "我被毀了！"
            play sound doorslamopen
            mom "耶穌基督老兄剛剛收拾下樓"
            mom "還記得在Kristik Saga 2中試圖抓住您的人嗎？好吧，他們都在這裡"
            kris "哦..."
            krismind "（該死...所以我無緣無故地自慰....）"
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
            krismind "（該死...他們到底是怎麼找到我的房子的？）"
            show kevindis 
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(1.2, hard=True)
            play backgroundmusic "audio/bgmusic1.ogg"
            kev "！！！ 那真是令人讨厌！"
            krismind "（该死！我最好躲在他们看到我之前）"
            ##<<ADD SOME SORT OF RUSTLING NOISE 
            kev "他觉得自己的印度小茴香觉得我想去那儿后就死了！"
            hide kevindis
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show jasonbruh
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "你应该刚敲门..."
            hide jasonbruh
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show kevinmad
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            kev "我应该怎么知道他在做自慰？"
            hide kevinmad
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            krismind "（该死！现在出来很尴尬...）"
            mom "大家好。 想要饼干吗？"
            krismind "（WTF ??她从不给我饼干...;-;）"
            show kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            kyle "地狱呀！ 印度饼干！"
            ###<<<< ADD ROBLOX NOM NOM NOM SFX
            kyle "*吧唧吧唧吧唧*"
            hide kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            krismind "（我要一些印度饼干！）"
            mom "克里斯蒂克在沙发后面出来，吃了一些饼干。"
            kris "该死...好..."
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "你听到我们了吗？"
            kris "是啊，我做了..."
            show kevinnorm:
                xalign 20.0 yalign 1.0
            $ renpy.transition(Dissolve(0.4))
            show jasonnorm at slideleft2ppl
            kev "确保您洗手，因为我不想吃精子饼干"
            kris "是的，是的...我已经做了..."
            hide kevinnorm
            hide jasonnorm
            show kevinnorm
            kev "用肥皂？"
            kris "是啊，我现在不闭嘴，让我吃掉这个饼干！"
            play sound doorbell
            #<<<< PLAY DOORBELL
            e "..."
            mom "哦，有人在门口"
            kris "我会得到它的"
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
            krismind "嗯WTF ？？？"
            show remtalk
            rem "你好。"
            kris "他妈的什么-{p=0.5}{nw}"
            rem "您是否看到过2020年斯巴鲁WRX Premium CVT？"
            hide remtalk
            show remnorm
            krismind "（她在说谁？？）"
            kris "嗯，我认为他在https://www.emiliamotors.com/"
            hide remnorm
            show remmad
            rem "不好笑..."
            hide remmad 
            show remmadtlak
            rem "因为那个玩笑我会杀了你。"
            krismind "（啊！她为什么这么吓人？？？）"
            hide remmadtlak
            show remmad
            kris "好吧，他不在这里..."
            kris "再见！"
            hide remmad
            play backgroundSFXnoloop "audio/doorclose.ogg"
            scene doorclose
            ###<<<<DOOR SLAM
            $ renpy.pause(2, hard=True)
            krismind "哈..."
            play sound doorbellexc
            $ renpy.pause(2, hard=True)
            ##<< PLAY OVEREXCESSIVE DOORBELL
            krismind "(啊啊啊！)"
            mom "那边发生了什么事？"
            kris "没有！！！"
            kris "这只是一个印度律师！"
            mom "什么？"
            kris "等待！ 妈妈不要开门！"
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
            krismind "（因为我的妈妈会说日语吗？）"
            hide remtalk
            show remtalkhap
            rem "{=japantext}ああなるほど。彼は本当に迷惑です。彼を殺したい♥♥~~{/=japantext}"
            krismind "（以某種方式我認為她在侮辱我...）"
            hide remtalkhap
            show remnorm
            kris "好吧，我猜你們兩個說話...我會和其他人說話。"
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
            kyle "我以為你媽媽是印度人？"
            kris "她是，但我不知道她會說日語"
            kyle "你這裡有一個怪異的家庭"
            kris "是的..."
            kris "無論如何，你們在這裡做什麼？"
            kyle "好...."
            hide kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "比爾，卡林，韋斯利和亞倫都失踪了。"
            kris "所以？？？？ 誰在乎？？？"
            kris "亞倫用AIM 9X響尾蛇把我炸死，我喝了比爾的小便就死了，卡林用劍將我的士兵斬首，韋斯利..."
            kris "衛斯理從來沒有在故事中...關閉"
            json "我們只需要他們，因為他們欠我們錢"
            kris "什麼？？？ 為什麼？？？"
            hide jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            kyle "你知道F / A-18C嗎？ 是的，我實際上是租來的，但是亞倫從來沒有還過我。"
            kyle "比爾欠我錢，因為他答應不小心對我生氣兩次後會給我一些。"
            kyle "卡林欠傑森的錢是因為這把劍實際上是從越南戰爭博物館被盜的，要搶那個地方並不容易。"
            kyle "還有衛斯理....."
            kyle "韋斯利沒用。"
            kris "我們在這裡聊多少錢？"
            kyle "恩，我要說2900萬美元左右"
            kris "WTF???"
            kris "你怎麼有錢？"
            kyle "我很豐富"
            kris "那你能給我買個女朋友嗎？"
            kyle "滾開"
            kris "那麼我們如何找到它們？"
            hide kylenorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.5, hard=True)
            json "好吧，我們用我的壓印機確定了他們的位置。 二，採用OC3光線路。"
            json "我們預計他們的位置在索馬里某處。"
            kris "他們在那裡做什麼？"
            json "大概組建一支軍隊，以便他們可以推翻我們。"
            kris "等一下。 堅持，稍等。"
            kris "他們為什麼這樣做？"
            json "好吧，基本上，在我們成功\"殺死\"您之後，我們就成為了惡魔世界中的新超級大國。"
            kris "真他媽的..."
            json "但是，我們爭論誰應該登上王位。"
            json "我們最終決定是我，因為我是這裡最聰明的人。 /s"
            kris "好吧，我還有大約500萬個問題，但我不想問他們。"
            json "在我成為領導者之後，這四個人開始爭論我是領導者，並威脅要殺死我們所有人。 他們兩天后離開了這個領域。"
            kris "那麼，我們是為了錢還是為了抓住他們而阻止他們成長？"
            json "我都猜..."
            kris "好..."
            kris "他媽的！ 我不想做狗屎！"
            kris "在深入研究這個惡魔狗屎之前，我需要先得到一個女友。"
            json "惡魔世界最多可以給你8個女孩。"
            kris "註冊我！"
            json "wwwwwwwwww"
            kris "所以我從哪裡開始？？？"
            json "我們要進入惡魔世界。"
            kris "等待。 馬上？？！！"
            json "不會。航班將在2天后出發。"
            ###<<<<<<<ADD SOUND EFFECT IDK
            kris "什麼？？？？？？？？？"
            json "最好帶些咖哩，印度男孩。"
            kris "等等...我們怎麼能乘飛機飛到那裡？"
            json "你傻嗎？？？"
            json "惡魔王國就在泰國之下。"
            json "就像三年級的地理..."
            json "好吧，凱爾（Kyle），凱文（Kevin）和阿德（cade）將在聖何塞機場與您會面。 航班於下午2點起飛。"
            hide jasonnorm
            window hide
            scene airportoutside
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            ######<<<<<<<<ADD AIRPORT AMBIENCE
            show jasonnorm
            window show
            json "啊...機場。"
            hide jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            show kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            kyle "我們乘坐什麼航空公司？"
            kris "顯然，我們正在“Southwest Airlines”飛行。"
            hide kylenorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            json "是的，我入侵了SWAlife數據庫並將我們註冊為非轉版，因此我不必為這些門票支付一角錢。"
            kris "好吧，快點趕到那裡，這樣我就可以招到一些女孩！！！"
            window hide
            scene airport
            $ renpy.transition(Fade(1, 0.3, 1)) 
            $ renpy.pause(2, hard=True)
            window show
            pa "請注意，候機樓中的所有乘客都在尋找Southwest 69420以及向魔界提供服務的乘客。 航班已取消。 所有出票的乘客都必須去看領獎台。"
            kris "拉屎！！！ 沒有！！！！！！！！"
            kris "我的辣妹!!!!!!!!!"
            show jasonnorm
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            json "糟透了..."
            json "猜猜我們將不得不等待下一個。"
            kris "下一個航班什麼時候？"
            json "好吧，每1小時就有一個航班，但是航班已經完全載滿。 下一個可用的是3天之內。"
            kris "嗯？？？ 我不能等待三天！！！ 我現在需要進入惡魔世界！"
            mys "有人說惡魔境界嗎？"
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
                girl2 "我可以幫忙。"
                krismind "!!!!!"
                krismind "（這是一個女孩！！！）"
                krismind "等待..."
                krismind "（沒有冒犯，但她將如何提供幫助？）"
                show jasonnorm at slideleft2ppl
                $ renpy.transition(Dissolve(0.2))
                show smay0101 at slideright2ppl
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                json "美智子?!?"
                krismind "他怎麼知道所有的女孩????? !!! ??????"
                kris "你認識這個人嗎？"
                json "是的，她是打印出機票導致我的打印機墨水用完的人。 我也去過她家幾次。"
                krismind "（我從來沒有見過她！）"
                krismind "（啊，老兄...那個女孩被傑森帶走了...。）"
                girl2 "我已經刪除了1航班起飛的69421航班上沒有出現的乘客。 你們應該能夠填補那些空缺。"
                json "好的，謝謝。"
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
                json "好吧，看來我們可以繼續。 我想你可以讓女孩..."
                krismind "（嗯，我心情不太好...現在我知道甚至JASON都有一個女孩...）"
                krismind "（現在我想想...我以前見過的那個女孩怎麼了？我想知道她去哪兒了）"
                json "我們4人將離開以獲得一些星巴克。 我有點渴..."
                kris "（我唯一渴望的是愛呵呵呵呵...。）"
                hide jasonnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show kylenorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                kyle "是的，也許我會換一些Pho。"
                hide kylenorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show kevinnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                kev "他們在這裡有河粉嗎？ 好吧，我的意思是，這是聖何塞。。。。"
                hide kevinnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show cadedis
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                cade "哇...麵條...討厭...麵條太爛了xD !!"
                hide cadedis
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                kris "是的...我想我會再見你們。 根據時間表，下一班航班僅在1號登機口在1小時內。"
                show jasonnorm
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                json "好吧，我們到那兒見。"
                kris "再見"
                hide jasonnorm
                $ renpy.transition(Dissolve(0.5))
                $ renpy.pause(0.5, hard=True)
                ####ADD WALKING AWAY FOOTSTEP SOUND
                kris "（嗯...也許我要一些雞肉Tikka masala ??）"
                window hide
                show airport at bgslide
                $ renpy.pause(2, hard=True)
                window show
                mys "喲~~♪♪♪"
                kris "（????）"
                show smay0101
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                girl2 "嘿〜 ♪"
                kris "啊！"
                hide smay0101
                show smay0106
                girl2 "嘻嘻...你為什麼這麼驚訝...？"
                hide smay0106
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                show smay0107zoom
                $ renpy.transition(Dissolve(0.2))
                $ renpy.pause(0.3, hard=True)
                girl2 "你已經.....墜入愛河了嗎？"
                kris "（老兄...她聞起來很香...）"
                kris "（等等，為什麼我要表現老套？在KRISTIK，該死的上帝！我是乍得！如果我想要的話，我會得到所有的女孩！）"
                window hide
            menu:
                "斷言統治":
                    $ pointsGirl2 += 2
                    jump air1
                "尷尬":
                    $ pointsGirl2 += 1
                    jump air2
        label air1:
            window show
            kris "嘿。"
            kris "讓我觸摸你的胸部。"
            hide smay0107zoom
            show smay0117
            girl2 "嗯？？？"
            girl2 "嗯..."
            hide smay0117
            show smay0118
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "我們可能應該首先找到一個私人的地方..."
            hide smay0118
            show smay0213
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            kris "..."
            kris "（她想實際去做嗎？？？？）"
            kris "等一下 我只是在開玩笑...."
            girl2 "什麼樣的人這麼說然後說謊呢？ 白痴！"
            kris "（該死的傢伙，我有一些真正的傲嬌氛圍，而且真的很性感！）"
            hide smay0213
            show smay0108
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.3, hard=True)
            girl2 "哈哈哈！ 看你的臉！"
            girl2 "超級紅！"
            kris "（該死！我被騙了...）"
            girl2 "您實際上以為我會讓您對我這樣做？"
            hide smay0108
            show smay0101
            $ renpy.transition(Dissolve(0.2))
            girl2 "男孩是如此容易操縱。"
            kris "閉嘴！ 您不應該大聲說出來！"
            kris "（我的表現是如此陳詞濫調，令人毛骨悚然！）"
            kris "這就是傑森的女孩的樣子..."
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
            json "And Kristik youre also going to meet 2 new people when we get there."
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
            girl4 "Just for your information.... those 2 new people you're going to meet are girls..."
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
            girl4 "It's already getting competitive between us 4! Imagine having 2 NEW girls!"
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
            window hide
            scene white
            $ renpy.transition(Dissolve(2.4))  
            $ renpy.pause(3.2, hard=True) 
            scene house
            $ renpy.transition(Dissolve(2.4))  
            $ renpy.pause(2.4, hard=True) 
            $ _skipping = False 
            ####################################################################################################################################
            
            ##########################<<<<<<<<<<<<<<<<<END OF DEMO
          
            ####################################################################################################################################             
            
            ####################################################################################################################################
            
            $ _skipping = True ##########################<<<<<<<<<<<<<<<<<DELETE ON RELEASE
          
            ####################################################################################################################################  
           
            kris "And thats what happened."
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
            girl1 "Oh... hahaha..."
            girl1 "Who knew you'd be a murderer? Haha..."
            kris "Hey! Im not like that anymore!"
            girl2 "Makes me kinda worried that im going to be dating a yandere..."
            kris "Yandere??? Dating??? "
            girl4 "Hey wait a minute."
            hide smay0101
            hide ssuo0101
            hide srik0101
            hide syuz0101
            show syuz0113
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.3, hard=True) 
            girl4 "Who is this \"other\" person?"
            kris "Oh... uh.."
            girl4 "Dont tell me youre cheating on her with us!?!"
            kris "Wait wait wait!!! Its not like that!!"
            girl4 "Hm. Then who is she to you?"
            kris "Uh idk... i dont really know much about her."
            girl4 "Hmmm..."
            girl4 "If i ever find out that youre dating someone else i will ruin your life!"
            kris "(jesus!!! wtF??????????)"
            hide syuz0113
            show sner0204:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Cmon Hui Young, youre scaring him!"
            hide sich0101
            show sich0106:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            girl6 "Yeah, plus he looks like a dud so hes probably too scared to cheat anyways!"
            kris "(did i just get called a dud by some 19 year old?)"
            kris "(OOF)"
            kris "Hey i aint no dud! Im a chad! I could cheat if i really want to!"
            hide sich0106
            hide sner0204
            show syuz0113zoom
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl4 "Oh really? You would cheat?"
            kris "(shit!!! nvm!!! im such a pussy!!)"
            kris "Im sorry Im sorry!!! Im a dud i would never cheat!!!"
            hide syuz0113zoom
            show syuz0206
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl4 "Good boy."
            kris "(bruh i am a dud...)"
            hide syuz0206
            show sner0101:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kris "Hey by the way."
            kris "I dont really know you two."
            kris "They said that you were supposed to be Somalia. What are you doing here?"
            girl5 "Hey, willst du schon etwas über mich wissen?"
            kris "um...."
            kris "What?"
            girl5 "Du scheinst wirklich verwirrt zu sein!"
            girl6 "{=chinesetext} 你已經喜歡我們了嗎？ {/=chinesetext}"
            kris "(JUST HOW MANY LANGAUGES ARE GOING THROUGH THIS ROOM???)"
            kris "Ok first of all, nein nein nein hitler nein nein."
            kris "Second of all, ching chong bing bong guangzhou xue hua piao piao."
            girl5 "That wasn't very nice!"
            girl6 "Racist too!"
            kris "Well you guys are purposely speaking a language YOU KNOW i dont know."
            girl5 "Well, my name is Hannah Schröder and I am apart of the Navy. I'm usually the commander of USS Ticonderoga (CG-47). I am of German descent, if you couldn't tell."
            girl6 "I am Chiyoko Nakamur, and although i sound Japaense, I am half Chinese."
            kris "(you look more japanese than chinese imo...)"
            girl6 "I am a submarine technician. I can't say too much about what i do, since its classified."
            kris "Why does literally everybody here have a military related job?"
            kris "I was just a Walmart cashier until i joined this mess."
            girl5 "What a sad job..."
            kris "Hey! I made a killing amount of money!"
            girl5 "How much?"
            kris "Uhh.... like.... 9 rupees every month?"
            girl5 "hahaha! Poor ass boy."
            kris "Ay stfu! I aint no posh german girl who lives off of daddy's money."
            hide sner0101
            show sner0212:
                    linear 0.0 xalign 0.1
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Well say whatever you want..."
            kris "..."
            girl5 "Hm? Ran out of roasts already?"
            kris "grrr..."
            girl5 "XD"
            hide sner0212
            show sich0101
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
            girl3 "Hey. Whats the big idea? You dont act like that to us!"
            girl2 "Yeah yeah!"
            kris "What??? What are you talking about ??!"
            girl4 "Ughhh.... im really hungry..."
            kris "Oh yeah, we havent eaten in 2 days."
            girl2 "What?!??! Are you guys okay?!?"
            kris "lol we're fine"
            girl4 "Well im not! Ive gotta eat something!"
            hide smay0111
            hide ssuo0107
            hide srik0109
            hide syuz0117
            hide sich0101
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            show sner0101:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            girl5 "Do you guys want something? Unfortunately, I dont have any ingrediants so Ill have to go shopping right now."
            girl5 "Either that or we can just get takeout at some random place."
            girl5 "Which do you guys prefer?"
            hide sner0101
            show sich0101
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
            girl4 "Hmm... I think i want a homemade meal."
            girl2 "What??! No way! Take out! I want some pork katsu!"
            girl2 "Its really hard to get that stuff made at home and tasting as good as the resturaunts!"
            girl3 "Yeah! I think i want a take out."
            girl1 "I think i prefer something from home though...."
            girl1 "What about you krisitik?"
            kris "Uh...."
            kris "(maybe ill ask chiyoko...)"
            hide smay0111
            hide ssuo0107
            hide srik0109
            hide syuz0117
            hide sich0101
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            show sner0101:
                    linear 0.0 xalign 0.1
            show sich0101:
                    linear 0.0 xalign 0.8
            $ renpy.transition(Dissolve(0.4))  
            $ renpy.pause(0.2, hard=True) 
            kris "What about you Chiyoko? Do you want something in particular?"
            girl6 "I really dont care. I can eat anything right now."
            kris "(ughh... that didnt really help...)"
            girl5 "Well what about you?"
            kris "Um..."
            window hide
            menu:
                "Takeout":
                    $ pointsGirl2 += 1
                    $ pointsGirl4 += 1
                    jump takeout
                "Homemade":
                    $ pointsGirl1 += 1
                    $ pointsGirl3 += 1
                    $ pointsGirl5 += 1
                    jump homemade
                "I dont care":
                    jump dontcare
            
            
            
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
            label takeout:
                    kris "I think Ill go for some takeout. I kinda want some chicken tikka masala."
                    girl5 "Ok! Well what do you guys want?"
                    hide sner0101
                    show sich0101
                    show smay0111:
                        linear 0.0 xalign -0.1
                    show ssuo0107:
                        linear 0.0 xalign 0.3
                    show srik0109:
                        linear 0.0 xalign 0.7
                    show syuz0110:
                        linear 0.0 xalign 1.1
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(0.2, hard=True) 
                    girl1 "Idk maybe...."
                    girl1 "{=japantext}うどん？{/=japantext}"
                    girl1 "{=japantext}何を食べたい、みちこ？{/=japantext}"
                    girl2 "{=japantext}私は間違いなく豚カツを食べています！{/=japantext}"
                    kris "(there they go again speaking ching chong...)"
                    girl3 "Alright well me and Hui Young are gonna order some Yukgaejang. We'll bring some tangsuyuk and bulgogi kimbap on the way."
                    kris "(No idea what that is....)"
                    girl2 "Well then me and Asami are gonna order some Udon and pork katsu!"
                    girl1 "Yeah, and i guess we can bring some Tempura with miso..."
                    hide smay0111
                    hide ssuo0107
                    hide srik0109
                    hide syuz0110
                    show sner0101:
                            linear 0.0 xalign 0.1
                    show sich0101:
                            linear 0.0 xalign 0.8
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(0.2, hard=True) 
                    girl5 "Then ill go order some Sauerbraten for myself with some Käsespätzle."
                    girl6 "Yea! And ill get Sichuan pork with dim sum and Kung Pao chicken!"
                    kris "(jesus they eat so much!!)"
                    kris "Yeah ill grab something as well. Maybe a 7-eleven burrito or something."
                    girl6 "Whatt????!!? Thats what little duds eat! You need to eat more to grow those indian bones!"
                    kris "What are you talking about?! Im 23 im pretty much grown already."
                    girl6 "That doesnt mean you have to stop eating!"
                    kris "(Ugh...)"
                    girl5 "Alright well we decided what we're gonna eat! So we'll see you guys later~!"
                    kris "Are we eating it here or at the resturaunt?"
                    girl5 "Hmmm... If you want we can all bring our food here and eat together."
                    girl6 "That sounds cool!"
                    girl6 "Lets do that!!"
                    hide sner0101
                    show sich0101
                    show smay0111:
                        linear 0.0 xalign -0.1
                    show ssuo0107:
                        linear 0.0 xalign 0.3
                    show srik0109:
                        linear 0.0 xalign 0.7
                    show syuz0110:
                        linear 0.0 xalign 1.1
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(0.2, hard=True) 
                    girl2 "Yeah!!"
                    girl4 "Hmmm... that sounds interesting."
                    kris "Alright well do whatever you guys want. Im gonna get my food."
                    girl3 "Yeah same here."
                    window hide
                    scene bg black
                    with wipeleft
                    scene outside
                    with wipeleft
                    $ renpy.pause(1.0, hard=True) 
                    window show
                    ###<<< PLAY FOOTSTEP SOUNDS
                    kris "Hghhhhh......."
                    kris "(ugh im tired of this...)"
                    kris "(finally a time where i can have some peace... without being distracted by girls....)"
                    window hide
                    scene bg black
                    with wipeleft
                    scene 711
                    with wipeleft
                    $ renpy.pause(1.0, hard=True) 
                    window show
                    kris "(i wonder what i should get.... maybe some fiji water and a sandwich?)"
                    #######<<<<<<PLAY BEEP SOUND FOR ENTERING
                    window hide
                    scene 711interior
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(1.2, hard=True) 
                    window show
                    kris "(hmm....)"
                    kris "(Yeah... ill just get this burrito and a fiji water.)"
                    window hide
                    scene 711cashier
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(1.2, hard=True) 
                    window show
                    clerk1 "Hello."
                    kris "Hello."
                    window hide
                    $ renpy.pause(2.2, hard=True) 

                    #<<<< PLAY SCAN sounds
                    window show
                    clerk1 "That will be $7.19"
                    kris "Ok."
                    window hide
                    $ renpy.pause(2.2, hard=True) 

                    #<<<< PLAY card swipe sounds
                    window show                    
                    clerk1 "Would you like your reciept?"
                    kris "No thanks."
                    clerk1 "Ok. Have a good day."
                    window hide
                    scene 711
                    #######<<<<<<PLAY BEEP SOUND FOR ENTERING
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(1.2, hard=True) 
                    window show
                    kris "(He looked familiar.... Reminded me of a guy who had a last name Sidhu.... I cant remember his first name though...)"
                    kris "(whatever... doesnt really matter to me...)"
                    window hide
                    scene bg black
                    with wipeleft
                    scene outside
                    with wipeleft
                    $ renpy.pause(1.0, hard=True) 
                    window show
                    ###<<< PLAY FOOTSTEP SOUNDS
                    kris "(i shouldve gotten some chips actually...)"
                    girl5 "Heey!!!"
                    kris "(?)"
                    show sner0101:
                            linear 0.0 xalign 0.1
                    show sich0101:
                            linear 0.0 xalign 0.8
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(0.2, hard=True) 
                    kris "Oh its you guys."
                    girl5 "So what did you get?"
                    kris "7-eleven burrito and a fiji water."
                    girl6 "Huhh??! Didnt i just say to get more food??!!"
                    girl6 "A lame burrito isnt going to cut it!"
                    girl6 "Plus we mostly brought food from our own culture. A burrito isnt in Indian culture is it?"
                    kris "(i just wanted a burrito man...)"
                    girl5 "Yeah, but what should we do about it? Its not like we can return it."
                    kris "Just let me eat it!"
                    girl6 "Well we can let you eat it, but at least bring something more exciting!"
                    girl5 "Alright well we're both going. You better have something more than a burrito when you come back!"
                    kris "(why????? just let me eat a burrito!!!!!!!!!!)"
                    hide sich0101
                    hide sner0101
                    $ renpy.transition(Dissolve(0.4))  
                    $ renpy.pause(0.2, hard=True) 
                    kris "uhhghghghfgh.gh.gh.fgzh.fg.hs.e45.t.gsertnu4weru9345bn94tiefbgomuji9pof9wh8nfbunbn890342b9r38o4bt04n7n80w4etun0nw45v774wn qv2734h89tnqv43ntv7nq43ty803w4780nvtvmw4tuv5w4978m0ywmc7un8904uvynun4yw05n84y8uw485n8tbuw4u589vnttwmv..."
                    kris "(cooooome oooonnnnn!!!!!!!!! really?????!!?!??!?!?!)"
                    kris "fuck dude..."
                    $ foodtype = 0
                    window hide
                    menu:
                        "Buy something else":
                            jump morefood
                        "Go straight home":
                            jump straighthome
                    label morefood:
                        window show
                        kris "Fuuuuuuuck... i guess ill do it."
                        kris "(but what kind of food??)"
                        window hide
                        menu:
                            "American":
                                $ foodtype = 1
                                jump americanfood
                            "Mexican":
                                $ foodtype = 2
                                jump mexicanfood
                            "Chinese":
                                $ foodtype = 3
                                jump chinesefood
                            "Korean":
                                $ foodtype = 4
                                jump koreanfood
                            "Vietnamese":
                                $ foodtype = 5
                                jump vietnamesefood
                        label americanfood:
                            window show
                            kris "I guess i could get some good ol American food eeeyeyyyyyeye"
                            window hide
                            scene bg black
                            with wipeleft
                            scene mcde
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show
                            kris "This is pretty American."
                            scene mcdi
                            $ renpy.transition(Dissolve(0.4))  
                            $ renpy.pause(0.2, hard=True) 
                            worker1 "Helloooo.... and welcome to the Donalds of Mc. Hoooooow can i help you todaaaaay?"
                            kris "(pretty depressing ngl XD)"
                            kris "Can i get a number 1 medium?"
                            worker1 "Ok."
                            worker1 "That'll be $2.12"
                            kris "(hella cheap!)"
                            kris "Ok."
                            window hide 
                            $ renpy.pause(1.2, hard=True) 
                            ###play card swipe sound
                            window show
                            worker1 "Your order number is 69."
                            kris "ok."
                            window hide
                            scene bg black
                            with wipeleft
                            scene mcdi
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show                           
                            worker1 "Order number 69!"
                            kris "Yup."
                            worker1 "Would you like any ketchup"
                            kris "No."
                            worker1 "O K."
                            window hide
                            scene bg black
                            with wipeleft
                            scene mcde
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show
                            kris "Well its better than nothing."
                            window hide
                            jump homefastfoodcometogether
                        label mexicanfood:
                            window show
                            kris "I guess i could get some mexican food pito de queso"
                            window hide
                            scene bg black
                            with wipeleft
                            scene tacobell
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "This is close enough."
                            window hide
                            scene bg black
                            with wipeleft
                            scene tacobelli
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            worker1 "Hello."
                            kris "????"
                            worker1 "Oh lo siento, ¿hablas español solamente?"
                            kris "?????????????????"
                            kris "(i learned spanish in high school, let me try and decode this....)"
                            kris "(lets see.... Oh lo siento means sorry, hablas español means do you speak spanish... what is solamente???)"
                            worker1 "¿Vas a pararte allí para siempre?"
                            kris "(shit!!!! this is too advanced!!!)"
                            kris "U-uhh... me no hablar espanol!! mi gusta pito de queso burrito!!!"
                            kris "(im pretty sure i said i want a burrito!)"
                            worker1 "??!?!?"
                            worker1 "You said you LIKE dick cheese??!"
                            kris "Uhh... what??"
                            worker1 "Nevermind. Hurry up and order."
                            kris "I want 20 pack of tacos."
                            worker1 "$20.59"
                            kris "ok."
                            window hide
                            scene bg black
                            with wipeleft
                            scene tacobell
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "Never coming back here again!"
                            kris "He just asked me do i like dick cheese what a fucking weirdo"
                            window hide
                            jump homefastfoodcometogether
                        label chinesefood:
                            kris "Maybe some ching chong chinese food will be good."
                            window hide
                            scene bg black
                            with wipeleft
                            scene chineserest
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show         
                            kris "Not really feeling for Panda express so i guess ill go here."
                            kris " \"Hung's Chinese restaurant\"? "
                            kris "Hmmm... reminds me of a kid named Hung."
                            window hide
                            scene bg black
                            with wipeleft
                            scene chineseresti
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "Holy shit this place is fucking insane!!!"
                            worker1 "Hello sir! Do you have a reservation?"
                            kris "No, im just looking for takeout."
                            worker1 "No worries sir, its down the hall to the left."
                            kris "Thanks."
                            window hide
                            $ renpy.pause(1.0, hard=True) 
                            window show
                            show hungnorm
                            $ renpy.transition(Dissolve(0.4))  
                            $ renpy.pause(0.2, hard=True) 
                            hung "Hello, what would you like to order for takeout?"
                            kris "...."
                            kris "HUNG?!?!?!?"
                            hung "Yes im hung."
                            kris "WHAT ARE YOU DOING HERE??!?!"
                            hung "What? Do you not like my job?!"
                            kris "I mean its fine, but since when do you own this place??"
                            hung "Huh? Ive had this business for a while. About 5 years now."
                            kris "WTF?!?!!?"
                            hung "Anyways what do you want??"
                            kris "uhh... oh yeah... uhhhh..."
                            kris "Ill take some chow mein and orange chicken i guess..."
                            hung "Foreigner scum... always orders the same things..."
                            kris "What was that?"
                            hung "nothing. Your food will come."
                            kris "Ok..."
                            window hide
                            scene bg black
                            with wipeleft
                            hide hungnorm
                            scene chineseresti
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            show hungnorm
                            $ renpy.transition(Dissolve(0.4))  
                            $ renpy.pause(0.2, hard=True) 
                            hung "here."
                            kris "Thanks. How much will it be?"
                            hung "Free. I know you have alot of kids to feed so i will give you an exception for today."
                            kris "KIDS?!?!?!?!"
                            kris "Hold on i dont have any kids. Who told you i had kids?"
                            hung "Aaron told me."
                            kris "WOT???"
                            kris "How is he still in contact with you!!?!?!?"
                            hung "huh? What do you mean? I can call bill too."
                            kris "WOT?!?!?!?!"
                            kris "Hung you NEED to tell me where they are! Me and the rest of the gang are trying to capture them!!"
                            hung "I dont think they're gay kristik."
                            kris "Not in that way! Just give me his number!"
                            hung "Ok."
                            hide hungnorm
                            $ renpy.transition(Dissolve(0.4))  
                            $ renpy.pause(2.2, hard=True) 
                            #add  phone dial beeping 
                            show hungnorm
                            $ renpy.transition(Dissolve(0.4))  
                            $ renpy.pause(0.2, hard=True) 
                            hung "Here."
                            kris "Thanks."
                            window hide
                            scene bg black
                            with wipeleft
                            hide hungnorm
                            scene chineserest
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "Im gonna try calling them...."
                            window hide 
                            $ renpy.pause(2.2, hard=True) 
                            ##play brrr sound
                            window show
                            aar "Hello?"
                            kris "Uhh... who is this?"
                            aar "I can ask the same question to you. Who are you?"
                            kris "Its me kristik!"
                            aar "What do you want?"
                            kris "Uhh....."
                            kris "(shit now that i think about it... what was i gonna ask him?)"
                            kris "So uh hows it been?"
                            aar "I dont know who you are so I wont be answering personal questions. Anything else?"
                            kris "Dude its me ! Krib, crab on a stick! etc. "
                            aar "I dont know what youre talking about. If youre going to solicit me ill call Merrywether to beat your ass."
                            kris "Uh....."
                            window hide 
                            $ renpy.pause(2.2, hard=True) 
                            ##play hangup sound
                            window show
                            kris "Shit that didnt go well...."
                            kris "Whatever ill let the bois know about this later. "
                            window hide 
                            jump homefastfoodcometogether
                        label koreanfood:
                            kris "im have the weird urge to try korean food again for some reason..."
                            window hide
                            scene bg black
                            with wipeleft
                            scene koreanstr
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show         
                            kris "Hm... Now which one of these signs say restaurant?"
                            window hide
                            scene bg black
                            with wipeleft
                            scene koreanstri
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "Bruh.... "
                            kris "Why does it look so good in here??"
                            worker1 "{=koreatext}어서 오십시오. 예약 하셨나요?{/=koreatext}"
                            kris "uhh....."
                            kris "No???"
                            worker1 "Are you here for takeout?"
                            kris "Yes!!"
                            worker1 "Takeout table is over there to the left."
                            kris "Thanks."
                            window hide
                            scene bg black
                            with wipeleft
                            scene koreanstr
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "Well, i ordered some weird stuff. I have no idea what this is."
                            kris "Im just gonna hope this is something i can eat."
                            window hide 
                            jump homefastfoodcometogether
                        label vietnamesefood:
                            window show
                            kris "Now that I think about it, I havent tried any sort of Vietnamese food."
                            kris "Maybe this is my chance?"
                            window hide
                            scene bg black
                            with wipeleft
                            scene pho
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "I think vietnamese people eat pho right?"
                            window hide
                            scene bg black
                            with wipeleft
                            scene phoi
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "Hmm..."
                            worker1 "chào mừng"
                            worker1 "đụ má mày"
                            kris "Uhh...."
                            kris "ill get some Phở with Cao lầu and a side of Gỏi cuốn."
                            worker1 "Ok người da đen"
                            kris "(No idea what that means...)"
                            window hide
                            scene bg black
                            with wipeleft
                            scene pho
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show  
                            kris "Well i got some random shit off of the menu..."
                            kris "I probably didnt speak vietnamese properly..."
                            jump homefastfoodcometogether
                    label straighthome:
                            window show
                            kris "Nahh... whatever... im just gonna eat my burrito."
                            window hide 
                            jump homefastfoodcometogether
                    label homefastfoodcometogether:
                        window hide
                        scene bg black
                        with wipeleft
                        scene house
                        with wipeleft
                        $ renpy.pause(1.0, hard=True) 
                        window show          
                        show smay0101:
                            linear 0.0 xalign -0.2
                        show ssuo0101:
                            linear 0.0 xalign 0.4
                        show srik0101:
                            linear 0.0 xalign 0.9
                        show syuz0101:
                            linear 0.0 xalign 1.2
                        show sner0101:
                                linear 0.0 xalign 0.1
                        show sich0101:
                                linear 0.0 xalign 0.7
                        $ renpy.transition(Dissolve(0.4))  
                        $ renpy.pause(0.2, hard=True)    
                        girl4 "So what did you guys get?"
                        girl2 "I got Pork Cutlet and Udon with Miso soup!"
                        girl5 "I got some German hot dogs and smoked steak."
                        girl4 "What about you kristik?"
                        if foodtype == 0:
                            $ pointsGirl6 -= 1
                            $ pointsGirl5 -= 1
                            kris "I just got a burrito. Nothing else."
                            girl6 "What???!?!?"
                            girl6 "We told you to get something more! You dud!"
                            kris "This isnt some 5th grade potluck!"
                            kris "Im just tryna eat my burrito bro!"
                            window hide
                            scene bg black
                            with wipeleft
                            scene house
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show   
                            kris "「該死的，那很好。」"
                            show smay0113
                            $ renpy.transition(Dissolve(0.4))  
                            $ renpy.pause(0.2, hard=True)    
                            girl2 "「你只吃了一件事！」"
                            kris "「我的意思是那是一個很好的墨西哥捲餅。」"
                            hide smay0113
                            show smay0111
                            girl2 "「像您這樣的男孩就是這樣得到小陰莖！」"
                            krismind "?!?!?!?"
                            hide smay0111
                            show smay0115
                            girl2 "「嗯...」"
                            hide smay0115
                            show smay0213
                            $ renpy.transition(Dissolve(0.4))  
                            $ renpy.pause(0.2, hard=True)    
                            girl2 "「忘了我說什麼....」"
                            krismind "她剛剛說了什麼？"
                            hide smay0213
                            show sner0207:
                                    linear 0.0 xalign 0.1
                            show sich0103:
                                    linear 0.0 xalign 0.8
                            $ renpy.transition(Dissolve(0.4))
                            $ renpy.pause(0.2, hard=True) 
                            girl5 "「克里斯蒂克...是真的嗎？ 她在說什麼...」"
                            girl6 "「哇...不管他要和誰交往，這都很爛。」"
                            kris "「我怎麼會知道？？？？！！！ 而且我不會交配！」"
                            girl5 "「嗯...」"
                            girl6 "「我為要與他發生性關係的人感到難過。」"
                            kris "「你為什麼...沒關係！ 夠了！」"
                            jump notfoodanymore

                        if else foodtype == 1:
                            kris "「我剛去麥當勞，並得到了巨無霸。 我也有7-11的墨西哥捲餅，但是那兩個告訴我再吃點東西。」"
                            hide smay0101
                            hide ssuo0101
                            hide srik0101
                            hide syuz0101
                            hide sner0101
                            hide sich0101
                            show syuz0101:
                                linear 0.0 xalign 0.8
                            $ renpy.transition(Dissolve(0.6))
                            show srik0104:
                                linear 0.0 xalign 0.1
                            $ renpy.transition(Dissolve(0.6))  
                            $ renpy.pause(3, hard=True) 
                            girl4 "Now that I think about it I dont think ive tried American fast food."
                            kris "Really???"
                            kris "You wanna try it?"
                            girl4 "Hmmm... maybe ill try it after you take a bite"
                            kris "Uhhh....."
                            kris "(isnt that....)"
                            hide srik0104
                            show srik0109:
                                linear 0.0 xalign 0.1
                            $ renpy.transition(Dissolve(0.6))  
                            $ renpy.pause(3, hard=True) 
                            girl3 "Hey! I know what youre trying to do Hui Young!"
                            girl4 "Teehee~~ What do you mean? I just want to try an American burger"
                            girl3 "What are you taking about!?!? i saw you eat 2 whoppers at burger king!"
                            hide syuz0101
                            show syuz0117:
                                linear 0.0 xalign 0.8
                            $ renpy.transition(Dissolve(0.6))
                            girl4 "!!"
                            girl4 "Dont say that shit out loud!!"
                            hide srik0109
                            show srik0205:
                                linear 0.0 xalign 0.1
                            $ renpy.transition(Dissolve(0.6))  
                            $ renpy.pause(3, hard=True) 
                            girl3 "Oh..?"
                            girl3 "Youre Embarrassed cause of that?"
                            girl3 "Hey kristik did you know that she masturbates to-"
                            girl4 "HEY!! WHY ARE YOU TELLING HIM THAT??!!!!"
                            kris "(bruh i didnt need to know that.... but now im sorta interested)"
                            girl4 "That shit isnt funny!"
                            window hide
                            scene bg black
                            with wipeleft
                            scene house
                            with wipeleft
                            $ renpy.pause(1.0, hard=True) 
                            window show   
                            kris "So what did you get?"
                            girl1 "Well essentially, we all got food thats froum our own culture."
                            girl2 "Yeah! Like me and Asami both got Japanese food, those two got Korean, Hannah got German food, and Chiyoko got chinese food."
                            kris "Hmmm..."
                            kris "(I wanna try their food, but whos?)"


                        if else foodtype == 2:
                            kris "I got some \"Mexican\" food. But im pretty sure real Mexicans dont eat taco bell or at least they dont consider it real Mexican food."
                            girl3 "Oh. Mexican? I thought you wouldve gotten something more indian."
                            kris "Ive eaten Indian food for like my whole life."
                            kris "I wanted to try something different..."
                            girl4 "And \"Mexican\" fast food was your choice?"
                            kris "Alright you dont need to roast me!"
                            girl4 "Huh? That wasnt a roast! I was just wondering the logic behind that..."
                            kris "Ugh..."
                        if else foodtype == 3:
                            kris "I got some Chinese food, and I met a friend I haven't seen a really long time over there. I also got Aaron's phone number..."
                            girl2 "Whos Aaron?"
                            kris "A person."
                            girl3 "No shit, we mean who is this person?"
                            kris "A person that Jason apparently has beef on."

                        if else foodtype == 4:
                            kris "I went to some random street in Koreatown and read whatever was off of the menu. No idea what some of this shit is."
                        else:
                            kris "I went to some Vietnamese restuarant. But i dont think the guy could speak English. He was sorta weird."

            label homemade:
                    kris "Im kinda feeling for something made from home."
                    girl5 "Okay! Well Ill be going to the grocery store. Do you want to come with me?"
                    kris "Hm..."
                    menu:
                        "Go with her":
                            $ pointsGirl5 += 1
                            jump store       
                        "Stay home":
                            jump stayhome
                    label store:
                    
                    label stayhome:

            label notfoodanymore:
                play backgroundSFX "audio/ringtone.mp3"
                $ renpy.pause(2, hard=True)
                kris "「有人在打電話給我...」"
                hide sner0207
                hide sich0103
                $ renpy.transition(Dissolve(0.4))
                $ renpy.pause(0.2, hard=True) 
                stop backgroundSFX
                kris "「您好」"
                json "「克里斯蒂克，這是一個嚴重的問題。 我們已經從索馬里的2名間諜那裡獲得了情報，看來衛斯理已經準備好了一顆正在工作的核彈，準備發射並轟炸惡魔領域！」"
                kris "「什麼？？？！ 有沒有搞錯？！ 他們打算炸毀我們嗎？」"
                show smay0111:
                    linear 0.0 xalign -0.2
                show ssuo0107:
                    linear 0.0 xalign 0.4
                show srik0214:
                    linear 0.0 xalign 0.9
                show syuz0113:
                    linear 0.0 xalign 1.2
                show sner0207:
                        linear 0.0 xalign 0.1
                show sich0109:
                        linear 0.0 xalign 0.7
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)    
                allofthem "{size=+12}「什麼？？？？！」{/size}"
                kris "「等一下，等等，發生了什麼事？」"
                json "「我們沒有很多時間！ 告訴其他女孩這是“ PLAN＃23”」"
                kris "「傑森說這是“Plan 23”」"
                json "「並告訴他們快點去宮殿！」"
                kris "「我們必須去宮殿！」"
                girl5 "「“Plan 23” ...這是最壞的情況。」"
                girl5 "「在這種情況下，我們沒有太多的培訓。」"
                krismind "「現在，我擔心這個計劃實際上是什麼！」"
                girl2 "「好吧，我們趕快去宮殿！」"
                hide smay0111
                hide ssuo0107
                hide srik0214
                hide syuz0113
                hide sner0207
                hide sich0109      
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)   
                window hide
                scene bg black
                with wipeleft
                scene castle2
                with wipeleft
                $ renpy.pause(1.0, hard=True)   
                window show
                show smay0111:
                    linear 0.0 xalign -0.2
                show ssuo0107:
                    linear 0.0 xalign 0.4
                show srik0214:
                    linear 0.0 xalign 0.9
                show syuz0113:
                    linear 0.0 xalign 1.2
                show sner0207:
                        linear 0.0 xalign 0.1
                show sich0109:
                        linear 0.0 xalign 0.7
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)  
                allofthem "{size=+22}「情況如何？！」{/size}"
                hide smay0111
                hide ssuo0107
                hide srik0214
                hide syuz0113
                hide sner0207
                hide sich0109      
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)   
                show jasonnorm
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)   
                json "「好吧，我給你做個簡介。 和胖男孩，你最好注意！」"
                kris "「是的，只要快點...」"
                json "「好了，這是計劃...」"
                window hide
                hide json
                scene plan1
                with fade
                $ renpy.pause(1.0, hard=True)
                json "「我們將在附近的機場起飛，由於地對空導彈，我們將在山上飛行。」"
                scene plan2
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)   
                json "「基地位於DR25區，我們將需要Kristik，Kyle，Cade和Kevin作為空對地戰鬥機。」"
                json "「任務控制將由千代子和漢娜進行，因此他們將留在後面。」"
                json "「麻美和美智子將成為您的航班負責人，他們將進入中隊，並摧毀所有進來的飛機。」"
                json "「鐘茶和惠英將與另外兩名女孩進行地面攻擊。」"
                scene plan3
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)   
                json "「您有4個男孩將加入F-16戰鬥機作為A-10疣豬中隊。 凱文和凱德將使用他們選擇的任何武器駕駛A-10並攻擊基地。 如果情況惡化，克里斯蒂克（Kristik）和凱爾（Kyle）將飛過頭頂，幫助女孩空空進行格鬥。」"
                json "「我們將在3小時內開始我們的任務。」"
                scene castle2
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)   
                show jasonnorm
                kris "「什麼？？？ 3小時？？！ 我不知道F-16會熱飛！」"
                json "「不用擔心，我們會為您提供幫助。 但是，駕駛飛機是您必須要適應的事情。」"
                json "「好吧，放手！」"
                hide jasonnorm
                show smay0111:
                    linear 0.0 xalign -0.2
                show ssuo0107:
                    linear 0.0 xalign 0.4
                show srik0214:
                    linear 0.0 xalign 0.9
                show syuz0113:
                    linear 0.0 xalign 1.2
                show sner0207:
                        linear 0.0 xalign 0.1
                show sich0109:
                        linear 0.0 xalign 0.7
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)  
                allofthem "{size=+22}「是的！」{/size}"
                krismind "他們怎麼不害怕？！？！？"
                window hide
                hide smay0111
                hide ssuo0107
                hide srik0214
                hide syuz0113
                hide sner0207
                hide sich0109      
                $ renpy.transition(Dissolve(0.4))  
                $ renpy.pause(0.2, hard=True)   
                show somaliaArcintro
                $ renpy.pause(27, hard=True)   
                e "yes"
            e "Test portion after demo end memory addr 0x0e340"
            label undertale:
                window hide
                show under1
                $ attacktimes = 0
                $ usedpages = 0
                $ quick_menu = False
                $ renpy.pause(25, hard=True) 
                show underidle
                $ renpy.pause(0.1, hard=True)     
                hide under1               
                play backgroundmusic "audio/yes.ogg"
                hide under1
                $ renpy.pause(3, hard=True) 
                $ under_tale = True
                show undertaleidle
                hide underidle
                $ renpy.pause(1000000000000000000, hard=True) 
            label attack:
                $usedpages += 1
                $attacktimes += 1
                if attacktimes > 1:
                    $ under_tale = False
                    show underattack2
                    $ renpy.pause(7, hard=True) 
                    hide underidleimage
                    hide underattack2
                else:
                    show underattack1
                    $ under_tale = False
                    $ renpy.pause(7, hard=True) 
                    hide underidleimage
                    hide underattack1

                jump idle
            label act:
                $usedpages += 1
                show actpage1
                $ under_tale = False
                $ renpy.pause(5, hard=True) 
                hide actpage1
                jump idle2
            label item:
                show itempage
                $ under_tale = False
                $ renpy.pause(6.5, hard=True) 
                hide itempage
                $usedpages += 1
                jump idle
            label mercy:
                show sparepage
                $ under_tale = False
                $ renpy.pause(3, hard=True) 
                hide sparepage
                $usedpages += 1
                show blueheart
                $ renpy.pause(8, hard=True) 
                hide blueheart
                jump idle         
            label idle:
                $ under_tale = True
                show idle1pic
                if usedpages == 3:
                    jump end
                $ renpy.pause(1000000000000000000, hard=True) 
            label idle2:
                $ under_tale = True
                show idle2
                if usedpages == 3:
                    jump end
                $ renpy.pause(1000000000000000000, hard=True)              
            label end:
                $ under_tale = False
                stop backgroundmusic
                show underend1
                $ renpy.pause(6.2, hard=True)       
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
