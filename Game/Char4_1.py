# -*- coding: utf-8 -*-

import random

guesstoken=0

print('你好，你叫什么名字？')

myname=input()

number=random.randint(1,20)

print('好的。' + myname + ', 请你猜一个1到20之间的整数。你有6次机会')

while guesstoken<6:
    print('请猜一个数。')

    guess=input()

    guess=int(guess)

    guesstoken=guesstoken+1

    if guess<number:
        print('太小了，' + myname + ',重猜吧')

    if guess>number:
        print('啊哦，太大了，' + myname + ',重猜吧')

    if guess==number:
        print('太棒了！'+myname+',你猜对了！')
        break

if guess!=number:
    print('啊，你6次都猜错了。下次再来吧')
    print('应该是'+str(number))
