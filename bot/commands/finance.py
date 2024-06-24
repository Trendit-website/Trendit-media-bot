from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

from ..extensions import api

async def fetch_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle fetching balance."""
    balance = api.fetch_wallet_balance()
    if balance:
        await update.callback_query.message.reply_text(f"Wallet Balance: {balance['amount']}")
    else:
        await update.callback_query.message.reply_text("Failed to fetch wallet balance.")
    await update.callback_query.answer()