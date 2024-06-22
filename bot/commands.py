from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am your task approval bot. Use /approve to handle tasks.')
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am here to assist you.')

async def handle_approval(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the task approval command."""
    update.message.reply_text("Fetching tasks for approval...")
    # Here you might want to call a function that fetches tasks from your backend
