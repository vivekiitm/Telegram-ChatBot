Bot Name: IIT Mandi
Bot UserName: IIT_Mandi_bot

Github Link: https://github.com/vivekiitm/Telegram-ChatBot

Features Implemented:
If the answer to the question asked by the user is found in the database with accuracy more than the threshold value which is set at 60%, then the reply is given directly from the database. In addition to it if the accuracy of best response is less than 85%, then top two google searches are also provided for reference. If the input is not valid i.e, other than plain english text, be it pictures or hindi text,  then the error message is sent as a reply to the user.

Model Used:
Sequential Neural Networks are used for searching questions in databases.

How To Run:
1. You have to enter your personnel bot token-id in config.cfg.
2. Pre-trained model is saved as saved_model.pb in the chat_model folder.
3. In addition to it you can train the model by running train_chatbot.py.
4. intents.json contains the dataset on which my model is being trained.
5. Finally run server.py to run the bot.
