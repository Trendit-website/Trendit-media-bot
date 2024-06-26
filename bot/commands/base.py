from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton("Fetch Balance", callback_data='fetch_balance')],
        [InlineKeyboardButton("Fetch Stats For The Day", callback_data='fetch_stats')],
        [InlineKeyboardButton("Send Notification", callback_data='send_notification')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    firstname = update.message.from_user.first_name
    
    await update.message.reply_text(f'Hi {firstname}! \n\nI am the trendit bot designed to assist admins. What would You like to do?' , reply_markup=reply_markup)
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am here to assist you.')

async def group_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send group ID when the command /group_id is issued."""
    chat = update.effective_chat
    if chat.type in ['group', 'supergroup']:
        await update.message.reply_text(f"This is the Group ID: {chat.id}")
    else:
        await update.message.reply_text(f"This is your personal Id: {chat.id}")
