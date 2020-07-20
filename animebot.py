import telebot
import time
from jikanpy import Jikan
jikan = Jikan()

mushishi = jikan.search("anime", "mushishi")
result = mushishi['results'][0]
title = result["title"]
bot_token = "1386369868:AAGYpDwxkBG9bZbTAC9ZnBJ5XNyLnP2Srjg"

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "moshi moshi! Get the details of any anime name! type Help to get help on how to.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "type in the name of the anime and recieve the details!")


@bot.message_handler(func = lambda msg: msg.text is not None and "/detail" in msg.text)
def animename(message):
    text = message.text.split()
    anime_name = text[1:]
    name = " ".join(anime_name)
    mushishi = jikan.search("anime", name)
    result = mushishi['results'][0]
    title = result["title"]
    airing = result["airing"]
    synopsis = result["synopsis"]
    rating = result["score"]
    episodes = result["episodes"]
    start_date = result["start_date"]
    members = result["members"]
    rated = result["rated"]

    bot.reply_to(message, f"Title: {title} \nSynopsis: {synopsis}\n\n\nAiring: {airing}\nRating: {rating}\nTotal Episodes: {episodes}\nPopularity: {members} people watched \nRated {rated}\n\n")
    

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)
