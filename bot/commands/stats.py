from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ContextTypes


from ..extensions import api

async def fetch_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /fetch_stats is issued."""
    response_data = api.fetch_stats()
    response_data_msg = response_data["message"]
    stats = response_data["stats"]
    
    
    if stats:
        new_signups = stats["new_signups"]
        new_task = stats["new_task"]
        approved_tasks = stats["approved_tasks"]
        rejected_tasks = stats["declined_tasks"]
        pending_tasks = stats["pending_tasks"]
        
        message = (f"Here are the stats for today: \n\n • New Sign Ups: {new_signups} \n • New Task Orders: {new_task} \n • Approved Task Orders: {approved_tasks} \n • Rejected Task Orders: {rejected_tasks} \n • Pending Task Orders: {pending_tasks} \n")
        
        await update.message.reply_text(f'{message} \n')
    else:
        await update.message.reply_text(f"Failed to fetch Stats: \n\n {response_data_msg}")
