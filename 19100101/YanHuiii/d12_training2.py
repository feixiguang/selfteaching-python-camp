'''这是一个利用wxpy功能自动完成微信登录和获取好友转发的网址信息，
将信息中的主要内容提取及获取词频反馈，并把结果发给好友的程序'''

import training1
from wxpy import *

'''登录微信'''
bot = Bot()

'''选取特定的对象小明'''
object1 = bot.friends()



@bot.register(object1)
def SHARING_Msg (msg) :
	if msg.type == 'Sharing' :
	    url = msg.url
	    object1.send(training1.stats_meg(url))
	else :
	    print("您的好友还没发给您关于分享类型的信息")

embed()