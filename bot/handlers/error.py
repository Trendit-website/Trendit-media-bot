from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


from ..utils.helpers import console_log, log_error


def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log Errors caused by Updates."""
    console_log(f"Update {update} caused error {context.error}", context.error)
    log_error("Exception while handling an update:", context.error)
    
    
    console_log(f"update {update} caused error:", str(context.error))