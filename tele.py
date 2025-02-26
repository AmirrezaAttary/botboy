import telebot
from telebot.types import ChatPermissions

TOKEN = '7622125771:AAHQjUyLIXg3qWIVxzbTcwf4cNqCuiOu37A'
bot = telebot.TeleBot(TOKEN)
GROUP_ID = -1001234567890  # شناسه گروه

# پیام خوش آمدگویی
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_member in message.new_chat_members:
        welcome_text = f"👋 خوش آمدید {new_member.first_name}! \n لطفاً قوانین گروه را رعایت کنید."
        bot.send_message(message.chat.id, welcome_text)

# پین کردن پیام
@bot.message_handler(commands=['pin'])
def pin_message(message):
    if message.reply_to_message:
        bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        bot.reply_to(message, "✅ پیام پین شد.")
    else:
        bot.reply_to(message, "⚠️ لطفاً روی پیامی ریپلای کنید و دستور /pin را ارسال کنید.")

# اخراج کاربر
@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.unban_chat_member(message.chat.id, user_id)  # جلوگیری از بن شدن دائمی
        bot.reply_to(message, "🚨 کاربر اخراج شد.")

# بن کردن کاربر
@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "⛔️ کاربر بن شد.")

# آنبن کردن کاربر
@bot.message_handler(commands=['unban'])
def unban_user(message):
    if len(message.text.split()) > 1:
        user_id = int(message.text.split()[1])
        bot.unban_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "✅ کاربر آنبن شد.")
    else:
        bot.reply_to(message, "⚠️ لطفاً ID کاربر را مشخص کنید.")

# ارتقا به ادمین
@bot.message_handler(commands=['promote'])
def promote_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.promote_chat_member(message.chat.id, user_id, can_change_info=True, can_delete_messages=True,
                                can_invite_users=True, can_restrict_members=True, can_pin_messages=True,
                                can_promote_members=False)
        bot.reply_to(message, "✅ کاربر به ادمین ارتقا یافت.")

# بازگرداندن به کاربر عادی
@bot.message_handler(commands=['demote'])
def demote_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.promote_chat_member(message.chat.id, user_id, can_change_info=False, can_delete_messages=False,
                                can_invite_users=False, can_restrict_members=False, can_pin_messages=False,
                                can_promote_members=False)
        bot.reply_to(message, "🔽 کاربر به حالت عادی بازگردانده شد.")

bot.infinity_polling()
