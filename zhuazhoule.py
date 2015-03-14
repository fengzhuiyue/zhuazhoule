#! /usr/bin/python
# coding:utf-8


"""

    跳跳抓周v1.0
    http://detail.tmall.com/item.htm?spm=a230r.1.14.8.LJIDF5&id=39269027652&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=18
    
    ToDoList:
        1.
        2.

"""


from random import *
import sys,select


def get_list_index(zz_list):
    list_len   = len(zz_list)
    return randint(1,list_len) - 1


def kbhit():
    fd = sys.stdin.fileno()
    r = select.select([sys.stdin],[],[],0.01)
    rcode = ''
    if len(r[0]) >0:
        rcode  = sys.stdin.read(1)
    return rcode

#抓周清单
zz_list = {
    "官星印":"命中有官，官运亨通。在中国，龙代表着至高无上的权利，印章又是权力和地位的象征。",
    "王亥算":"易商好商，商界巨子。该物为算盘羊秤砣。秤砣是最原始的物物交换工具，而算盘表示精打细算，有“算盘一响，黄金万两”之说。",
    "串铃":"心地善良，医行天下。串铃是过去行医的标志，也是卖药者的护身符。",
    "伊尹镬":"守家爱家，一生幸福。伊尹是民间的厨神，是中国烹饪的鼻祖。他在烹饪方面有很多的发明创造。而此物则是古代的一种很有代表性的炊具。",
    "鲁班斗":"心灵手巧，长于设计。",
    "陀螺乐":"喜欢运动，体坛巨星。",
    "仓颉简":"学识渊博，前途无量。",
    "酒令筹筒":"喜好交际，友遍天下。",
    "洪崖乐":"性格活泼，能歌善舞。洪崖制乐器作五律铸十二钟，是华夏音乐始祖",
    "将军盔":"爱武尚武，易军易武。",
    "食神盒":"口中有福，享尽美味。",
    "财满星":"命中有财，一生富贵。",
    }
print '\33[1;32;47m',
print "[跳跳抓周乐，感谢爸爸!]"
print '\033[0m'
print "\n\n\n"

print "抓周开始，请按任意键开始抓周,按‘q'退出\n\n\n"
while 1:
    c = kbhit()
    if c == 'q':
        sys.exit(1)
    elif len(c) !=0:
        index = get_list_index(zz_list)
        print '\33[1;31;47m',
        print "跳跳抓到的是%s" % zz_list.keys()[index]
        print " 寓意:%s" % zz_list.values()[index]
        print '\033[0m'        
        break

print "\n\n\n跳跳，爸爸妈妈为你感到骄傲，无论你将来成为什么样子的人，爸爸妈妈都支持你，爱你！"






