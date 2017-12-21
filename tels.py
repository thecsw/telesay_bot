from gtts import gTTS
import os
import telepot
from telepot.loop import MessageLoop
key = ''
bot = telepot.Bot(key)

 
def handle(msg):
    user_id = msg['chat']['id']
    command = msg['text'].encode('utf-8').lower() # Support lowercase
    tts = gTTS(text=command, lang='en')
    tts.save("{}.mp3".format(command))
    bot.sendVoice(user_id, open("{}.mp3".format(command)))

    try:
        os.remove('{}.mp3'.format(command))
    except:
        pass
MessageLoop(bot, handle).run_forever()
