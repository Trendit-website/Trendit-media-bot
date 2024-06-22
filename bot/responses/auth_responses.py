from telegram import Update
from telegram.ext import CallbackContext, ContextTypes


from config import Config
from ..utils.helpers import console_log
from ..trendit.auth import trendit_login

async def handle_login_credentials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    credentials = update.message.text.split()  # Assuming space-separated username and password

    # Validate credentials (you can replace this with your own logic)
    data = {
        "username": credentials[0],
        "pwd": credentials[1]
    }
    response_data = trendit_login(data)

    if response_data and response_data["status"] == "success":
        console_log("response_data", response_data)
        
        access_token: str = response_data["access_token"]
        
        update.message.reply_text(f"You are now logged in! Your access token is {access_token}")
    else:
        update.message.reply_text("Invalid credentials. Please try again.")