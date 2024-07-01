'''
This package contains commands for Trendit³ Telegram Bot


@author: Emmanuel Olowu
@link: https://github.com/zeddyemy
@package: Trendit³ Bot
'''
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from .base import start, help, group_id
from .auth import login
from .task import fetch_tasks, reject_task, approve_task, pending_task_orders
from .finance import fetch_balance
from .services import send_notification, update_prices
from .stats import fetch_stats
from .profile import pending_social_profiles

def register_commands(app: Application):
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("login", login))
    
    # tasks
    app.add_handler(CommandHandler("tasks", fetch_tasks))
    app.add_handler(CommandHandler("reject", reject_task))
    app.add_handler(CommandHandler("approve", approve_task))
    app.add_handler(CommandHandler("pending_task_orders", pending_task_orders))
    
    app.add_handler(CommandHandler("group_id", group_id))
    
    # stats
    app.add_handler(CommandHandler("fetch_stats", fetch_stats))
    
    # social Profiles
    app.add_handler(CommandHandler("pending_social_profiles", pending_social_profiles))
