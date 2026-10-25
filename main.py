import telebot

# التوكن الخاص بك مضمن هنا مباشرة
TOKEN = "7275178891:AAFTCA9Wd5-5LUnOBonUi51NE4glDe5pRH8"
bot = telebot.TeleBot(TOKEN)

# الترحيب بالأعضاء الجدد
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for member in message.new_chat_members:
        bot.reply_to(message, f"أهلاً بك يا {member.first_name} في المجموعة! نورتنا 🌸")

# الرد على رسائل المشتركين
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = message.text
    bot.reply_to(message, f"أهلاً بك! لقد استلمت رسالتك وأقوم بإدارة المجموعة بنجاح.")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
