from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

from config import Config
from .utils.helpers import console_log

BOT_USERNAME = Config.BOT_USERNAME


def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if processed == "":
        return "How can I help You?"
    
    if "hello" in processed:
        return "Hey There!"
    
    return "I don't quite get you"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    console_log(
        "Message Info",
        (f"\
            User ID: {update.message.from_user.id}\n \
            Message Type: {message_type}\n \
            Message: {text}"
        )
    )
    
    if message_type == "group" or message_type == "supergroup":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
        
    console_log("Bot:", response)
    await update.message.reply_text(response)
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    console_log(f"Update {update} caused error {context.error}", context.error)