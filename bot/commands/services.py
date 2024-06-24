from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ContextTypes

from ..extensions import api

async def send_notification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle sending notifications."""
    # Implement the logic to send a notification
    await update.callback_query.message.reply_text("Send notification function not implemented yet.")
    await update.callback_query.answer()

async def update_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle updating price."""
    # Implement the logic to update price
    await update.callback_query.message.reply_text("Update price function not implemented yet.")
    await update.callback_query.answer()