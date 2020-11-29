import webbrowser
import pyperclip

clip, oldClip = '', ''

url = "https://translate.google.com/?sl=auto&tl=vi&text={}&op=translate"
from time import sleep
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

while 1:
    sleep(0.1)
    clip = pyperclip.paste()
    if clip != oldClip:
        webbrowser.get('chrome').open(url.format(clip))
        oldClip = clip

