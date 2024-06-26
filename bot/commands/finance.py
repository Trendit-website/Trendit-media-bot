from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

from ..extensions import api

async def fetch_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle fetching balance."""
    response_data = api.fetch_wallet_balance()
    balances = response_data["balances"]
    if balances:
        available_balance = balances["available_balance"]
        ledger_balance = balances["ledger_balance"]
        message = (f"WALLET BALANCES: \n\n • AVAILABLE BALANCE: ₦ {available_balance} \n • LEDGER BALANCE: ₦ {ledger_balance} \n")
        
        await update.callback_query.message.reply_text(f"{message}")
    else:
        await update.callback_query.message.reply_text("Failed to fetch wallet balance.")
    await update.callback_query.answer()