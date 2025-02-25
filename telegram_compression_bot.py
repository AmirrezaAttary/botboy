# import telebot
# from telebot import types
# from PIL import Image
# import io
# import os

# # توکن ربات تلگرام
# API_TOKEN = '7622125771:AAHQjUyLIXg3qWIVxzbTcwf4cNqCuiOu37A'
# bot = telebot.TeleBot(API_TOKEN)

# # تابع برای فشرده‌سازی عکس
# def compress_image(image_path):
#     with Image.open(image_path) as img:
#         img = img.convert("RGB")  # تبدیل به RGB برای همه فرمت‌ها
#         img.save(image_path, quality=50, optimize=True)

# # دریافت عکس از کاربر
# @bot.message_handler(content_types=['photo'])
# def handle_photo(message):
#     file_info = bot.get_file(message.photo[-1].file_id)
#     downloaded_file = bot.download_file(file_info.file_path)
    
#     # ذخیره عکس دریافت شده به صورت موقت
#     input_image_path = "input_image.jpg"
#     with open(input_image_path, 'wb') as new_file:
#         new_file.write(downloaded_file)

#     # فشرده‌سازی تصویر
#     compress_image(input_image_path)

#     # ارسال تصویر فشرده به کاربر
#     with open(input_image_path, 'rb') as compressed_image:
#         bot.send_photo(message.chat.id, compressed_image)

#     # حذف فایل‌های موقت
#     os.remove(input_image_path)

# # تابع برای inline query
# @bot.inline_handler(lambda query: True)
# def query_text(inline_query):
#     query = inline_query.query.lower()
    
#     # ایجاد نتایج برای inline query
#     if query == "ربات":
#         results = [
#             types.InlineQueryResultArticle(
#                 id="1", title="درباره ربات", input_message_content=types.InputTextMessageContent("این ربات برای فشرده‌سازی تصاویر است.")
#             ),
#             types.InlineQueryResultArticle(
#                 id="2", title="درباره سایت", input_message_content=types.InputTextMessageContent("برای اطلاعات بیشتر به سایت مراجعه کنید.")
#             ),
#             types.InlineQueryResultArticle(
#                 id="3", title="آدرس ربات", input_message_content=types.InputTextMessageContent("آدرس ربات: @YourBotUsername")
#             )
#         ]
#     else:
#         results = []

#     bot.answer_inline_query(inline_query.id, results)

# # شروع ربات با inline query
# bot.infinity_polling()
