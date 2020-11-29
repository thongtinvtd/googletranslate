import pyperclip
from googletrans import Translator
from time import sleep

tran = Translator()
clip, oldClip = '', ''
while 1:
    sleep(0.1)
    # print('.')
    clip = pyperclip.paste()
    if clip != oldClip:
        des = tran.translate(clip, dest = 'vi')
        oldClip = clip
        print(des.text)
