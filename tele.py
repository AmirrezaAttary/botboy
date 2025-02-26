import telebot
import os
from telebot.types import ChatMemberUpdated, ChatJoinRequest

API_TOKEN = '7622125771:AAHQjUyLIXg3qWIVxzbTcwf4cNqCuiOu37A'
bot = telebot.TeleBot(API_TOKEN)

func_in_group= lambda message:message.chat.type in ['supergroup','group']


# ADD
@bot.chat_member_handler()
def handle_new_chat_members(message: ChatMemberUpdated):
    if message.new_chat_member.status == 'member':
        bot.approve_chat_join_request(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, f"Welcome {message.from_user.first_name}!")

@bot.chat_join_request_handler()
def handle_join_request(message: ChatJoinRequest):
    user = message.from_user
    bot.approve_chat_join_request(message.chat.id, user.id)
    bot.send_message(message.chat.id, f"""خوش آمدید, {user.first_name}!
قوانین گروه 
آداب معاشرت داشته باشید.""")


# PIN
@bot.message_handler(commands=['pin'])
def pin_message(message):
    # پیام باید به پیامی که باید پین شود ریپلای شده باشد
    if message.reply_to_message:
        try:
            bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
            bot.send_message(message.chat.id, "Message pinned successfully!")
        except Exception as e:
            bot.send_message(message.chat.id, f"Failed to pin message: {e}")
    else:
        bot.send_message(message.chat.id, "Please reply to the message you want to pin.")




bot.infinity_polling()