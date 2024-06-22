from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

from ..trendit.auth import trendit_login
from ..utils.helpers import console_log

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    # Check if the user is already authenticated (you can use your own logic here)
    # authenticated = check_user_authentication(user_id)
    authenticated = False

    if authenticated:
        await update.message.reply_text("You are already logged in.")
    else:
        # Send an authentication link or instructions
        await update.message.reply_text("Please enter your credentials: username and password.")


