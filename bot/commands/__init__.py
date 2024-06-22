'''
This package contains commands for Trendit³ Telegram Bot


@author: Emmanuel Olowu
@link: https://github.com/zeddyemy
@package: Trendit³ Bot
'''
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from .base import start, help
from .auth import login

def register_commands(app: Application):
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("login", login))