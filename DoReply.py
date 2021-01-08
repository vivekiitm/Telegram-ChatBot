from englisttohindi.englisttohindi import EngtoHindi 
from bs4 import BeautifulSoup
import requests
import random
import model

class DoReply:

    def __init__(self, message, from_ , bot):
        self.bot = bot
        try:    
            self.message = message.lower()
        except:
            self.message = None
        self. from_ = from_
        self.errorMessage = "Sorry, but I only understand text messages :("

    def greeting(self):
        user_greetings = ["hi", "hii", "hiii", "hello",  "hola", "greetings",  "wassup", "hey"]
        if self.message in user_greetings:
            bot_greetings = ["howdy", "hi", "hey", "what's good",  "hello","hey there"]
            reply = random.choice(bot_greetings)
            #reply = EngtoHindi(reply)
            #print(reply.convert) 
            self.bot.send_message(reply, self.from_)
            return True
        return False

    def GoogleSearch(self):
        reply = set([])
        try:
            results = 50 
            page = requests.get(f"https://www.google.com/search?q={self.message}&num={results}")
            soup = BeautifulSoup(page.content, "html5lib")
            links = soup.findAll("a")
            for link in links:
                link_href = link.get('href')
                if "url?q=" in link_href and not "webcache" in link_href:
                    s = link.get('href').split("?q=")[1].split("&sa=U")[0]
                    reply.add(s)
                    if(len(reply)>1):
                        break
            return reply
        except:
            return self.errorMessage

    def ReplyBack(self):
        if(self.message == None):
            reply = self.errorMessage
            self.bot.send_message(reply, self.from_)
            return

        if(self.greeting()):
            return

        reply = model.getOutputFromDataBase(self.message)
        if(reply!='-1'):
            self.bot.send_message(reply, self.from_)

        websites = self.GoogleSearch()

        if(type(websites)==str):
            self.bot.send_message(websites, self.from_)
            return

        reply = 'You can check the following websites for more info'
        self.bot.send_message(reply, self.from_)
        for website in websites:
            self.bot.send_message(website, self.from_)

