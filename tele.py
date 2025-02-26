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
قوانین گروه""")


# PIN
bot.message_handler(commands='pin')
def pin_message_handeler(message):
    bot.send_message(message.chat.id,'پیام را برای پین کردن به من بده')
    bot.register_next_step_handler(message,message_pinner)

def message_pinner(message):
    bot.pin_chat_message(message.chat.id,message.message_id)



bot.infinity_polling()