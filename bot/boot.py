from bot import config
from bot.handlers import command_handlers, error_handlers, message_handlers
from telegram.ext import Application, CommandHandler, MessageHandler, filters


def boot():
    bot = _build_bot()

    _register_command_handlers(bot)
    _register_message_handlers(bot)
    _register_error_handlers(bot)

    _print_start_message()
    _start_bot(bot)


# -------------------------------PRIVATE--------------------------------- #


def _build_bot() -> Application:
    bot_token = config.BOT_TOKEN

    bot = Application.builder().token(bot_token).build()
    return bot


def _register_command_handlers(bot: Application):
    bot.add_handler(CommandHandler("start", command_handlers.handle_start_command))
    bot.add_handler(CommandHandler("help", command_handlers.handle_help_command))


def _register_message_handlers(bot: Application):
    bot.add_handler(
        MessageHandler(filters.TEXT, message_handlers.handle_greetings_message)
    )


def _register_error_handlers(bot: Application):
    bot.add_error_handler(error_handlers.handle_error)


def _start_bot(bot: Application):
    bot.run_polling()


def _print_start_message():
    bot_name: str = config.BOT_NAME

    print(f"{bot_name} is running...")
