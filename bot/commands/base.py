from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am your task approval bot. Use /approve to handle tasks.')
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am here to assist you.')