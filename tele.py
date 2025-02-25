import telebot
import yt_dlp
import os

# 🔑 توکن ربات را اینجا قرار دهید
TOKEN = '7622125771:AAHQjUyLIXg3qWIVxzbTcwf4cNqCuiOu37A'

# 📥 مسیر فایل کوکی
COOKIE_FILE = 'cookies.txt'

# ⚙️ پیکربندی yt-dlp برای دانلود ویدئو
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
    'cookiefile': COOKIE_FILE  # استفاده از کوکی برای دور زدن محدودیت‌ها
}

# 🎯 ایجاد ربات
bot = telebot.TeleBot(TOKEN)

# 💬 پیام شروع
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "سلام! 👋\n\n"
        "این ربات می‌تواند ویدئوهای یوتیوب را برای شما دانلود کند.\n"
        "📌 کافیست لینک ویدئو را ارسال کنید.\n\n"
        "دستورات موجود:\n"
        "/start - شروع به کار ربات\n"
        "/help - راهنما"
    )
    bot.reply_to(message, welcome_text)

# 📺 دانلود ویدئو از یوتیوب
@bot.message_handler(func=lambda message: 'youtube.com' in message.text or 'youtu.be' in message.text)
def download_video(message):
    url = message.text
    bot.reply_to(message, "🔄 در حال دانلود ویدئو... لطفاً صبور باشید.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        # آپلود ویدئو به عنوان پاسخ به پیام لینک
        with open(filename, 'rb') as video:
            bot.send_video(
                message.chat.id,
                video,
                caption=f"🎬 {info.get('title', 'ویدئو')}",
                reply_to_message_id=message.message_id
            )

        # حذف فایل پس از ارسال
        os.remove(filename)

    except Exception as e:
        bot.reply_to(message, f"❌ خطایی رخ داد: {str(e)}")

# 🚀 اجرای ربات
if __name__ == "__main__":
    bot.infinity_polling()
