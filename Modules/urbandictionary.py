#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from BotKit import command, stylize

@command("ud")
def parse(bot, channel, user, arg):
    resp = urllib2.urlopen("http://www.urbandictionary.com/define.php?term=" + urllib2.quote(arg)).read()
    if "isn't defined." in resp:
        bot.msg(channel, "%s: That word is not defined" % user)
    else:
        soup = BeautifulSoup(resp)
        definitions = [x for x in soup.findAll("div") if x.get('class') and x.get('class') == ['definition']]
        examples = [x for x in soup.findAll("div") if x.get('class') and x.get('class') == ['example']]
        meaning = definitions[0].text.replace('\r', '').strip()
        if len(meaning) > 300:
            bot.msg(channel, stylize.Trunicate(meaning.replace("\n", " ") ,300))
        else:
            bot.msg(channel, meaning.replace("\n", " "))
        stylize.SetMore("%s\n\nExample:\n%s" % (meaning, examples[0].text.strip()))