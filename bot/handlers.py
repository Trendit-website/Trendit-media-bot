from .utils.helpers import console_log


def error_handler(update, context):
    """Log Errors caused by Updates."""
    console_log(f"update {update} caused error:", str(context.error))

def callback_query_handler(update, context):
    """Handle callback queries triggered by inline button presses."""
    query = update.callback_query
    query.answer()
    # Handle the callback query based on its data
