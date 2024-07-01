from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

from ..extensions import api


async def fetch_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_data = api.fetch_tasks()
    tasks = response_data["all_tasks"]
    
    message = f""
    if tasks:
        for task in tasks:
            task_id = task["id"]
            task_type = task["task_type"]
            payment_status = task["payment_status"]
            platform = task["platform"]
            fee_paid = task["fee_paid"]
            status = task["status"]
            date_created = task["date_created"]
            
            requested_count = task.get("posts_count")
            
            if not requested_count:
                requested_count = task.get("engagements_count")
            
            count = "No of posts" if task.get("posts_counts") else "No of Engagements"
            
            task_info = (f"- Task {task_id}: \n • Task Type: {task_type} \n • Payment Status: {payment_status} \n • Platform: {platform} \n • Amount Paid: {fee_paid} \n • {count}: {requested_count} \n • Status: {status} \n • Date Created: {date_created} ")
            
            formatted = f"\n\n{task_id:-^29}\n {task_info} \n{'//':-^29}"
            message = message + (formatted)
        
        await update.message.reply_text(f"10 Tasks per Page:\n{message}")
    else:
        await update.message.reply_text("No tasks available.")


async def pending_task_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_data = api.send_pending_tasks()
    response_data_msg = response_data.get("message", "Fetching pending task orders")
    pending_tasks = response_data.get("pending_tasks", None)
    
    
    if pending_tasks:
        message = (f"{response_data_msg}")
        
        await update.message.reply_text(f'{message} \n')
    else:
        await update.message.reply_text(f"Failed to fetch pending social profile : \n\n {response_data_msg}")



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