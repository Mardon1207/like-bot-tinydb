from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,CallbackContext,Filters,MessageHandler
import json
import os
from db import LikeDB
db=LikeDB('db.json')
TOKEN=os.environ.get("TOKEN")
updater=Updater(TOKEN)
dp=updater.dispatcher
def start(update,context):
    chat_id = update.message.chat.id
    bot = context.bot
    like=KeyboardButton(text="👍")
    dislike=KeyboardButton(text="👎")
    keyboard=ReplyKeyboardMarkup(
        [[like,dislike]],resize_keyboard=True
    )
    db.save(chat_id)
    bot.sendMessage(chat_id,text="like_and_dislike",reply_markup=keyboard)

def text(update,context):
    like="👍"
    dislike="👎"
    bot=context.bot
    message=update.message.text
    chat_id=update.message.chat.id
    if message==like:
        db.like(chat_id)
    elif message==dislike:
        db.dislike(chat_id)
    text=f'LIKE {db.add_like(chat_id)} \t DISLIKE {db.add_dislike(chat_id)}'
    bot.sendMessage(chat_id,text)
    
    

dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text,text))
updater.start_polling()
updater.idle()