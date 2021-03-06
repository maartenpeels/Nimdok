from BotKit import handles

@handles('msg')
def parse(bot, channel, user, msg):
	usr = user
	msg = msg.strip()
	s = msg.split(':',2)
	if len(s) > 1:
		usr = s[0]
		msg = s[1].strip()
	if msg[:4] == ">>>/" and msg[-1] == "/" and len(msg[4:-1]) in [1,2,3]:
		bot.msg(channel, "%s: https://boards.4chan.org/%s/" % (usr, msg[4:-1]))