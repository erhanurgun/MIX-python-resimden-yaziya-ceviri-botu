import Constants as keys
import Responses as R
import pytesseract
import telegram
import os
from traceback import print_exc
from telegram.ext import *

try:
    from PIL import Image
except ImportError:
    import Image

print("Bot başlatılıyor...")

def start_command(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    return_message0 = 'Merhaba, *' + first_name + '*'
    return_message1 = '⭕ Hemen bir resim gönder ve senin için resmin içindeki yazıyı okuyayım 😉'
    return_message2 = '⭕ *%96* oranında doğru okuyabilirim. Geliştiricim *%100* oranında okuyabilmem için beni sürekli güncelliyor 😇'
    return_message3 = '⭕ Ne kadar net bir resim gönderirsen senin için o kadar doğru bir şekilde okuyabilirim ❗️'
    update.message.reply_text(return_message0, quote=True, parse_mode=telegram.ParseMode.MARKDOWN)
    update.message.reply_text(return_message1)
    update.message.reply_text(return_message2, parse_mode=telegram.ParseMode.MARKDOWN)
    update.message.reply_text(return_message3)

def help_command(update, context):
    update.message.reply_text('Eğer yardıma ihtiyacın varsa! Bunu Google Amca\'dan istemelisin 😇', quote=True)

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response, quote=True)

def convert_image(update, context):
    # print(update.message)
    filename = "test.jpg"
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.get_file(file_id)
    print(update.message.photo)
    newFile.download(filename)
    # update.message.reply_text("Bu bir resim mesajıdır")

    try:
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        extracted_string = pytesseract.image_to_string(Image.open(filename), lang="tur")
        update.message.reply_text(extracted_string, quote=True)
        os.remove(filename)
    except Exception:
        print_exc()
        if extracted_string is not None:
            update.message.reply_text(extracted_string, quote=True)
            os.remove(filename)

def error(update, context):
    print(f"Update {update} caused of {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.photo, convert_image))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()