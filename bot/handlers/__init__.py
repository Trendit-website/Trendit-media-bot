from telegram import Update
from telegram.ext import Application, CallbackQueryHandler

from ..utils.helpers import console_log
from .error import error_handler
from .callback import callback_query_handler
from ..commands import fetch_balance, send_notification, update_prices
from .callback import fetch_stats_callback


def add_callback_handlers(app: Application):
    
    # Add callback handler
    app.add_handler(CallbackQueryHandler(callback_query_handler))
    
    # Add individual handlers for new commands
    app.add_handler(CallbackQueryHandler(fetch_stats_callback, pattern='fetch_stats_callback'))
    app.add_handler(CallbackQueryHandler(fetch_balance, pattern='fetch_balance'))
    app.add_handler(CallbackQueryHandler(send_notification, pattern='send_notification'))
