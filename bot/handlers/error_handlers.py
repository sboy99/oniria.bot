from telegram import Update
from telegram.ext import ContextTypes


# Commands
async def handle_error(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    print(
        f"""
          Update: {update} caused an error! 
          Error: {ctx.error}
            """
    )
