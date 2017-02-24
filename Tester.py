# encoding: utf-8
import random
from random import choice

D = [u'扭了扭老腰', u'往裤裆下一躲', u'快速趴下求饶', u'使用了撒石灰遁术', u'获得宝爷加持']
G = [u'海底捞月', u'黑虎掏心', u'羊癫疯', u'神一样的技能[神经病]', u'吐口水']


class Game:
    def __init__(self, name, hp, at, de, hit, per, dex, sp):
        self.name = name
        self.hp = hp
        self.at = at
        self.de = de
        self.hit = hit
        self.per = per
        self.dex = dex
        self.sp = sp


y = Game(u"老羊", 120, 40, 10, 40, 20, 20, 22)
j = Game(u"小姜", 150, 20, 25, 30, 50, 15, 18)


# 判断谁先出手
def sp_p(p1, p2):
    if p1.sp + (100 - random.randint(0, 100)) >= p2.sp + (100 - random.randint(0, 100)):
        sp_player = 0
    else:
        sp_player = 1
    return sp_player


# 判断是否命中
def hit_p(p1, p2):
    if p1.hit + 50 - p2.hit >= (100 - random.randint(0, 100)):
        hit_player = 0
    else:
        hit_player = 1
    return hit_player


# 判断是否暴击
def dex_p(p1, p2):
    if p1.dex >= (100 - random.randint(0, 100)):
        dex_player = 0
    else:
        dex_player = 1
    return dex_player


def player(p1, p2):
    hit_player = hit_p(p1, p2)
    if hit_player == 0:
        # 判断是否暴击
        dex_player = dex_p(p1, p2)
        p2.hpa = 0
        if dex_player == 0:
            # 单次被攻击掉的血量
            p2.hpa = p1.at * 2 - p2.de
            p2.hp = p2.hp - p2.hpa
            if p2.hp <= 0:
                p2.hp = 0
                print u"〖" + p1.name + u"〗" + u"使用了[" + choice(G) + "]" + u"暴击成功!" + p2.name + u"被打死了,减少血量:" + str(
                        p2.hpa) + u":当前血量:" + u"[" + p1.name + u":" + str(p1.hp) + u"|" + p2.name + u":" + str(
                        p2.hp) + u"]"
            else:
                print u"〖" + p1.name + u"〗" + u"使用了[" + choice(G) + "]" + u"暴击成功!" + p2.name + u"被打掉了" + str(
                        p2.hpa) + u",剩余血量为:" + u"[" + p1.name + u":" + str(p1.hp) + u"|" + p2.name + u":" + str(
                        p2.hp) + u"]"

        else:
            p2.hpa = p1.at - p2.de
            p2.hp = p2.hp - p2.hpa
            if p2.hp <= 0:
                p2.hp = 0
                print u"〖" + p1.name + u"〗" + u"使用了[" + choice(G) + "]" + u"暴击成功!" + p2.name + u"被打死了,减少血量:" + str(
                        p2.hpa) + u"当前血量" + u"[" + p1.name + u":" + str(p1.hp) + u"|" + p2.name + u":" + str(
                        p2.hp) + u"]"
            else:
                print u"〖" + p1.name + u"〗" + u"使用了[" + choice(G) + "]" + u"攻击成功!" + p2.name + u"被打掉了" + str(
                        p2.hpa) + u",剩余血量为:" + u"[" + p1.name + u":" + str(p1.hp) + u"|" + p2.name + u":" + str(
                        p2.hp) + u"]"
    else:
        print u"〖" + p1.name + u"〗" + u"失手了!" + p2.name + choice(
                D) + u",躲避成功!" + u",剩余血量为:" + u"[" + p1.name + u":" + str(p1.hp) + u"|" + p2.name + u":" + str(
                p2.hp) + u"]"


# 调用攻击规则
def kill(p1, p2):
    i = 0
    while p2.hp > 0 and p1.hp > 0:
        i = i + 1
        print u"第" + str(i) + u"回合"
        if p2.hp > 0 and p1.hp > 0:
            sp_player = sp_p(p1, p2)
            if sp_player == 1:
                if p1.hp > 0:
                    player(p1, p2)
                    if p2.hp > 0:
                        player(p2, p1)
                else:
                    break
            else:
                if p2.hp > 0:
                    player(p2, p1)
                    if p1.hp > 0:
                        player(p1, p2)
                else:
                    break
        else:
            print "Game Over"


kill(y, j)
