from typing import Final
from telegram import Update
from telegram.ext import ContextTypes

from bot import config


async def handle_greetings_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    chat_type = update.message.chat.type
    chat_message = update.message.text

    if chat_type == "group":
        reply_text = _handle_group_message(chat_message)
        await update.message.reply_text(reply_text)
        return

    reply_text = _greet(chat_message)
    await update.message.reply_text(reply_text)


# -------------------------------PRIVATE--------------------------------- #


def _handle_group_message(text: str) -> str:
    bot_username: Final = config.bot_username

    if bot_username in text:
        updated_text = text.replace(bot_username, "").strip()
        return _greet(updated_text)

    return _greet(text)


def _greet(text: str) -> str:
    user_message = text.lower()

    if user_message in ["hi", "hello", "hey", "hola"]:
        return "Hello! I'm Oniria. How can I help you today?"

    if user_message in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking. How can I help you today?"

    if user_message in ["what's your name", "who are you"]:
        return "I'm Oniria. How can I help you today?"

    if user_message in ["bye", "goodbye", "adios"]:
        return "Goodbye! Have a nice day!"

    return "Sorry, I don't understand that. Please ask me something else."
