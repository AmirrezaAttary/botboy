import telebot
import os
from yt_dlp import YoutubeDL

# توکن ربات را اینجا قرار دهید
API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

# تنظیمات yt-dlp برای دانلود ویدئو
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  # ذخیره فایل با نام و فرمت اصلی
}

# پیام خوش‌آمدگویی و توضیحات دستورات
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "سلام! 👋\n"
        "من یک ربات دانلود ویدئو از یوتیوب هستم. 🎥\n\n"
        "🔗 کافیست لینک ویدئوی یوتیوب را ارسال کنید تا من آن را برای شما دانلود کنم.\n"
        "📥 ویدئو به صورت پاسخ به پیام شما ارسال خواهد شد."
    )
    bot.send_message(message.chat.id, welcome_text)

# پردازش لینک یوتیوب
@bot.message_handler(func=lambda message: 'youtube.com' in message.text or 'youtu.be' in message.text)
def download_video(message):
    url = message.text
    bot.reply_to(message, "در حال دانلود ویدئو... ⏳")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_title = info.get('title', 'video')
            file_ext = info.get('ext', 'mp4')
            filename = f"{video_title}.{file_ext}"
            
        # ارسال ویدئو در حالت reply
        with open(filename, 'rb') as video:
            bot.send_video(
                message.chat.id,
                video,
                caption=f"🎬 {video_title}",
                reply_to_message_id=message.message_id
            )
        
        # حذف فایل بعد از ارسال
        os.remove(filename)
        
    except Exception as e:
        bot.reply_to(message, f"❌ خطایی رخ داد: {str(e)}")

# شروع ربات
bot.infinity_polling()