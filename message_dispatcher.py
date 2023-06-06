import telebot


# Create a bot
apiToken = "TBD"  # set once a telegram bot is created
bot = telebot.TeleBot(apiToken)


@bot.message_handler(commands=["start"])
def send_msg(message: str) -> None:
    bot.send_message(message.chat.id, message, parse_mode="Markdown")
