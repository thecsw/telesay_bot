from gtts import gTTS
import os
import telepot
from telepot.loop import MessageLoop
import config

def say_exit(user_id, text):
    bot.sendMessage(user_id, text)

def handle(msg):
    user_id = msg['chat']['id']
    command = msg['text'].encode('utf-8').lower() # Support lowercase
    if command == "/start":
        say_exit(user_id, "Thank you for starting telesaybot!\n\
Send any text to him and he will send you a computer-generated voice.")
        return
        
    if command == "/help":
        say_exit(user_id, "Send any text message and you will receive a computer-generated voice that reads your message.")
        return
        
    if command[0] == '/':
        say_exit(user_id, "Do not start message with a slash if it is not a command!")
        return
        
    if len(command) > 128:
        say_exit(user_id, "Too many characters ({}). Limit = 128.".format(len(command)))
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

if __name__ == "__main__":
    bot = telepot.Bot(config.key)    
    MessageLoop(bot, handle).run_forever()
else:
    pass
