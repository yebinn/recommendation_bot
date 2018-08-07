from rtmbot import RtmBot
from rtmbot.core import ACTIVE_PLUGINS

import secret

class HelloPlugin(Plugin):
    def process_message(self, data):
        if "tv" in data["text"]:
            self.outputs.append([data["channel"], ""])

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]

}
bot = RtmBot(config)
bot.start()


print("hi you want to see tv?")
print("sure, why not?")
print("Let's go~!")
