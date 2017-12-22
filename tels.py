from gtts import gTTS
import os
import telepot
from telepot.loop import MessageLoop
<<<<<<< HEAD
import config
bot = telepot.Bot(config.key)
=======
key = ''
bot = telepot.Bot(key)

>>>>>>> ed7f4114f996e3a21425d950ce6af1dc4b81b3db
 
def handle(msg):
    user_id = msg['chat']['id']
    command = msg['text'].encode('utf-8').lower() # Support lowercase
    if command == "/start":
        bot.sendMessage(user_id, "Thank you for starting telesaybot!\n\
Send any text to him and he will send you a computer-generated voice.")
        return
    
    if command == "/help":
        bot.sendMessage(user_id, "Send any text message and you will receive a computer-generated voice that reads your message.")
        return

    bot.sendMessage(user_id, "Processing... Please wait.")
    tts = gTTS(text=command, lang='en')
    tts.save("{}.mp3".format(command))
    bot.sendChatAction(user_id, 'upload_audio')
    bot.sendVoice(user_id, open("{}.mp3".format(command)))

    try:
        os.remove('{}.mp3'.format(command))
    except:
        pass
    
MessageLoop(bot, handle).run_forever()
