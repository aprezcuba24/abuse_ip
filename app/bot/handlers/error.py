import traceback


def error_handler(update, context):
    """
    Log the error in sentry
    """
    print(traceback.format_exc())
