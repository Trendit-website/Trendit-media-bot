from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

from .commands import register_commands
from .responses import register_responses
from .handlers import error_handler, callback_query_handler
from config import Config, logger

def main():
    """Start the bot."""
    logger.info("Starting Bot...\n\n")
    
    token = Config.TELEGRAM_BOT_TOKEN
    
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()
    
    # Add handlers
    register_commands(app=application)
    
    # messages responses
    register_responses(app=application)
    
    # Errors
    application.add_error_handler(error_handler)
    
    # Polls the bot
    logger.info("Polling... \n\n")
    
    application.run_polling(poll_interval=3)
    

    # # Handle callback queries (e.g., buttons in Telegram messages)
    # application.add_handler(CallbackQueryHandler(callback_query_handler))
