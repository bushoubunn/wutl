#coding:utf-8
import django
from django.conf import settings
#japanese text segmentaion
import nagisa
string='何がちゃうねん、言うてみ'
string00='明日東京いかたん'
word=nagisa.tagging(string)
word00=nagisa.tagging(string00)
print(word.words)
print(word00.words)
