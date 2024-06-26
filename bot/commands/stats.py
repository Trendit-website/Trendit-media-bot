from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ContextTypes
from datetime import date


from ..extensions import api

async def fetch_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    response_data = api.fetch_stats()
    stats = response_data["stats"]
    
    today = date.today()
    today_date = today.strftime("%B %d, %Y")
    
    firstname = update.message.from_user.first_name
    
    if stats:
        new_signups = stats["new_signups"]
        new_task = stats["new_task"]
        approved_tasks = stats["approved_tasks"]
        rejected_tasks = stats["declined_tasks"]
        
        message = (f"Here are the stats for today: \n\n • New Sig Ups: {new_signups} \n • New Task Orders: {new_task} \n • Approved Task Orders: {approved_tasks} \n • Rejected Task Orders: {rejected_tasks} \n")
        
        await update.callback_query.message.reply_text(f"{message}")
    else:
        await update.callback_query.message.reply_text("Failed to fetch wallet balance.")
    
    await update.message.reply_text(f'{message} \n\n\n DATE: {today_date}')