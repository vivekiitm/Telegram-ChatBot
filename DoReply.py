from bs4 import BeautifulSoup
import requests
import random

class DoReply:

    def __init__(self, message, from_ , bot):
        self.bot = bot
        self.message = message.lower()
        self. from_ = from_

    def greeting(self):
        user_greetings = ["hi", "hello",  "hola", "greetings",  "wassup","hey"]
        if self.message in user_greetings:
            bot_greetings = ["howdy","hi", "hey", "what's good",  "hello","hey there"]
            reply = random.choice(bot_greetings)
            self.bot.send_message(reply, self.from_)
            return True
        return False

    def GoogleSearch(self):
        results = 50 
        page = requests.get(f"https://www.google.com/search?q={self.message}&num={results}")
        soup = BeautifulSoup(page.content, "html5lib")
        links = soup.findAll("a")
        reply = set([])
        for link in links:
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                s = link.get('href').split("?q=")[1].split("&sa=U")[0]
                reply.add(s)
                if(len(reply)>1):
                    break
        return reply

    def ReplyBack(self):
        if(self.greeting()):
            return
        websites = self.GoogleSearch()
        reply = 'You can check the following websites for more info'
        self.bot.send_message(reply, self.from_)
        for website in websites:
            self.bot.send_message(website, self.from_)

