from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

from ..extensions import api


async def fetch_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_data = api.fetch_tasks()
    tasks = response_data["all_tasks"]
    
    message = "\n\n"
    if tasks:
        for task in tasks:
            task_id = task["id"]
            task_type = task["task_type"]
            payment_status = task["payment_status"]
            platform = task["platform"]
            fee_paid = task["fee_paid"]
            status = task["status"]
            date_created = task["date_created"]
            message.join(f"- Task {task_id}: \n • Task Type: {task_type} \n • Payment Status: {payment_status} \n • Platform: {platform} \n • Amount Paid: {fee_paid} \n • Status: {status} \n • Date Created: {date_created} \n\n ")
        
        
        await update.message.reply_text(f"Tasks:\n{message}")
    else:
        await update.message.reply_text("No tasks available.")

async def approve_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task_id = context.args[0]
    if api.approve_task(task_id):
        await update.message.reply_text(f"Task {task_id} approved.")
    else:
        await update.message.reply_text(f"Failed to approve task {task_id}.")

async def reject_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task_id = context.args[0]
    if api.reject_task(task_id):
        await update.message.reply_text(f"Task {task_id} rejected.")
    else:
        await update.message.reply_text(f"Failed to reject task {task_id}.")