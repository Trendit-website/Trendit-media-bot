from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import date

from ..extensions import api
from ..utils.helpers import console_log
from ..commands import fetch_balance, send_notification, update_prices


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    
    console_log("query", query)
    console_log("action", query.data)
    
    if query.data in ["fetch_balance", "fetch_stats", "send_notification"]:
        action = query.data
        
        if action == "fetch_balance":
            await fetch_balance(update, context)
        elif action == "send_notification":
            await send_notification(update, context)
        elif action == "fetch_stats":
            await fetch_stats_callback(update, context)
    else:
        data = query.data.split('_')
        action, item_type, item_id = data[0], data[1], data[2]

        if item_type == "task":
            if action == "approve":
                response_data = api.approve_task(item_id)
                if response_data:
                    await query.edit_message_text(f"{response_data['message']}")
                else:
                    await query.edit_message_text(f"Failed to approve task {item_id}.")
            elif action == "reject":
                response_data = api.reject_task(item_id)
                if response_data:
                    await query.edit_message_text(f"Task {item_id} rejected.")
                else:
                    await query.edit_message_text(f"Failed to reject task {item_id}.")
        elif item_type == "profile":
            if action == "accept":
                response_data = api.approve_social_profile(item_id)
                if response_data:
                    await query.edit_message_text(f"{response_data['message']}")
                else:
                    await query.edit_message_text(f"Failed to accept profile {item_id}.")
            elif action == "reject":
                response_data = api.reject_social_profile(item_id)
                if response_data:
                    await query.edit_message_text(f"{response_data['message']}")
                else:
                    await query.edit_message_text(f"Failed to reject profile {item_id}.")
    
    await query.answer()


async def fetch_stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    response_data = api.fetch_stats()
    stats = response_data["stats"]
    
    today = date.today()
    today_date = today.strftime("%B %d, %Y")
    
    if stats:
        new_signups = stats["new_signups"]
        new_task = stats["new_task"]
        approved_tasks = stats["approved_tasks"]
        rejected_tasks = stats["declined_tasks"]
        
        message = (f"Here are the stats for today: \n\n • New Sig Ups: {new_signups} \n • New Task Orders: {new_task} \n • Approved Task Orders: {approved_tasks} \n • Rejected Task Orders: {rejected_tasks} \n")
        
        await update.callback_query.message.reply_text(f"{message} \n\n\n DATE: {today_date}")
    else:
        await update.callback_query.message.reply_text("Failed to fetch wallet balance.")
    
    await update.callback_query.answer()
