'''
This package contains commands for Trendit³ Telegram Bot


@author: Emmanuel Olowu
@link: https://github.com/zeddyemy
@package: Trendit³ Bot
'''
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from .base import start, help, group_id
from .auth import login
from .task import fetch_tasks, reject_task, approve_task
from .finance import fetch_balance
from .services import send_notification, update_prices

def register_commands(app: Application):
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("login", login))
    
    app.add_handler(CommandHandler("tasks", fetch_tasks))
    app.add_handler(CommandHandler("reject", reject_task))
    app.add_handler(CommandHandler("approve", approve_task))
    
    app.add_handler(CommandHandler("group_id", group_id))