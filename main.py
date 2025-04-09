import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! به ربات محاسبه سیستم خورشیدی خوش آمدید. برای افزودن وسیله دستور /adddevice را وارد کنید.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("دستورات:\n/start - شروع\n/help - راهنما\n/adddevice - افزودن وسیله")

def add_device(update: Update, context: CallbackContext):
    update.message.reply_text("لطفاً مشخصات وسیله را وارد کنید:\nنام، توان(W)، تعداد، ساعت مصرف روز، ساعت مصرف شب، موتوری هست؟ (بله/خیر)")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("adddevice", add_device))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
