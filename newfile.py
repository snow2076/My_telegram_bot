import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackContext

# 🟢 توكن بوت التليغرام مالتك
TELEGRAM_BOT_TOKEN = "8184423446:AAFdBvkIWoC8SqJzxWPv0Zd2d1YKGp3Tq3Q"

# 🟢 مفتاح Together AI مالتك
API_KEY = "be2efd7d1fc5a44a44a9c9f2b1d05c856776b5d0dd7567f173ff7d70a2560b36"
URL = "https://api.together.xyz/v1/chat/completions"

# 🔹 دالة لمعالجة الرسائل وإرسالها إلى Together AI
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/Llama-2-7b-chat-hf",  # نموذج مدعوم ومجاني
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post(URL, headers=headers, json=data).json()
    
    reply = response["choices"][0]["message"]["content"]
    await update.message.reply_text(reply)

# 🔹 تشغيل البوت
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()