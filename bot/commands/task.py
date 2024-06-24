from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

from ..extensions import api


async def fetch_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_data = api.fetch_tasks()
    tasks = response_data["all_tasks"]
    if tasks:
        message = "\n\n".join(
                [
                    f"- Task {task['id']}: \n \
        • Task Type: {task["task_type"]} \n \
        • Payment Status: {task["payment_status"]} \n \
        • Platform: {task["platform"]} \n \
        • Amount Paid: {task["fee_paid"]} \n \
        \n \
        • Status: {task["status"]} \n \
        • Date Created: {task["date_created"]} \n \
                    " for task in tasks
                ]
            )
        
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