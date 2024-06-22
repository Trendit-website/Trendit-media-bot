from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

from .commands import register_commands
from .handlers import error_handler, callback_query_handler
from .responses import handle_message, handle_response
from config import Config

def main():
    """Start the bot."""
    print("starting Bot...")
    
    token = Config.TELEGRAM_BOT_TOKEN
    
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()
    
    # Add handlers
    register_commands(app=application)
    
    # messages
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    application.add_error_handler(error_handler)
    
    # Polls the bot
    print("Polling...")
    application.run_polling(poll_interval=3)
    

    # # Handle callback queries (e.g., buttons in Telegram messages)
    # application.add_handler(CallbackQueryHandler(callback_query_handler))
