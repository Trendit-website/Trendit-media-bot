from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ContextTypes


from ..extensions import api

async def pending_social_profiles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /fetch_stats is issued."""
    response_data = api.webhook_get_pending_social_profiles()
    response_data_msg = response_data["message"]
    pending_social_profiles = response_data["pending_social_profiles"]
    
    
    if pending_social_profiles:
        message = (f"{response_data_msg}")
        
        await update.message.reply_text(f'{message} \n')
    else:
        await update.message.reply_text(f"Failed to fetch Stats: \n\n {response_data_msg}")
