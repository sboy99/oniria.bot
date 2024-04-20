from telegram import Update
from telegram.ext import ContextTypes


# Commands
async def handle_start_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    reply_text = "Hello, I am Oniria! Nice to meet you!"
    await update.message.reply_text(reply_text)


async def handle_help_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    help_text = "Hey! This is a help text!"
    await update.message.reply_text(help_text)
