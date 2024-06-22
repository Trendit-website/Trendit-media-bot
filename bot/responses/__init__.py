from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from ..utils.helpers import console_log
from .auth_responses import handle_login_credentials
from .base_responses import handle_message


def register_responses(app: Application):
    
    # Add message response
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_login_credentials))

