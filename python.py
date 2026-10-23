import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# BotFather se apna NEW token daalo
BOT_TOKEN = "8454459218:AAGA1jMxvGOzxwxRiX5miL_A-QR80DxU0VQ"
OWNER_USERNAME = "VTX_Monster\n @ITS_EGOIST90"

bot = telebot.TeleBot(BOT_TOKEN)


def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton(
            "👑  Owner",
            url=f"https://t.me/{OWNER_USERNAME}"
        ),
        InlineKeyboardButton(
            "✨ About Bot",
            callback_data="about"
        ),
        InlineKeyboardButton(
            "🆘 Help",
            callback_data="help"
        ),
        InlineKeyboardButton(
            "💬 Chat With Owner",
            url=f"https://t.me/{OWNER_USERNAME}"
        )
    )

    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    user = message.from_user
    name = user.first_name or "Friend"

    text = (
        "╭━━━ ✦ 𝙃𝘼𝙔 𝙄 𝘼𝙈 𝘽𝘼𝘿𝘼𝙇 𝙃𝙊𝙒 𝘾𝘼𝙉𝙀 𝙃𝙀𝙇𝙋 𝙔𝙊𝙐  ✦ ━━━╮\n\n"
        f"👋 Welcome, {name}!\n\n"
        "💫 Welcome to my Telegram world!\n"
        "✨ Explore the menu below.\n\n"
        f"🆔 Your ID: {user.id}\n"
        f"👑 Owner: @{OWNER_USERNAME}\n\n"
        "╰━━ Stay Cool & Be Kind ━━╯"
    )

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=main_menu()
    )


@bot.callback_query_handler(
    func=lambda call: call.data in ["about", "help"]
)
def button_handler(call):
    if call.data == "about":
        text = (
            "✨ ABOUT VTX CHAT HUB ✨\n\n"
            "A stylish Telegram welcome bot.\n"
            "Made to connect visitors with the owner.\n\n"
            f"👑 Owner: @{OWNER_USERNAME}"
        )

    else:
        text = (
            "🆘 HELP MENU\n\n"
            "/start - Open main menu\n"
            "/help - Show help\n\n"
            "Use the buttons to explore the bot."
        )

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        text,
        reply_markup=main_menu()
    )


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "🆘 Use /start to open the main menu.",
        reply_markup=main_menu()
    )


print("VTX Chat Hub is running...")
bot.infinity_polling()
