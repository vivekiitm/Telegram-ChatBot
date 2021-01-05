from bot import telegram_chatbot
from DoReply import DoReply
bot = telegram_chatbot("config.cfg")

update_id = None

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            user = item["message"]["from"]["first_name"]
            print(user, message)
            Reply = DoReply(message,from_,bot)
            Reply.ReplyBack()
