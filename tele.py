import telebot
from telebot.types import ChatMemberUpdated ,ChatJoinRequest

TOKEN = '7622125771:AAHQjUyLIXg3qWIVxzbTcwf4cNqCuiOu37A'
bot = telebot.TeleBot(TOKEN)



@bot.chat_member_handler()
def handle_new_chat_members(message: ChatMemberUpdated):
    if message.new_chat_member.status == 'member':
        bot.approve_chat_join_request(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, f"Welcome {message.from_user.first_name}!")

@bot.chat_join_request_handler()
def handle_join_request(message: ChatJoinRequest):
    user = message.from_user
    bot.approve_chat_join_request(message.chat.id, user.id)
    bot.send_message(message.chat.id, f"به گروه خوش آمدید{user.first_name}! \n لطفا قوانین گروه را رعایت کنید")


@bot.message_handler(commands=['pin'])
def pin_message(message):
    if message.reply_to_message:
        bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        bot.reply_to(message, "✅ پیام پین شد.")
    else:
        bot.reply_to(message, "⚠️ لطفاً روی پیامی ریپلای کنید و دستور /pin را ارسال کنید.")


@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.unban_chat_member(message.chat.id, user_id)  # جلوگیری از بن شدن دائمی
        bot.reply_to(message, "🚨 کاربر اخراج شد.")


@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "⛔️ کاربر بن شد.")


@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.unban_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "✅ کاربر آنبن شد.")
    elif len(message.text.split()) > 1:
        try:
            user_id = int(message.text.split()[1])
            bot.unban_chat_member(message.chat.id, user_id)
            bot.reply_to(message, "✅ کاربر آنبن شد.")
        except ValueError:
            bot.reply_to(message, "⚠️ لطفاً ID معتبر وارد کنید.")
    else:
        bot.reply_to(message, "⚠️ لطفاً روی پیامی ریپلای کنید یا ID کاربر را وارد کنید.")


@bot.message_handler(commands=['promote'])
def promote_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.promote_chat_member(message.chat.id, user_id, can_change_info=True, can_delete_messages=True,
                                can_invite_users=True, can_restrict_members=True, can_pin_messages=True,
                                can_promote_members=False)
        bot.reply_to(message, "✅ کاربر به ادمین ارتقا یافت.")


@bot.message_handler(commands=['demote'])
def demote_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.promote_chat_member(message.chat.id, user_id, can_change_info=False, can_delete_messages=False,
                                can_invite_users=False, can_restrict_members=False, can_pin_messages=False,
                                can_promote_members=False)
        bot.reply_to(message, "🔽 کاربر به حالت عادی بازگردانده شد.")

bot.infinity_polling()
