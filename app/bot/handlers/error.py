def error_handler(update, context):
    """
    Log the error in sentry
    """
    print(context.error)
