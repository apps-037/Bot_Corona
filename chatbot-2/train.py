from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")
	print("Removing old database. Training new database")
except:
	print('No database found. Creating new database.')

english_bot = ChatBot('Bot')
english_bot.set_trainer(ListTrainer)
for file in os.listdir('dataset'):
        print('Training using '+file)
        convData = open('dataset/' + file).readlines()
        english_bot.train(convData)
        print("Training completed for "+file)
    

