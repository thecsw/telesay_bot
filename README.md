# Telesay bot

Telegram bot that receives some text as a message in Telegram, reads the text, records it and then sends the voice message back to the user. This project is out because of a competition that I made with my friend that I couldn't do this bot in under 10 minutes. Took around 8 minutes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
sudo apt-get install espeak
sudo pip install telepot
sudo pip install gTTS
```
[telepot](https://github.com/nickoala/telepot) is a python framework for Telegram Bot API. This package will be used to connect to Telegram API and to communicate with users over the internet.

[eSpeak](http://espeak.sourceforge.net/) is a compact open source software speech synthesizer for English and other languages, for Linux and Windows.

[gTTS](https://pypi.python.org/pypi/gTTS) a *Python* interface for Google's _Text to Speech_ API.

### Installing

Nothing too complicated. The source code is written in python, so no worries.

The only thing that needs to be done before execution is the config profile. In the config profile you should fill your Reddit API details and Telegram Bot's unique API key.

For that please follow these steps

```bash
git clone https://github.com/thecsw/telesay_bot
cd telesay_bot
mv example.config.py config.py
nano config.py
```

Now here, you can use any text editor you like. When opening the file you will see this

```python
key = ''
```

So what will you need to do now is to get your Telegram API token from [BotFather](https://telegram.me/botfather)

After filling out the key, save and exit.

## Deployment

Config file is ready and you are good to go!

Just run this

```bash
python tels.py
```

That is everything. The script now just runs and any user that is connected to your Telegram bot can request a joke via the /joke command.

## Source code

Overall code is very simple and stright-forward.

There are some things that I want to mention.

Firstly, gTTS has limitation to 128 characters, so validation is included here

```python
if len(command) > 128:
   say_exit(user_id, "Too many characters ({}). Limit = 128.".format(len(command)))
   return
```

Secondly, gTTS cannnot record text if it starts with a slash

```python
if command[0] == '/':
   say_exit(user_id, "Do not start message with a slash if it is not a command!")
   return
```

Thirdly, no matter what the created mp3 file be deleted

```python
try:
	os.remove('{}.mp3'.format(command))
except:
    pass
```

## Built With

* [telepot](https://github.com/nickoala/telepot) - python framework for Telegram Bot API.

* [eSpeak](http://espeak.sourceforge.net/) is a compact open source software speech synthesizer for English and other languages, for Linux and Windows.

* [gTTS](https://pypi.python.org/pypi/gTTS) a *Python* interface for Google's _Text to Speech_ API.

## Authors

* **Sagindyk Urazayev** - *Initial work* - [thecsw](https://github.com/thecsw)

## License

This project is licensed under the The GNU General Public License - see the [LICENSE.md](https://github.com/thecsw/rjokes/blob/master/LICENSE) file for details