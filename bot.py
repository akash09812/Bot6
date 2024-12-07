from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai
import os

# API Keys (ye Replit me setup honge)
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ChatGPT Response Function
def chat_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Kuch galat hua! Dobara try karein."

# Commands
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Namaste! Main ek GPT-powered bot hoon. Mujhse kuch bhi poochhein!")

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    reply = chat_with_gpt(user_message)
    update.message.reply_text(reply)

# Main Function
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
