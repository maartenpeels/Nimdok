# -*- coding: utf-8 -*-
#!/usr/bin/python
from BotKit import handles
from random import choice

smileys = [
    u"""¢‿¢""" ,u"""©¿© o""" ,u"""ª{•̃̾_•̃̾}ª""" ,u"""¬_¬"""
    ,u"""¯＼(º_o)/¯""" ,u"""¯\(º o)/¯""" ,u"""¯\_(⊙︿⊙)_/¯""" ,u"""¯\_(ツ)_/¯"""
    ,u"""°ω°""" ,u"""°Д°""" ,u"""°‿‿°""" ,u"""¿ⓧ_ⓧﮌ"""
    ,u"""Ò,ó""" ,u"""ó‿ó""" ,u"""ô⌐ô""" ,u"""ôヮô"""
    ,u"""ŎםŎ""" ,u"""ŏﺡó""" ,u"""ʕ•̫͡•ʔ""" ,u"""ʕ•ᴥ•ʔ"""
    ,u"""ʘ‿ʘ""" ,u"""˚•_•˚""" ,u"""˚⌇˚""" ,u"""˚▱˚"""
    ,u"""̿ ̿̿'̿'\̵͇̿̿\=(•̪●)=/̵͇̿̿/'̿̿ ̿ ̿ ̿""" ,u"""Σ ◕ ◡ ◕""" ,u"""Σ(ﾟДﾟ )""" ,u"""Φ,Φ"""
    ,u"""δﺡό""" ,u"""σ_σ""" ,u"""д_д""" ,u"""ф_ф"""
    ,u"""щ（ﾟДﾟщ)""" ,u"""Ծ_Ծ""" ,u"""٩๏̯͡๏۶""" ,u"""٩๏̯͡๏)۶"""
    ,u"""٩◔̯◔۶""" ,u"""٩(͡๏̯͡๏)۶""" ,u"""٩(͡๏̯ ͡๏)۶""" ,u"""٩(ಥ_ಥ)۶"""
    ,u"""٩(•̮̮̃•̃)۶""" ,u"""٩(●̮̮̃•̃)۶""" ,u"""٩(●̮̮̃●̃)۶""" ,u"""٩(｡͡•‿•｡)۶"""
    ,u"""٩(-̮̮̃•̃)۶""" ,u"""٩(-̮̮̃-̃)۶""" ,u"""۞_۞""" ,u"""۞_۟۞"""
    ,u"""۹ↁﮌↁ""" ,u"""۹⌤_⌤۹""" ,u"""॓_॔""" ,u"""१✌◡✌५"""
    ,u"""१|˚–˚|५""" ,u"""ਉ_ਉ""" ,u"""ଘ_ଘ""" ,u"""இ_இ"""
    ,u"""ఠ_ఠ""" ,u"""రృర""" ,u"""ಠ¿ಠi""" ,u"""ಠ‿ಠ"""
    ,u"""ಠ⌣ಠ""" ,u"""ಠ╭╮ಠ""" ,u"""ಠ▃ಠ""" ,u"""ಠ◡ಠ"""
    ,u"""ಠ益ಠ""" ,u"""ಠ益ಠ""" ,u"""ಠ︵ಠ凸""" ,u"""ಠ , ಥ"""
    ,u"""ಠ.ಠ""" ,u"""ಠoಠ""" ,u"""ಠ_ృ""" ,u"""ಠ_ಠ"""
    ,u"""ಠ_๏""" ,u"""ಠ~ಠ""" ,u"""ಡ_ಡ""" ,u"""ತಎತ"""
    ,u"""ತ_ತ""" ,u"""ಥдಥ""" ,u"""ಥ‿ಥ""" ,u"""ಥ◡ಥ"""
    ,u"""ಥ﹏ಥ""" ,u"""ಥ_ಥ""" ,u"""ಭ_ಭ""" ,u"""ರ_ರ"""
    ,u"""ಸ , ໖""" ,u"""ಸ_ಸ""" ,u"""ക_ക""" ,u"""อ้_อ้"""
    ,u"""อ_อ""" ,u"""โ๏௰๏ใ ื""" ,u"""๏̯͡๏﴿""" ,u"""๏̯͡๏"""
    ,u"""๏̯͡๏﴿""" ,u"""๏[-ิิ_•ิ]๏""" ,u"""๏_๏""" ,u"""໖_໖"""
    ,u"""༺‿༻""" ,u"""ლ(´ڡ`ლ)""" ,u"""ლ(◉◞౪◟◉‵ლ)""" ,u"""ლ,ᔑ•ﺪ͟͠•ᔐ.ლ"""
    ,u"""ᄽὁȍ ̪ őὀᄿ""" ,u"""ᕙ(⇀‸↼‶)ᕗ""" ,u"""•▱•""" ,u"""•✞_✞•"""
    ,u"""‷̗ↂ凸ↂ‴̖""" ,u"""‹•.•›""" ,u"""‹› ‹(•¿•)› ‹›""" ,u"""‹(ᵒᴥᵒ­­­­­)›﻿"""
    ,u"""ↁ_ↁ""" ,u"""⇎_⇎""" ,u"""≧ヮ≦""" ,u"""⊂•⊃_⊂•⊃"""
    ,u"""⊂(◉‿◉)つ""" ,u"""⊙ω⊙""" ,u"""⊙▂⊙""" ,u"""⊙▃⊙"""
    ,u"""⊙△⊙""" ,u"""⊙︿⊙""" ,u"""⊙﹏⊙""" ,u"""⊙０⊙"""
    ,u"""⊛ठ̯⊛""" ,u"""⋋ō_ō`""" ,u"""━━━ヽ(ヽ(ﾟヽ(ﾟ∀ヽ(ﾟ∀ﾟヽ(ﾟ∀ﾟ)ﾉﾟ∀ﾟ)ﾉ∀ﾟ)ﾉﾟ)ﾉ)ﾉ━━━""" ,u"""┌∩┐(◕_◕)┌∩┐"""
    ,u"""┌( ಠ_ಠ)┘""" ,u"""┌( ಥ_ಥ)┘""" ,u"""╚(•⌂•)╝""" ,u"""╭╮╭╮☜{•̃̾_•̃̾}☞╭╮╭╮"""
    ,u"""╭✬⌢✬╮""" ,u"""╯‵Д′)╯彡┻━┻""" ,u"""╰☆╮""" ,u"""□_□"""
    ,u"""►_◄""" ,u"""◃┆◉◡◉┆▷""" ,u"""◉△◉""" ,u"""◉︵◉"""
    ,u"""◉_◉""" ,u"""○_○""" ,u"""●¿●\ ~""" ,u"""●_●"""
    ,u"""◔̯◔""" ,u"""◔ᴗ◔""" ,u"""◔ ⌣ ◔""" ,u"""◔_◔"""
    ,u"""◕ω◕""" ,u"""◕‿◕""" ,u"""◕◡◕""" ,u"""◕ ◡ ◕"""
    ,u"""◖♪_♪|◗""" ,u"""◖|◔◡◉|◗""" ,u"""◘_◘""" ,u"""◙‿◙"""
    ,u"""◜㍕◝""" ,u"""◪_◪""" ,u"""◮_◮""" ,u"""☁ ☝ˆ~ˆ☂"""
    ,u"""☆¸☆""" ,u"""☉‿⊙""" ,u"""☉_☉""" ,u"""☐_☐"""
    ,u"""☜(ﾟヮﾟ☜)""" ,u"""☜-(ΘLΘ)-☞""" ,u"""☝☞✌""" ,u"""☮▁▂▃▄☾ ♛ ◡ ♛ ☽▄▃▂▁☮"""
    ,u"""☹_☹""" ,u"""☻_☻""" ,u"""☼.☼""" ,u"""☾˙❀‿❀˙☽"""
    ,u"""✌.ʕʘ‿ʘʔ.✌""" ,u"""✌.|•͡˘‿•͡˘|.✌""" ,u"""✖_✖""" ,u"""❐‿❑"""
    ,u"""⨀_⨀""" ,u"""⨀_Ꙩ""" ,u"""⨂_⨂""" ,u"""〆(・∀・＠)"""
    ,u"""《〠_〠》""" ,u"""【•】_【•】""" ,u"""〠_〠""" ,u"""〴⋋_⋌〵"""
    ,u"""のヮの""" ,u"""ニガー? ━━━━━━(ﾟ∀ﾟ)━━━━━━ ニガー?""" ,u"""ペ㍕˚\\""" ,u"""ヽ(´ｰ｀ )ﾉ"""
    ,u"""ヽ(｀Д´)ﾉ""" ,u"""ヽ(ｏ`皿′ｏ)ﾉ""" ,u"""ㅎ_ㅎ""" ,u"""乂◜◬◝乂"""
    ,u"""凸ಠ益ಠ)凸""" ,u"""句_句""" ,u"""Ꙩ⌵Ꙩ""" ,u"""Ꙩ_Ꙩ"""
    ,u"""ꙩ_ꙩ""" ,u"""Ꙫ_Ꙫ""" ,u"""ꙫ_ꙫ""" ,u"""ꙮ_ꙮ"""
    ,u"""흫_흫""" ,u"""句_句""" ,u"""﴾͡๏̯͡๏﴿ O'RLY?""" ,u"""﻿¯\(ºдಠ)/¯"""
    ,u"""（·×·）""" ,u"""（⌒Д⌒）""" ,u"""（♯・∀・）⊃""" ,u"""（゜Д゜）"""
    ,u"""（ﾟ∀ﾟ）""" ,u"""（ ´☣///_ゝ///☣｀）""" ,u"""（ つ Д ｀）""" ,u"""＿☆（ ´_⊃｀）☆＿"""
    ,u"""｡◕‿‿◕｡""" ,u"""｡◕ ‿ ◕｡""" ,u"""!⑈ˆ~ˆ!⑈""" ,u"""!(｀･ω･｡)"""
    ,u"""(¬_¬)""" ,u"""(°ℇ °)""" ,u"""(°∀°)""" ,u"""(´◉◞౪◟◉)"""
    ,u"""(´・ω・｀)""" ,u"""(ʘ‿ʘ)""" ,u"""(ʘ_ʘ)""" ,u"""(˚இ˚)"""
    ,u"""(͡๏̯͡๏)""" ,u"""(ΘεΘ;)""" ,u"""(Ծ‸ Ծ)""" ,u"""(० ्०)"""
    ,u"""(ு८ு_ .:)""" ,u"""(ಠ‾ಠ﻿)""" ,u"""(ಠ‿ʘ)""" ,u"""(ಠ‿ಠ)"""
    ,u"""(ಠ⌣ಠ)""" ,u"""(ಠ益ಠ ╬)""" ,u"""(ಠ益ಠ)""" ,u"""(ಠ_ృ)"""
    ,u"""(ಠ_ಠ)""" ,u"""(ಥ﹏ಥ)""" ,u"""(ಥ_ಥ)""" ,u"""(๏̯͡๏ )"""
    ,u"""(ᵔᴥᵔ)""" ,u"""(•ω•)""" ,u"""(•‿•)""" ,u"""(• ε •)"""
    ,u"""(≧ロ≦)""" ,u"""(⌐■_■)""" ,u"""(┛◉Д◉)┛┻━┻""" ,u"""(╬ಠ益ಠ)"""
    ,u"""(╬◣д◢)""" ,u"""(╬ ಠ益ಠ)""" ,u"""(╯°□°）╯︵ ┻━┻""" ,u"""(▰˘◡˘▰)"""
    ,u"""(●´ω｀●)""" ,u"""(◑◡◑)""" ,u"""(◕‿◕)""" ,u"""(◕︵◕)"""
    ,u"""(◕ ^ ◕)""" ,u"""(◕_◕)""" ,u"""(◜௰◝)""" ,u"""(◣_◢)"""
    ,u"""(☞ﾟ∀ﾟ)☞""" ,u"""(☞ﾟヮﾟ)☞""" ,u"""(☞ﾟ ∀ﾟ )☞""" ,u"""(☼◡☼)"""
    ,u"""(☼_☼)""" ,u"""(✌ﾟ∀ﾟ)☞""" ,u"""(　・∀・)""" ,u"""(　･ัω･ั)？"""
    ,u"""(　ﾟ∀ﾟ)o彡゜えーりんえーりん!!""" ,u"""(づ｡◕‿‿◕｡)づ""" ,u"""(ノಠ益ಠ)ノ彡┻━┻""" ,u"""(ノ ◑‿◑)ノ"""
    ,u"""(；一_一)""" ,u"""(｡◕‿‿◕｡)""" ,u"""(｡◕‿◕｡)""" ,u"""(｡◕ ‿ ◕｡)"""
    ,u"""(｡･ω..･)っ""" ,u"""(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧""" ,u"""(ﾟ∀ﾟ)""" ,u"""(ﾟヮﾟ)"""
    ,u"""(￣ー￣)""" ,u"""( °٢° )""" ,u"""( •_•)>⌐■-■""" ,u"""( ･ิз･ิ)"""
    ,u"""(*..Д｀)""" ,u"""(*..д｀*)""" ,u"""(-’๏_๏’-)""" ,u"""(/◔ ◡ ◔)/"""
    ,u"""(///_ಥ)""" ,u"""(>'o')> ♥ <('o'<)"""
    ,u"""\(◕ ◡ ◕\)""" ,u"""^̮^""" ,u"""^ㅂ^""" ,u"""_(͡๏̯͡๏)_""" 
    ,u"""{´◕ ◡ ◕｀}""" ,u"""{ಠ_ಠ}__,,|,""" ,u"""{◕ ◡ ◕}"""
]

@handles('msg')
def parse(bot, channel, user, msg):
    if msg.lower().strip() == "smile":
        #smiley = urllib2.urlopen("http://dominick.p.elu.so/fun/kaomoji/get.php").read()
        try: bot.msg(channel, choice(smileys).encode("utf-8", "ignore"))
        except: bot.msg(channel, "My jaw hurts")